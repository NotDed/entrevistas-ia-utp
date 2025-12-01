"""
Agentes especializados para el consolidador de infraestructura IA.
"""
from .agente_grupos_labs import AgenteGruposLabs
from .agente_hardware import AgenteHardware
from .agente_software import AgenteSoftware
from .agente_fortalezas import AgenteFortalezas
from .agente_limitaciones import AgenteLimitaciones
from .agente_oportunidades import AgenteOportunidades
from .agente_propuestas import AgentePropuestas
from .agente_conclusiones import AgenteConclusiones

__all__ = [
    "AgenteGruposLabs",
    "AgenteHardware",
    "AgenteSoftware",
    "AgenteFortalezas",
    "AgenteLimitaciones",
    "AgenteOportunidades",
    "AgentePropuestas",
    "AgenteConclusiones",
]
