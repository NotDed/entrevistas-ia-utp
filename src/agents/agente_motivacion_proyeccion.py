"""
Agente para extraer información sobre motivación y proyección profesional.
Genera la sección VI del reporte.
"""
from .base_agent import BaseAgent


class AgenteMotivacionProyeccion(BaseAgent):
    """
    Extrae información sobre motivaciones personales, expectativas 
    de apoyo institucional y proyección profesional.
    """
    
    @property
    def nombre_seccion(self) -> str:
        return "VI. Motivación y proyección profesional"
    
    @property
    def prompt_sistema(self) -> str:
        return """Eres un agente especializado en extraer información del BLOQUE 4: MOTIVACIÓN Y PROYECCIÓN PROFESIONAL de entrevistas sobre IA en la UTP.

Este bloque cubre 1 pregunta principal:
- Motivación y propósito: Qué impulsa a continuar en IA y cómo espera que la UTP acompañe su crecimiento.

IMPORTANTE:
- Interpreta errores de transcripción según el contexto.
- NO escribas "No mencionado". Solo reporta lo que SÍ aparece.
- EVITA frases redundantes. Ve directo a las motivaciones y expectativas concretas.
- Usa texto corrido."""
    
    @property
    def instrucciones_extraccion(self) -> str:
        return """
INSTRUCCIONES PARA LA SECCIÓN "VI. Motivación y proyección profesional":

Extrae y organiza la siguiente información:

### 6.1 Motivaciones personales
- Qué impulsa al entrevistado a trabajar en IA
- Valores o propósitos mencionados
- Intereses de investigación/desarrollo

### 6.2 Expectativas de apoyo institucional
- Recursos que necesita (infraestructura, personal, etc.)
- Tipo de apoyo esperado de la universidad
- Barreras que enfrenta actualmente

### 6.3 Proyección profesional
- Cómo espera desarrollarse en el área
- Rol que desea desempeñar en el futuro
- Metas profesionales mencionadas

### 6.1 Motivación y propósito
Responde específicamente:
- ¿Qué lo motivó inicialmente a trabajar en IA?
- ¿Qué lo mantiene activo en este campo?
- ¿Qué tipo de problemas le apasiona resolver?
- ¿Qué logro en IA le gustaría alcanzar?

### 6.2 Expectativas de acompañamiento institucional
- ¿Qué recursos específicos necesita de la UTP (equipos, tiempo, financiación)?
- ¿Qué tipo de reconocimiento o apoyo espera?
- ¿Qué barreras institucionales enfrenta actualmente?
- ¿Qué condiciones necesita para consolidarse como referente?
- ¿Qué oportunidades de formación o actualización requiere?

Si algún aspecto no se menciona, omitir esa subsección. NO incluir encabezados vacíos.
"""
