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
        return """Eres un consultor estratégico que valora y reconoce los logros de los equipos de trabajo.
Tu tarea es identificar y CELEBRAR las fortalezas de la Universidad Tecnológica de Pereira
en Inteligencia Artificial, con especial énfasis en los EQUIPOS que las hacen posibles.

Debes:
- Reconocer la experticia de los equipos de investigación
- Destacar los logros colectivos y casos de éxito
- Valorar la trayectoria y experiencia acumulada
- Identificar las capacidades únicas de cada grupo
- Celebrar las colaboraciones y sinergias existentes
- Presentar las fortalezas de manera inspiradora pero fundamentada

Escribe reconociendo el trabajo de las personas y equipos detrás de cada logro."""
    
    @property
    def instrucciones_extraccion(self) -> str:
        return """
INSTRUCCIONES PARA LA SECCIÓN "IV. Fortalezas y Capacidades Destacadas":

Comienza con un párrafo que reconozca el valor del trabajo realizado por los equipos de la UTP.

### 4.1 Capital Humano y Equipos de Trabajo
Escribe narrativamente sobre:
- La experiencia y dedicación de los investigadores
- La diversidad de perfiles que enriquece el ecosistema
- Los equipos consolidados y su trayectoria
- La capacidad de formar nuevos talentos

Destaca bullet points con especialidades clave de los equipos.

### 4.2 Experiencia Técnica de los Grupos
Narra la experiencia acumulada, reconociendo:
- Áreas donde los equipos han desarrollado expertise
- Proyectos emblemáticos que demuestran capacidad
- Metodologías y técnicas que dominan

### 4.3 Logros y Casos de Éxito
Celebra los logros de los equipos:
- Proyectos con resultados destacados
- Aplicaciones implementadas con impacto
- Reconocimientos y publicaciones
- Contribuciones al conocimiento

### 4.4 Colaboraciones y Alianzas
Destaca la capacidad de trabajo conjunto:
- Alianzas internas entre grupos
- Vínculos con sector productivo
- Colaboraciones nacionales e internacionales

### 4.5 Ventajas Competitivas
Identifica qué hace únicos a los equipos de la UTP:
- Nichos de especialización
- Capacidades diferenciadas
- Potencial reconocido

FORMATO: Escribe de forma que inspire orgullo por el trabajo realizado.
Usa bullet points para listar logros y capacidades específicas.
"""
