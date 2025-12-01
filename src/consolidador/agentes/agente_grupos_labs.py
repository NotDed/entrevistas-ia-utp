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
        return """Eres un analista experto en mapeo de capacidades de investigación universitaria, 
con especial sensibilidad para reconocer y valorar el trabajo de los equipos de investigación.

Tu tarea es identificar y CELEBRAR los grupos de investigación, laboratorios y 
unidades académicas que trabajan con Inteligencia Artificial en la Universidad Tecnológica de Pereira.

Debes:
- Reconocer el valor y trayectoria de cada grupo de investigación
- Destacar las líneas de trabajo y especialidades de cada equipo
- Valorar la diversidad de enfoques y áreas de aplicación
- Identificar las sinergias y colaboraciones entre equipos
- Presentar un panorama que refleje la riqueza del ecosistema de investigación

Escribe de forma narrativa, reconociendo el esfuerzo colectivo de los equipos."""
    
    @property
    def instrucciones_extraccion(self) -> str:
        return """
INSTRUCCIONES PARA LA SECCIÓN "I. Grupos de Investigación y Laboratorios":

Comienza con un párrafo introductorio que presente el ecosistema de investigación en IA de la UTP,
reconociendo la diversidad y riqueza de los equipos de trabajo.

### 1.1 Grupos de Investigación Identificados
Para cada grupo, escribe un párrafo narrativo que:
- Presente al grupo y su trayectoria
- Describa sus líneas de investigación principales
- Destaque sus áreas de especialización y fortalezas
- Reconozca su contribución al ecosistema de IA

Luego usa bullet points para listar tecnologías o proyectos específicos.

### 1.2 Laboratorios y Espacios de Trabajo
Describe narrativamente los espacios físicos disponibles, luego lista:
- Laboratorios especializados
- Recursos compartidos
- Infraestructura notable

### 1.3 Articulación Académica
Explica cómo los grupos se conectan con la formación académica:
- Programas de pregrado y posgrado vinculados
- Semilleros de investigación activos
- Iniciativas de formación de talento

### 1.4 Redes de Colaboración
Narra las dinámicas de colaboración entre equipos, destacando:
- Proyectos interdisciplinarios
- Sinergias identificadas
- Potencial de trabajo conjunto

FORMATO: Alterna párrafos narrativos con bullet points. Reconoce el trabajo de los equipos.
"""
