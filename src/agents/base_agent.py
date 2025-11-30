"""
Clase base para todos los agentes del sistema multi-agente.
Cada agente hereda de esta clase e implementa su prompt específico.
Soporta OpenAI y Google Gemini como proveedores de LLM.
"""
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from abc import ABC, abstractmethod
from config import (
    LLM_PROVIDER, 
    OPENAI_API_KEY, OPENAI_MODEL,
    GOOGLE_API_KEY, GEMINI_MODEL,
    MAX_TOKENS, TEMPERATURE, REGLAS_GLOBALES
)


class BaseAgent(ABC):
    """
    Agente base que procesa transcripciones de entrevistas.
    Los agentes hijos definen el prompt específico para su sección.
    Soporta OpenAI y Gemini como proveedores.
    """
    
    def __init__(self):
        self.provider = LLM_PROVIDER.lower()
        self.max_tokens = MAX_TOKENS
        self.temperature = TEMPERATURE
        
        if self.provider == "openai":
            from openai import OpenAI
            self.client = OpenAI(api_key=OPENAI_API_KEY)
            self.model = OPENAI_MODEL
        else:  # gemini
            from google import genai
            self.client = genai.Client(api_key=GOOGLE_API_KEY)
            self.model = GEMINI_MODEL
    
    @property
    @abstractmethod
    def nombre_seccion(self) -> str:
        """Nombre de la sección que genera este agente (ej: 'I. Datos básicos')"""
        pass
    
    @property
    @abstractmethod
    def prompt_sistema(self) -> str:
        """Prompt del sistema que define el rol y tarea específica del agente."""
        pass
    
    @property
    @abstractmethod
    def instrucciones_extraccion(self) -> str:
        """Instrucciones específicas sobre qué información extraer."""
        pass
    
    def construir_prompt_usuario(self, transcripcion: str) -> str:
        """
        Construye el prompt de usuario con la transcripción.
        """
        return f"""
{REGLAS_GLOBALES}

{self.instrucciones_extraccion}

---
TRANSCRIPCIÓN DE LA ENTREVISTA:
---
{transcripcion}
---

Genera ÚNICAMENTE la sección "{self.nombre_seccion}" en formato Markdown.
"""
    
    def _llamar_openai(self, prompt_sistema: str, prompt_usuario: str) -> str:
        """Llama a la API de OpenAI."""
        # Modelos nuevos (gpt-4.1, o1, etc.) usan max_completion_tokens
        # Modelos antiguos (gpt-4o-mini, gpt-4, etc.) usan max_tokens
        use_new_param = any(x in self.model for x in ['gpt-4.1', 'gpt-5', 'o1', 'o3'])
        
        params = {
            "model": self.model,
            "messages": [
                {"role": "system", "content": prompt_sistema},
                {"role": "user", "content": prompt_usuario}
            ],
            "temperature": self.temperature
        }
        
        if use_new_param:
            params["max_completion_tokens"] = self.max_tokens
        else:
            params["max_tokens"] = self.max_tokens
        
        response = self.client.chat.completions.create(**params)
        return response.choices[0].message.content.strip()
    
    def _llamar_gemini(self, prompt_completo: str) -> str:
        """Llama a la API de Google Gemini."""
        from google.genai import types
        response = self.client.models.generate_content(
            model=self.model,
            contents=prompt_completo,
            config=types.GenerateContentConfig(
                max_output_tokens=self.max_tokens,
                temperature=self.temperature
            )
        )
        return response.text.strip()
    
    def process(self, transcripcion: str) -> str:
        """
        Procesa la transcripción y genera el contenido de la sección.
        """
        import time
        max_retries = 3
        
        prompt_usuario = self.construir_prompt_usuario(transcripcion)
        
        for attempt in range(max_retries):
            try:
                if self.provider == "openai":
                    return self._llamar_openai(self.prompt_sistema, prompt_usuario)
                else:
                    prompt_completo = f"{self.prompt_sistema}\n\n{prompt_usuario}"
                    return self._llamar_gemini(prompt_completo)
                    
            except Exception as e:
                error_str = str(e)
                if "429" in error_str or "RESOURCE_EXHAUSTED" in error_str or "rate" in error_str.lower():
                    wait_time = 10 * (attempt + 1)
                    print(f"      ⏳ Rate limit. Esperando {wait_time}s...")
                    time.sleep(wait_time)
                    continue
                return f"## {self.nombre_seccion}\n\n**Error al procesar:** {str(e)}"
        
        return f"## {self.nombre_seccion}\n\n**Error:** Rate limit excedido."
    
    async def process_async(self, transcripcion: str) -> str:
        """Versión asíncrona del procesamiento."""
        return self.process(transcripcion)
