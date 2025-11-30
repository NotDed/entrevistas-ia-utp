"""
Agente para generar el resumen general de la entrevista.
Genera la sección II del reporte.
"""
from .base_agent import BaseAgent


class AgenteResumenGeneral(BaseAgent):
    """
    Genera un resumen ejecutivo de los temas principales 
    discutidos en la entrevista.
    """
    
    @property
    def nombre_seccion(self) -> str:
        return "II. Resumen general de la entrevista"
    
    @property
    def prompt_sistema(self) -> str:
        return """Eres un agente especializado en sintetizar entrevistas sobre 
inteligencia artificial realizadas en la Universidad Tecnológica de Pereira (UTP).

La entrevista sigue una guía estructurada en 4 bloques:
1. Experiencia técnica y práctica aplicada
2. Desarrollo, innovación y transferencia tecnológica  
3. Colaboración, liderazgo y visión estratégica
4. Motivación y proyección profesional

IMPORTANTE:
- Las transcripciones pueden contener errores. Interpreta el contexto.
- NO uses "No mencionado". Solo incluye lo que SÍ se discutió.
- EVITA frases redundantes como "el entrevistado mencionó", "durante la entrevista", "participó en proyectos de IA".
- Ve directo al contenido: qué proyectos, qué herramientas, qué propuestas."""
    
    @property
    def instrucciones_extraccion(self) -> str:
        return """
INSTRUCCIONES PARA LA SECCIÓN "II. Resumen general de la entrevista":

Genera un resumen ejecutivo de 2-3 párrafos con los principales aportes.

EVITAR:
- "El entrevistado ha participado en..."
- "Se mencionó que..."
- "Durante la entrevista se discutió..."

PREFERIR estilo directo:
- "Desarrolló un modelo de clasificación de especies..."
- "Colabora con el grupo GIROPS en..."
- "Propone aplicar IA para..."

FORMATO: Texto corrido en párrafos, sin listas, directo al contenido.
"""
