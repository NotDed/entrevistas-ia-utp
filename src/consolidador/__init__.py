"""
Módulo consolidador para generar reportes institucionales
a partir de múltiples entrevistas.

Incluye:
- Agentes especializados por sección (grupos, hardware, software, etc.)
- Integrador que orquesta los agentes
- Clase base para agentes consolidadores
"""
from .agente_consolidador import AgenteConsolidadorInfraestructura
from .base_agent_consolidador import BaseAgentConsolidador
from .integrador_consolidado import IntegradorConsolidado

__all__ = [
    'AgenteConsolidadorInfraestructura',
    'BaseAgentConsolidador', 
    'IntegradorConsolidado',
]
