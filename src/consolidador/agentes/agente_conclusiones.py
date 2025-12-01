"""
Agente especializado en generar conclusiones ejecutivas.
"""
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from consolidador.base_agent_consolidador import BaseAgentConsolidador


class AgenteConclusiones(BaseAgentConsolidador):
    """
    Genera una síntesis ejecutiva con las conclusiones principales
    del análisis consolidado de capacidades de IA en la UTP.
    """
    
    @property
    def nombre_seccion(self) -> str:
        return "VIII. Conclusiones y Síntesis Ejecutiva"
    
    @property
    def prompt_sistema(self) -> str:
        return """Eres un líder de investigación con visión estratégica que reconoce el valor
del trabajo colectivo y puede inspirar a otros hacia una visión compartida.

Tu tarea es generar conclusiones que sinteticen el análisis, RECONOCIENDO el trabajo
de los equipos y MOTIVANDO hacia el futuro de la IA en la UTP.

Debes:
- Sintetizar los hallazgos más importantes de forma inspiradora
- Reconocer los logros y el trabajo de los equipos
- Presentar una visión clara y motivadora del futuro
- Conectar fortalezas actuales con el potencial futuro
- Generar un llamado a la acción que inspire colaboración

Escribe con un tono que inspire orgullo y motivación para avanzar juntos."""
    
    @property
    def instrucciones_extraccion(self) -> str:
        return """
INSTRUCCIONES PARA LA SECCIÓN "VIII. Conclusiones y Síntesis Ejecutiva":

Comienza con un párrafo inspirador que reconozca el valor del ecosistema de IA en la UTP
y el trabajo de los equipos que lo hacen posible.

### 8.1 Reconocimiento del Ecosistema Actual
Narra el estado actual de forma positiva pero realista:
- Riqueza y diversidad de los equipos de investigación
- Capacidades consolidadas y en desarrollo
- Potencial del talento humano existente

### 8.2 Hallazgos Clave
Presenta los 5-7 descubrimientos más importantes:
- Fortalezas que destacan
- Desafíos que merecen atención
- Oportunidades que no deben desaprovecharse

Usa bullet points para sintetizar cada hallazgo clave.

### 8.3 Reconocimiento a los Equipos
Celebra específicamente:
- El trabajo de los grupos de investigación identificados
- Los logros alcanzados con los recursos disponibles
- El compromiso con el avance de la IA en la UTP

### 8.4 Factores Críticos de Éxito
Identifica qué es esencial para avanzar:
- Condiciones necesarias para el crecimiento
- Recursos críticos a asegurar
- Capacidades a desarrollar

### 8.5 Visión de Futuro
Presenta una visión inspiradora:
- Hacia dónde puede llegar la UTP en IA
- Rol que pueden jugar los equipos
- Impacto potencial regional y nacional

### 8.6 Llamado a la Acción
Cierra con un mensaje motivador:
- Urgencia de aprovechar el momento
- Invitación a la colaboración entre equipos
- Compromiso institucional necesario

FORMATO: Escribe de forma que inspire orgullo y motivación.
Alterna prosa narrativa con bullet points para los puntos clave.
"""
