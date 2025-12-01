"""
Agente especializado en generar propuestas y recomendaciones.
"""
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from consolidador.base_agent_consolidador import BaseAgentConsolidador


class AgentePropuestas(BaseAgentConsolidador):
    """
    Genera propuestas concretas y recomendaciones priorizadas
    para fortalecer las capacidades de IA en la UTP.
    """
    
    # Más tokens para propuestas detalladas
    max_tokens = 5000
    
    @property
    def nombre_seccion(self) -> str:
        return "VII. Propuestas y Recomendaciones"
    
    @property
    def prompt_sistema(self) -> str:
        return """Eres un consultor senior especializado en estrategia de innovación tecnológica.
Tu tarea es generar PROPUESTAS CONCRETAS y RECOMENDACIONES PRIORIZADAS para fortalecer
las capacidades de Inteligencia Artificial en la Universidad Tecnológica de Pereira.

Las propuestas deben ser:
- Específicas y accionables
- Basadas en las necesidades expresadas
- Priorizadas por impacto y factibilidad
- Alineadas con las fortalezas existentes
- Orientadas a resolver las limitaciones identificadas

Considera propuestas para:
- Infraestructura y equipamiento
- Recursos humanos y capacitación
- Organización y gobernanza
- Colaboración y articulación
- Financiación y sostenibilidad"""
    
    @property
    def instrucciones_extraccion(self) -> str:
        return """
INSTRUCCIONES PARA LA SECCIÓN "VII. Propuestas y Recomendaciones":

Organiza la información en las siguientes subsecciones:

### 7.1 Propuestas de Corto Plazo (0-6 meses)
Acciones inmediatas de bajo costo y alto impacto:
- Quick wins que pueden implementarse rápidamente
- Mejoras operativas inmediatas
- Articulaciones básicas entre grupos
- Optimización de recursos existentes

### 7.2 Propuestas de Mediano Plazo (6-18 meses)
Iniciativas que requieren planificación y recursos moderados:
- Adquisición de equipamiento prioritario
- Programas de capacitación estructurados
- Establecimiento de alianzas estratégicas
- Desarrollo de proyectos piloto

### 7.3 Propuestas de Largo Plazo (18+ meses)
Transformaciones estructurales y estratégicas:
- Creación de centros o unidades especializadas
- Inversiones mayores en infraestructura
- Desarrollo de programas académicos
- Posicionamiento regional/nacional

### 7.4 Recomendaciones de Infraestructura
- Equipos y recursos específicos a adquirir
- Arquitectura tecnológica recomendada
- Estrategia de actualización de equipos
- Soluciones cloud vs on-premise

### 7.5 Recomendaciones de Gobernanza
- Estructura organizacional sugerida
- Mecanismos de coordinación entre grupos
- Políticas institucionales necesarias
- Modelo de gestión de recursos compartidos

### 7.6 Recomendaciones de Financiación
- Fuentes de financiación a explorar
- Estrategias de captación de recursos
- Modelos de sostenibilidad
- Priorización de inversiones

FORMATO: Cada propuesta debe ser específica, indicando qué hacer, para qué y cómo.
Usa viñetas claras y prioriza las recomendaciones más importantes.
"""
