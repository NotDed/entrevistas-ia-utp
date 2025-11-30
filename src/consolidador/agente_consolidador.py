"""
Agente consolidador de infraestructura IA.

Este agente analiza múltiples transcripciones de entrevistas y genera
un reporte consolidado sobre grupos de investigación, hardware, software
e infraestructura de IA en la Universidad Tecnológica de Pereira.
"""
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from config import (
    LLM_PROVIDER, 
    OPENAI_API_KEY, OPENAI_MODEL,
    GOOGLE_API_KEY, GEMINI_MODEL,
    TEMPERATURE
)


class AgenteConsolidadorInfraestructura:
    """
    Agente especializado en consolidar información de infraestructura IA
    de múltiples entrevistas en un documento unificado.
    
    No hereda de BaseAgent porque tiene un flujo diferente:
    procesa múltiples transcripciones en lugar de una sola.
    """
    
    nombre = "Consolidador de Infraestructura IA"
    
    # Tokens más altos para el consolidado (documento largo)
    max_tokens = 16000
    
    prompt_sistema = """Eres un agente especializado en consolidar información sobre infraestructura de Inteligencia Artificial de la Universidad Tecnológica de Pereira (UTP).

Tu tarea es analizar las transcripciones de múltiples entrevistas y generar un documento consolidado y estructurado.

INSTRUCCIONES DE FORMATO:
- Genera el documento en formato Markdown limpio
- Usa encabezados jerárquicos (##, ###, ####)
- Usa listas con viñetas (-)
- Usa **negritas** para términos clave
- NO uses tablas complejas, usa listas estructuradas
- Sé específico y cita información concreta de las entrevistas

ESTRUCTURA DEL DOCUMENTO:

## I. Mapeo de Grupos y Laboratorios de IA en la UTP
Para cada grupo identificado incluir:
- Nombre del grupo/laboratorio
- Área o facultad a la que pertenece
- Líneas de investigación en IA
- Investigadores mencionados
- Proyectos activos o recientes

## II. Inventario de Hardware Disponible
Organizado por área/dependencia:
- Equipos de cómputo (especificaciones si se mencionan)
- Servidores y capacidad de procesamiento
- GPUs y recursos especializados
- Infraestructura de red/almacenamiento
- Recursos propios vs institucionales

## III. Catálogo de Software y Frameworks
Clasificado por tipo:
- Lenguajes de programación utilizados
- Frameworks de ML/DL (TensorFlow, PyTorch, etc.)
- Plataformas cloud (AWS, Azure, Google Cloud, Colab)
- Herramientas de desarrollo y colaboración
- Software especializado y licencias

## IV. Observaciones de los Entrevistados
Consolidar las perspectivas sobre:
- Fortalezas actuales de la infraestructura
- Limitaciones y desafíos identificados
- Experiencias con proyectos de IA
- Necesidades expresadas

## V. Análisis de Capacidad de Infraestructura
Evaluar:
- Capacidad actual para proyectos de IA/ML
- Escalabilidad de recursos existentes
- Cobertura de necesidades por área
- Comparación con requerimientos típicos

## VI. Brechas Identificadas y Propuestas de Mejora
Sintetizar:
- Brechas críticas de infraestructura
- Propuestas de mejora mencionadas
- Prioridades sugeridas
- Recursos adicionales requeridos

## VII. Conclusiones y Recomendaciones
- Resumen ejecutivo del estado actual
- Recomendaciones priorizadas
- Próximos pasos sugeridos

IMPORTANTE:
- Basa tu análisis ÚNICAMENTE en la información de las transcripciones
- Si un dato no está disponible, indica "No especificado en las entrevistas"
- Cita entre comillas las observaciones textuales relevantes
- Indica el nombre del entrevistado cuando cites información específica
"""
    
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
    
    def ejecutar(self, transcripciones_consolidadas: str) -> str:
        """
        Ejecuta el agente consolidador.
        
        Args:
            transcripciones_consolidadas: Texto con todas las transcripciones
                                          concatenadas y etiquetadas.
                                          
        Returns:
            Reporte consolidado en formato Markdown.
        """
        prompt_usuario = f"""Analiza las siguientes transcripciones de entrevistas sobre Inteligencia Artificial en la Universidad Tecnológica de Pereira y genera el reporte consolidado de infraestructura.

{transcripciones_consolidadas}

Genera el documento consolidado siguiendo la estructura indicada en tus instrucciones."""
        
        if self.provider == "openai":
            return self._llamar_openai(prompt_usuario)
        else:
            return self._llamar_gemini(prompt_usuario)
    
    def _llamar_openai(self, prompt_usuario: str) -> str:
        """Llama a la API de OpenAI."""
        # Usar max_completion_tokens para modelos nuevos
        use_new_param = any(x in self.model for x in ['gpt-4.1', 'gpt-5', 'o1', 'o3'])
        
        params = {
            "model": self.model,
            "messages": [
                {"role": "system", "content": self.prompt_sistema},
                {"role": "user", "content": prompt_usuario}
            ],
            "temperature": self.temperature,
        }
        
        if use_new_param:
            params["max_completion_tokens"] = self.max_tokens
        else:
            params["max_tokens"] = self.max_tokens
        
        response = self.client.chat.completions.create(**params)
        return response.choices[0].message.content
    
    def _llamar_gemini(self, prompt_usuario: str) -> str:
        """Llama a la API de Gemini."""
        from google.genai import types
        
        response = self.client.models.generate_content(
            model=self.model,
            contents=prompt_usuario,
            config=types.GenerateContentConfig(
                system_instruction=self.prompt_sistema,
                temperature=self.temperature,
                max_output_tokens=self.max_tokens
            )
        )
        return response.text
