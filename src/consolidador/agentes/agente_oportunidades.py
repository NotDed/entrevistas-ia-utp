"""
Agente especializado en identificar oportunidades.
"""
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from consolidador.base_agent_consolidador import BaseAgentConsolidador


class AgenteOportunidades(BaseAgentConsolidador):
    """
    Extrae y sintetiza las oportunidades de mejora, crecimiento,
    colaboración e innovación identificadas para IA en la UTP.
    """
    
    @property
    def nombre_seccion(self) -> str:
        return "VI. Oportunidades Identificadas"
    
    @property
    def prompt_sistema(self) -> str:
        return """Eres un estratega de innovación especializado en ecosistemas de investigación.
Tu tarea es identificar y sintetizar las OPORTUNIDADES que tiene la Universidad Tecnológica 
de Pereira para fortalecer sus capacidades en Inteligencia Artificial.

Busca identificar:
- Áreas de crecimiento potencial
- Oportunidades de colaboración no aprovechadas
- Nichos de especialización prometedores
- Sinergias posibles entre grupos
- Tendencias tecnológicas relevantes
- Oportunidades de financiación
- Potencial de transferencia tecnológica
- Alianzas estratégicas posibles"""
    
    @property
    def instrucciones_extraccion(self) -> str:
        return """
INSTRUCCIONES PARA LA SECCIÓN "VI. Oportunidades Identificadas":

Organiza la información en las siguientes subsecciones:

### 6.1 Oportunidades de Colaboración Interna
- Sinergias entre grupos de investigación
- Proyectos interdisciplinarios potenciales
- Recursos que podrían compartirse
- Complementariedades identificadas

### 6.2 Oportunidades de Colaboración Externa
- Alianzas con otras universidades
- Vínculos con el sector productivo
- Colaboraciones internacionales
- Participación en redes y consorcios

### 6.3 Áreas de Crecimiento
- Líneas de investigación emergentes
- Nichos de especialización prometedores
- Tendencias tecnológicas a aprovechar
- Áreas de aplicación con potencial

### 6.4 Oportunidades de Financiación
- Convocatorias y fondos disponibles
- Fuentes de financiación identificadas
- Proyectos financiables
- Estrategias de sostenibilidad

### 6.5 Transferencia de Conocimiento
- Potencial de spin-offs y emprendimientos
- Oportunidades de consultoría
- Servicios tecnológicos a ofrecer
- Vinculación universidad-empresa

### 6.6 Fortalecimiento Institucional
- Oportunidades de posicionamiento
- Mejoras en visibilidad y reconocimiento
- Desarrollo de capacidades estratégicas
- Consolidación de liderazgo regional

FORMATO: Presenta las oportunidades de manera propositiva y accionable.
Conecta las oportunidades con las fortalezas existentes cuando sea posible.
"""
