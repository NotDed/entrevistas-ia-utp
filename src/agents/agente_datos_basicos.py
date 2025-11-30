"""
Agente para extraer datos básicos del entrevistado.
Genera la sección I del reporte.
"""
from .base_agent import BaseAgent


class AgenteDatosBasicos(BaseAgent):
    """
    Extrae información básica del entrevistado como nombre, rol, 
    facultad, grupo de investigación, etc.
    """
    
    @property
    def nombre_seccion(self) -> str:
        return "I. Datos básicos del entrevistado"
    
    @property
    def prompt_sistema(self) -> str:
        return """Eres un agente especializado en extraer datos básicos de entrevistados 
a partir de transcripciones de entrevistas sobre inteligencia artificial en la 
Universidad Tecnológica de Pereira (UTP).

IMPORTANTE:
- Las transcripciones pueden contener errores. Interpreta el contexto.
- NO escribas "No mencionado". Si un dato no aparece, omítelo.
- Solo incluye información que SÍ aparece en la transcripción.
- EVITA información obvia o implícita como "participó en la entrevista" o "es entrevistado".
- Ve directo al contenido sustantivo.
- Si es una ENTREVISTA GRUPAL, lista todos los participantes identificados.

Mantén un tono formal y conciso."""
    
    @property
    def instrucciones_extraccion(self) -> str:
        return """
INSTRUCCIONES PARA LA SECCIÓN "I. Datos básicos del entrevistado":

El nombre del entrevistado se proporciona. Extrae SOLO: rol/cargo, facultad, grupo de investigación, programa académico y área de especialización.

Si es ENTREVISTA GRUPAL:
- Lista cada participante identificado
- Incluye el área/dependencia que representan
- Menciona roles individuales si se identifican

EVITAR frases como:
- "El entrevistado participó en..."
- "Durante la entrevista mencionó..."
- "Es parte de la universidad..."

FORMATO: Un párrafo breve y directo con los datos concretos.
"""
    
    def process(self, transcripcion: str, nombre_entrevistado: str = None, info_entrevista = None) -> str:
        """
        Procesa la transcripción incluyendo el nombre del entrevistado.
        
        Args:
            transcripcion: Texto de la transcripción (puede incluir contexto).
            nombre_entrevistado: Nombre del entrevistado o área.
            info_entrevista: InfoEntrevista con detalles de tipo de entrevista.
        """
        import time
        from config import REGLAS_GLOBALES
        
        max_retries = 3
        
        # Construir información del encabezado según tipo de entrevista
        if info_entrevista and info_entrevista.es_grupal:
            nombre_info = f"""
TIPO DE ENTREVISTA: GRUPAL
PARTICIPANTES: {', '.join(info_entrevista.nombres)}
ÁREA/DEPENDENCIA: {info_entrevista.area_dependencia or 'No especificada'}
"""
        else:
            nombre_info = f"\nNOMBRE DEL ENTREVISTADO: {nombre_entrevistado}\n" if nombre_entrevistado else ""
        
        prompt_usuario = f"""{REGLAS_GLOBALES}
{nombre_info}
{self.instrucciones_extraccion}

---
TRANSCRIPCIÓN DE LA ENTREVISTA:
---
{transcripcion}
---

Genera ÚNICAMENTE la sección "{self.nombre_seccion}" en formato Markdown.
"""
        
        for attempt in range(max_retries):
            try:
                if self.provider == "openai":
                    # Modelos nuevos usan max_completion_tokens
                    use_new_param = any(x in self.model for x in ['gpt-4.1', 'gpt-5', 'o1', 'o3'])
                    params = {
                        "model": self.model,
                        "messages": [
                            {"role": "system", "content": self.prompt_sistema},
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
                else:  # gemini
                    from google.genai import types
                    prompt_completo = f"{self.prompt_sistema}\n\n{prompt_usuario}"
                    response = self.client.models.generate_content(
                        model=self.model,
                        contents=prompt_completo,
                        config=types.GenerateContentConfig(
                            max_output_tokens=self.max_tokens,
                            temperature=self.temperature
                        )
                    )
                    return response.text.strip()
            except Exception as e:
                error_str = str(e)
                if "429" in error_str or "RESOURCE_EXHAUSTED" in error_str or "rate" in error_str.lower():
                    wait_time = 10 * (attempt + 1)
                    print(f"      ⏳ Rate limit. Esperando {wait_time}s...")
                    time.sleep(wait_time)
                    continue
                return f"## {self.nombre_seccion}\n\n**Error al procesar:** {str(e)}"
        
        return f"## {self.nombre_seccion}\n\n**Error:** Rate limit excedido."
