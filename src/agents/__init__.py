# Agentes del sistema multi-agente
from .base_agent import BaseAgent
from .agente_correccion import AgenteCorreccion
from .agente_datos_basicos import AgenteDatosBasicos
from .agente_resumen_general import AgenteResumenGeneral
from .agente_experiencia_tecnica import AgenteExperienciaTecnica
from .agente_desarrollo_innovacion import AgenteDesarrolloInnovacion
from .agente_colaboracion_liderazgo import AgenteColaboracionLiderazgo
from .agente_motivacion_proyeccion import AgenteMotivacionProyeccion
from .agente_hallazgos_clave import AgenteHallazgosClave
from .agente_narrativo import AgenteNarrativo
from .agente_integrador import AgenteIntegrador

__all__ = [
    'BaseAgent',
    'AgenteCorreccion',
    'AgenteDatosBasicos',
    'AgenteResumenGeneral',
    'AgenteExperienciaTecnica',
    'AgenteDesarrolloInnovacion',
    'AgenteColaboracionLiderazgo',
    'AgenteMotivacionProyeccion',
    'AgenteHallazgosClave',
    'AgenteNarrativo',
    'AgenteIntegrador',
]
