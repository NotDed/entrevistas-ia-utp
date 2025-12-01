"""
Agente especializado en inventario de hardware e infraestructura.
"""
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from consolidador.base_agent_consolidador import BaseAgentConsolidador


class AgenteHardware(BaseAgentConsolidador):
    """
    Extrae información sobre hardware, equipos de cómputo, servidores,
    GPUs y recursos computacionales disponibles para IA en la UTP.
    """
    
    @property
    def nombre_seccion(self) -> str:
        return "II. Inventario de Hardware e Infraestructura Computacional"
    
    @property
    def prompt_sistema(self) -> str:
        return """Eres un especialista en infraestructura tecnológica con capacidad para reconocer
los esfuerzos de los equipos por construir capacidad computacional.

Tu tarea es documentar el hardware disponible para proyectos de IA en la UTP,
RECONOCIENDO el trabajo de los grupos por adquirir y mantener estos recursos.

Debes:
- Identificar los recursos computacionales de cada grupo
- Reconocer el esfuerzo por construir infraestructura propia
- Documentar capacidades técnicas de manera clara
- Valorar tanto recursos institucionales como de grupos específicos
- Presentar un panorama realista pero que reconozca los logros

Escribe de forma narrativa, valorando el trabajo de construcción de capacidades."""
    
    @property
    def instrucciones_extraccion(self) -> str:
        return """
INSTRUCCIONES PARA LA SECCIÓN "II. Inventario de Hardware e Infraestructura Computacional":

Comienza con un párrafo que contextualice la infraestructura disponible y reconozca
el esfuerzo de los grupos por construir capacidades computacionales.

### 2.1 Equipos de Alto Rendimiento
Narra qué equipos han logrado construir los grupos, incluyendo:
- Workstations y equipos especializados
- Especificaciones técnicas (RAM, procesadores, almacenamiento)
- Cómo estos recursos apoyan la investigación

Lista con bullet points los equipos específicos identificados.

### 2.2 Servidores y Clusters
Describe la infraestructura de servidores disponible:
- Servidores dedicados a IA/ML y su capacidad
- Configuraciones y sistemas operativos
- Accesibilidad (local, remoto)

Reconoce el trabajo de los grupos que han desarrollado esta infraestructura.

### 2.3 GPUs y Capacidad de Procesamiento Paralelo
Detalla las capacidades de procesamiento gráfico:
- Modelos de tarjetas identificadas (NVIDIA, etc.)
- Capacidad de memoria VRAM
- Distribución entre grupos

Usa bullet points para listar GPUs específicas.

### 2.4 Recursos en la Nube
Describe cómo los equipos complementan su infraestructura:
- Plataformas cloud utilizadas (AWS, Google Cloud, Azure, Colab)
- Tipo de uso y frecuencia
- Estrategias de optimización de costos

### 2.5 Valoración General
Concluye con una reflexión sobre:
- El estado actual de la infraestructura
- Los logros alcanzados por los equipos
- Áreas de oportunidad para fortalecer

FORMATO: Combina narrativa que reconozca el trabajo con bullet points técnicos.
"""
