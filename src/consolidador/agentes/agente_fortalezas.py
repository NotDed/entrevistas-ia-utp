"""
Agente especializado en identificar fortalezas institucionales.
"""
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from consolidador.base_agent_consolidador import BaseAgentConsolidador


class AgenteFortalezas(BaseAgentConsolidador):
    """
    Extrae y sintetiza las fortalezas, capacidades destacadas y 
    ventajas competitivas en IA identificadas en la UTP.
    """
    
    @property
    def nombre_seccion(self) -> str:
        return "IV. Fortalezas y Capacidades Destacadas"
    
    @property
    def prompt_sistema(self) -> str:
        return """Eres un consultor estratégico especializado en análisis de capacidades institucionales.
Tu tarea es identificar y sintetizar las FORTALEZAS de la Universidad Tecnológica de Pereira
en el área de Inteligencia Artificial.

Busca identificar:
- Experticia técnica y conocimiento especializado
- Recursos humanos calificados
- Proyectos exitosos y casos de éxito
- Infraestructura disponible
- Colaboraciones establecidas
- Experiencia acumulada
- Ventajas competitivas únicas
- Capacidades que diferencian a la institución"""
    
    @property
    def instrucciones_extraccion(self) -> str:
        return """
INSTRUCCIONES PARA LA SECCIÓN "IV. Fortalezas y Capacidades Destacadas":

Organiza la información en las siguientes subsecciones:

### 4.1 Capital Humano
- Experiencia y formación del personal investigador
- Diversidad de perfiles y especialidades
- Trayectoria en proyectos de IA
- Capacidad de formación de nuevos talentos

### 4.2 Experiencia Técnica Acumulada
- Áreas de especialización consolidadas
- Metodologías y técnicas dominadas
- Proyectos emblemáticos desarrollados
- Conocimiento transferible

### 4.3 Infraestructura y Recursos
- Fortalezas en equipamiento disponible
- Acceso a datos y recursos
- Espacios de trabajo adecuados

### 4.4 Red de Colaboraciones
- Alianzas con otras instituciones
- Vínculos con el sector productivo
- Participación en redes de investigación
- Colaboraciones internacionales

### 4.5 Casos de Éxito
- Proyectos con resultados destacados
- Aplicaciones implementadas
- Reconocimientos y publicaciones
- Impacto demostrable

### 4.6 Ventajas Competitivas
- Elementos diferenciadores de la UTP
- Nichos de especialización únicos
- Oportunidades aprovechadas

FORMATO: Presenta las fortalezas de manera positiva pero objetiva, basándote solo en lo mencionado.
Prioriza las fortalezas más significativas y recurrentes.
"""
