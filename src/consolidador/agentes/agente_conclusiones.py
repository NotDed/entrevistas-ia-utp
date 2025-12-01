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
        return """Eres un director de investigación con amplia experiencia en planeación estratégica.
Tu tarea es generar las CONCLUSIONES FINALES y una SÍNTESIS EJECUTIVA del análisis
de capacidades de Inteligencia Artificial en la Universidad Tecnológica de Pereira.

Las conclusiones deben:
- Sintetizar los hallazgos más importantes
- Destacar el estado actual de las capacidades
- Identificar los factores críticos de éxito
- Proporcionar una visión clara del camino a seguir
- Ser útiles para tomadores de decisiones

El tono debe ser:
- Estratégico y visionario
- Objetivo pero propositivo
- Orientado a la acción
- Adecuado para presentar a directivos"""
    
    @property
    def instrucciones_extraccion(self) -> str:
        return """
INSTRUCCIONES PARA LA SECCIÓN "VIII. Conclusiones y Síntesis Ejecutiva":

Organiza la información en las siguientes subsecciones:

### 8.1 Diagnóstico General
Síntesis del estado actual de las capacidades de IA en la UTP:
- Nivel de madurez institucional en IA
- Principales activos y recursos disponibles
- Brechas críticas identificadas
- Posicionamiento relativo

### 8.2 Hallazgos Clave
Los 5-7 hallazgos más importantes del análisis:
- Descubrimientos que requieren atención
- Patrones identificados en las entrevistas
- Insights estratégicos relevantes

### 8.3 Factores Críticos de Éxito
Elementos esenciales para el desarrollo de IA en la UTP:
- Condiciones necesarias para avanzar
- Recursos críticos a asegurar
- Capacidades a desarrollar prioritariamente

### 8.4 Riesgos y Alertas
Situaciones que podrían comprometer el avance:
- Riesgos identificados
- Señales de alerta
- Escenarios a evitar

### 8.5 Visión de Futuro
Hacia dónde debe orientarse la UTP en IA:
- Estado deseado a mediano/largo plazo
- Rol que puede jugar la universidad
- Aspiraciones realistas

### 8.6 Llamado a la Acción
Mensaje final para tomadores de decisiones:
- Urgencia de actuar
- Primeros pasos recomendados
- Compromiso institucional requerido

FORMATO: Esta sección debe ser inspiradora pero realista.
Usa un lenguaje ejecutivo apropiado para directivos universitarios.
"""
