"""
Agente especializado en identificar grupos y laboratorios de IA.
"""
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from consolidador.base_agent_consolidador import BaseAgentConsolidador


class AgenteGruposLabs(BaseAgentConsolidador):
    """
    Extrae información sobre grupos de investigación, laboratorios,
    facultades y líneas de trabajo relacionadas con IA en la UTP.
    """
    
    @property
    def nombre_seccion(self) -> str:
        return "I. Grupos de Investigación y Laboratorios"
    
    @property
    def prompt_sistema(self) -> str:
        return """Eres un analista experto en mapeo de capacidades de investigación universitaria.
Tu tarea es identificar y catalogar TODOS los grupos de investigación, laboratorios y 
unidades académicas que trabajan con Inteligencia Artificial en la Universidad Tecnológica de Pereira.

Debes extraer información estructurada sobre:
- Nombres oficiales de grupos de investigación
- Facultades o dependencias a las que pertenecen
- Líneas de investigación relacionadas con IA
- Áreas de aplicación (salud, energía, industria, etc.)
- Colaboraciones entre grupos mencionadas"""
    
    @property
    def instrucciones_extraccion(self) -> str:
        return """
INSTRUCCIONES PARA LA SECCIÓN "I. Grupos de Investigación y Laboratorios":

Organiza la información en las siguientes subsecciones:

### 1.1 Grupos de Investigación Identificados
Para cada grupo mencionado, incluye:
- Nombre del grupo
- Facultad o dependencia
- Líneas de investigación en IA
- Áreas de aplicación

### 1.2 Laboratorios y Espacios de Trabajo
- Laboratorios especializados mencionados
- Infraestructura física disponible
- Recursos compartidos entre grupos

### 1.3 Articulación Académica
- Programas académicos relacionados (pregrado, maestría, doctorado)
- Semilleros de investigación
- Conexiones entre docencia e investigación

### 1.4 Redes de Colaboración Interna
- Colaboraciones entre grupos de la UTP
- Proyectos interdisciplinarios
- Sinergias identificadas

FORMATO: Usa encabezados ### para subsecciones y #### para grupos específicos.
Agrupa la información de manera coherente, no la presentes por entrevistado.
"""
