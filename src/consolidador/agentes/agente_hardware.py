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
        return """Eres un especialista en infraestructura tecnológica y recursos computacionales.
Tu tarea es realizar un inventario exhaustivo del hardware disponible para proyectos de 
Inteligencia Artificial en la Universidad Tecnológica de Pereira.

Debes identificar:
- Equipos de cómputo de alto rendimiento
- Servidores locales y su capacidad
- Tarjetas gráficas (GPUs) para entrenamiento de modelos
- Clusters de computación
- Recursos en la nube utilizados
- Estado y antigüedad del equipamiento"""
    
    @property
    def instrucciones_extraccion(self) -> str:
        return """
INSTRUCCIONES PARA LA SECCIÓN "II. Inventario de Hardware e Infraestructura Computacional":

Organiza la información en las siguientes subsecciones:

### 2.1 Equipos de Alto Rendimiento
- Workstations y equipos especializados
- Especificaciones técnicas mencionadas (RAM, procesadores, almacenamiento)
- Ubicación y grupo que los administra

### 2.2 Servidores y Clusters
- Servidores dedicados a IA/ML
- Capacidad de procesamiento
- Sistemas operativos y configuraciones
- Accesibilidad (local, remoto)

### 2.3 GPUs y Aceleradores
- Modelos de tarjetas gráficas identificadas (NVIDIA, AMD, etc.)
- Cantidad y distribución por grupo
- Capacidad de memoria VRAM
- Uso principal (entrenamiento, inferencia)

### 2.4 Recursos en la Nube
- Plataformas cloud utilizadas (AWS, Google Cloud, Azure, Colab)
- Tipo de uso (ocasional, frecuente, institucional)
- Limitaciones de acceso o presupuesto

### 2.5 Estado General de la Infraestructura
- Antigüedad del equipamiento
- Necesidades de actualización identificadas
- Cuellos de botella en capacidad

FORMATO: Presenta la información de manera consolidada, agrupando recursos similares.
Incluye especificaciones técnicas cuando estén disponibles.
"""
