"""
Clase base abstracta para agentes consolidadores.

Los agentes consolidadores procesan múltiples transcripciones de entrevistas
y generan una sección específica del reporte consolidado.
"""
import sys
import os
from abc import ABC, abstractmethod

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from config import (
    LLM_PROVIDER,
    OPENAI_API_KEY, OPENAI_MODEL,
    GOOGLE_API_KEY, GEMINI_MODEL,
    TEMPERATURE, MAX_TOKENS
)


class BaseAgentConsolidador(ABC):
    """
    Clase base abstracta para agentes que consolidan información
    de múltiples entrevistas en una sección específica del reporte.
    
    Cada agente hereda de esta clase y define:
    - nombre_seccion: título de la sección que genera
    - prompt_sistema: rol y contexto del agente
    - instrucciones_extraccion: qué información extraer y cómo formatearla
    """
    
    # Tokens por sección (más bajo que el consolidador monolítico)
    max_tokens = 4000
    
    def __init__(self):
        self.provider = LLM_PROVIDER.lower()
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
        """Título de la sección que genera este agente (ej: 'I. Grupos y Laboratorios')"""
        pass
    
    @property
    @abstractmethod
    def prompt_sistema(self) -> str:
        """Prompt del sistema que define el rol y contexto del agente."""
        pass
    
    @property
    @abstractmethod
    def instrucciones_extraccion(self) -> str:
        """Instrucciones específicas de qué información extraer y cómo formatearla."""
        pass
    
    def _construir_prompt(self, transcripciones: str) -> str:
        """Construye el prompt completo para el LLM."""
        return f"""
{self.prompt_sistema}

REGLAS IMPORTANTES:
- NO menciones nombres de entrevistados directamente (ej: "según Juan García...")
- NO hagas referencias explícitas a entrevistas específicas (ej: "en la entrevista 3...")
- Sintetiza y agrupa la información de TODAS las entrevistas
- Presenta los hallazgos como descubrimientos del análisis institucional
- Usa lenguaje impersonal y profesional
- Si múltiples fuentes mencionan lo mismo, preséntalo como hallazgo consolidado
- Solo incluye información que SÍ fue mencionada, no inventes datos

FORMATO DE SALIDA:
- Usa Markdown con jerarquía de encabezados (##, ###, ####)
- Las viñetas (-) solo para items finales, NO para categorías
- Usa **negritas** para términos clave
- Mantén un tono formal de informe ejecutivo

{self.instrucciones_extraccion}

---
TRANSCRIPCIONES A ANALIZAR:
---

{transcripciones}

---

Genera ÚNICAMENTE la sección "{self.nombre_seccion}" siguiendo las instrucciones anteriores.
"""
    
    def ejecutar(self, transcripciones: str) -> str:
        """
        Procesa las transcripciones y genera la sección correspondiente.
        
        Args:
            transcripciones: Texto concatenado de todas las entrevistas
            
        Returns:
            Contenido Markdown de la sección generada
        """
        prompt = self._construir_prompt(transcripciones)
        
        if self.provider == "openai":
            return self._llamar_openai(prompt)
        else:
            return self._llamar_gemini(prompt)
    
    async def ejecutar_async(self, transcripciones: str) -> str:
        """Versión asíncrona de ejecutar (para procesamiento paralelo)."""
        import asyncio
        return await asyncio.get_event_loop().run_in_executor(
            None, self.ejecutar, transcripciones
        )
    
    def _llamar_openai(self, prompt: str) -> str:
        """Llama a la API de OpenAI."""
        params = {
            "model": self.model,
            "messages": [
                {"role": "user", "content": prompt}
            ],
            "max_tokens": self.max_tokens,
            "temperature": self.temperature,
        }
        
        response = self.client.chat.completions.create(**params)
        return response.choices[0].message.content.strip()
    
    def _llamar_gemini(self, prompt: str) -> str:
        """Llama a la API de Google Gemini."""
        response = self.client.models.generate_content(
            model=self.model,
            contents=prompt,
            config={
                "max_output_tokens": self.max_tokens,
                "temperature": self.temperature,
            }
        )
        return response.text.strip()
