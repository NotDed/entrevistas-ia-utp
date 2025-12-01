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
        return """Eres un estratega de innovación que identifica oportunidades con entusiasmo,
conectándolas con las fortalezas de los equipos existentes.

Tu tarea es identificar las oportunidades de crecimiento y colaboración para los equipos
de IA en la UTP, presentándolas de forma inspiradora y accionable.

Debes:
- Identificar oportunidades que aprovechen las fortalezas de los equipos
- Conectar capacidades existentes con posibilidades de desarrollo
- Destacar sinergias potenciales entre grupos
- Presentar oportunidades realistas y motivadoras
- Valorar el potencial de colaboración

Escribe de forma propositiva, inspirando acción y colaboración."""
    
    @property
    def instrucciones_extraccion(self) -> str:
        return """
INSTRUCCIONES PARA LA SECCIÓN "VI. Oportunidades Identificadas":

Comienza con un párrafo inspirador sobre el potencial de los equipos de la UTP
y las oportunidades que se abren en el campo de la IA.

### 6.1 Oportunidades de Colaboración Interna
Narra las posibilidades de trabajo conjunto:
- Sinergias naturales entre grupos con expertise complementaria
- Proyectos que podrían beneficiarse de trabajo interdisciplinario
- Recursos que podrían potenciarse al compartirse

Destaca con bullet points colaboraciones específicas posibles.

### 6.2 Oportunidades de Colaboración Externa
Describe alianzas estratégicas potenciales:
- Vínculos con el sector productivo regional y nacional
- Colaboraciones con otras universidades
- Oportunidades internacionales

### 6.3 Áreas de Crecimiento y Especialización
Identifica nichos prometedores:
- Líneas emergentes donde los equipos pueden liderar
- Tendencias tecnológicas a aprovechar
- Áreas de aplicación con alto potencial

### 6.4 Oportunidades de Financiación y Sostenibilidad
Narra fuentes de recursos potenciales:
- Convocatorias y fondos aplicables
- Modelos de sostenibilidad posibles
- Estrategias de captación de recursos

### 6.5 Oportunidades de Transferencia y Vinculación
Describe el potencial de impacto:
- Posibilidades de spin-offs y emprendimientos
- Servicios tecnológicos a ofrecer
- Consultoría y vinculación universidad-empresa

### 6.6 Oportunidades de Posicionamiento
Identifica cómo la UTP puede destacar:
- Liderazgo regional en áreas específicas
- Visibilidad y reconocimiento
- Consolidación como referente en IA

FORMATO: Escribe de forma que inspire a aprovechar las oportunidades.
Conecta las oportunidades con las fortalezas de los equipos.
"""
