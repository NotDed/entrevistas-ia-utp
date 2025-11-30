"""
Agente para identificar hallazgos clave de la entrevista.
Genera la sección VII del reporte.
"""
from .base_agent import BaseAgent


class AgenteHallazgosClave(BaseAgent):
    """
    Identifica y sintetiza los hallazgos más relevantes 
    de la entrevista en forma de puntos destacados.
    """
    
    @property
    def nombre_seccion(self) -> str:
        return "VII. Hallazgos clave"
    
    @property
    def prompt_sistema(self) -> str:
        return """Eres un agente especializado en identificar hallazgos clave de entrevistas sobre IA en la UTP.

La entrevista sigue una guía de 4 bloques:
1. Experiencia técnica y práctica aplicada
2. Desarrollo, innovación y transferencia tecnológica
3. Colaboración, liderazgo y visión estratégica
4. Motivación y proyección profesional

Tu tarea es sintetizar los puntos más relevantes:
- Fortalezas y capacidades demostradas
- Proyectos e impacto logrado
- Desafíos y necesidades identificadas
- Propuestas concretas
- Oportunidades para el ecosistema de IA

IMPORTANTE:
- Los hallazgos deben ser concretos y accionables.
- NO uses "No mencionado".
- EVITA frases como "se destaca que" o "cabe mencionar". Ve directo al hallazgo."""
    
    @property
    def instrucciones_extraccion(self) -> str:
        return """
INSTRUCCIONES PARA LA SECCIÓN "VII. Hallazgos clave":

Identifica entre 5 y 7 hallazgos clave de la entrevista, considerando:

1. **Fortalezas identificadas**: Capacidades, experiencias o recursos destacables
2. **Oportunidades**: Áreas de desarrollo o aplicación prometedoras
3. **Desafíos críticos**: Problemas o limitaciones importantes mencionadas
4. **Propuestas concretas**: Sugerencias específicas realizadas por el entrevistado
5. **Insights estratégicos**: Observaciones relevantes para la estrategia institucional

Cada hallazgo debe:
- Ser específico y basado en la transcripción
- Incluir contexto suficiente para entenderlo
- Ser relevante para la toma de decisiones

Identificar entre 5 y 7 hallazgos CONCRETOS y ACCIONABLES. Cada hallazgo debe responder:

1. ¿Qué se descubrió o identificó específicamente?
2. ¿Por qué es relevante para la UTP?
3. ¿Qué acción o decisión podría derivarse?

Categorías de hallazgos a buscar:
- **Capacidades técnicas**: ¿Qué sabe hacer el entrevistado que es valioso?
- **Proyectos activos**: ¿Qué está funcionando y podría escalarse?
- **Brechas críticas**: ¿Qué falta (infraestructura, talento, datos, recursos)?
- **Oportunidades de innovación**: ¿Qué propuestas concretas hizo?
- **Redes y colaboraciones**: ¿Con quiénes trabaja y qué aportan?
- **Riesgos identificados**: ¿Qué podría perderse si no se actúa?

FORMATO:
**[Número]. [Título específico del hallazgo]:**
Descripción concreta con datos, nombres, cifras cuando estén disponibles.
- **Relevancia para la UTP:** Una línea explicando por qué importa.
- **Acción sugerida:** Una línea con recomendación concreta.

NO incluir:
- Hallazgos genéricos que apliquen a cualquier entrevistado
- Sección de "síntesis ejecutiva" al final (se genera en otro documento)
- Resúmenes redundantes
"""
