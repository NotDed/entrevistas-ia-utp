"""
Agente especializado en identificar limitaciones y desafíos.
"""
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from consolidador.base_agent_consolidador import BaseAgentConsolidador


class AgenteLimitaciones(BaseAgentConsolidador):
    """
    Extrae y sintetiza las limitaciones, desafíos, brechas y 
    obstáculos identificados para el desarrollo de IA en la UTP.
    """
    
    @property
    def nombre_seccion(self) -> str:
        return "V. Limitaciones y Desafíos Identificados"
    
    @property
    def prompt_sistema(self) -> str:
        return """Eres un consultor estratégico que identifica desafíos de manera constructiva,
reconociendo el contexto y los esfuerzos de los equipos por superar obstáculos.

Tu tarea es identificar las limitaciones y desafíos que enfrentan los equipos de IA en la UTP,
presentándolos como oportunidades de mejora y no como críticas.

Debes:
- Identificar limitaciones de recursos e infraestructura
- Reconocer los desafíos que enfrentan los equipos
- Contextualizar las limitaciones en el entorno institucional
- Presentar los desafíos de manera que inspire soluciones
- Valorar los esfuerzos por superar obstáculos

Escribe de forma empática y constructiva, orientada a la mejora."""
    
    @property
    def instrucciones_extraccion(self) -> str:
        return """
INSTRUCCIONES PARA LA SECCIÓN "V. Limitaciones y Desafíos Identificados":

Comienza con un párrafo que contextualice los desafíos como parte natural del crecimiento,
reconociendo que identificarlos es el primer paso para superarlos.

### 5.1 Desafíos de Infraestructura
Narra los retos en recursos computacionales:
- Necesidades de hardware más potente
- Capacidad de procesamiento actual vs requerida
- Oportunidades de mejora en equipamiento

Reconoce lo que los equipos han logrado con recursos limitados.

### 5.2 Desafíos en Talento y Capacidades
Describe los retos en recursos humanos:
- Necesidades de personal especializado
- Oportunidades de capacitación y formación
- Balance entre docencia e investigación

### 5.3 Desafíos Financieros
Contextualiza las restricciones presupuestales:
- Limitaciones para adquirir recursos
- Dependencia de financiación por proyectos
- Costos de tecnologías y servicios

### 5.4 Desafíos Institucionales
Identifica barreras organizacionales:
- Procesos administrativos que podrían agilizarse
- Oportunidades de mejor articulación
- Políticas que podrían fortalecerse

### 5.5 Desafíos Técnicos
Describe retos tecnológicos:
- Acceso a datos para investigación
- Integración de sistemas y herramientas
- Actualización tecnológica

### 5.6 Desafíos de Articulación
Narra oportunidades de mejor colaboración:
- Trabajo que podría integrarse mejor
- Recursos que podrían compartirse
- Espacios de encuentro entre equipos

FORMATO: Presenta los desafíos de manera constructiva, orientada a soluciones.
Usa bullet points para listar aspectos específicos a atender.
"""
