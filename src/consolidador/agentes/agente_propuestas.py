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
        return """Eres un consultor senior que genera propuestas accionables,
reconociendo el contexto y capacidades de los equipos existentes.

Tu tarea es generar recomendaciones concretas para fortalecer las capacidades de IA en la UTP,
basándote en las fortalezas de los equipos y los desafíos identificados.

Debes:
- Proponer acciones que aprovechen el talento existente
- Generar recomendaciones específicas y factibles
- Priorizar por impacto y viabilidad
- Reconocer lo que ya funciona bien
- Conectar propuestas con las capacidades de los equipos

Escribe de forma propositiva, con propuestas que motiven a la acción."""
    
    @property
    def instrucciones_extraccion(self) -> str:
        return """
INSTRUCCIONES PARA LA SECCIÓN "VII. Propuestas y Recomendaciones":

Comienza con un párrafo que conecte las propuestas con las fortalezas de los equipos
y el potencial identificado, generando motivación para la acción.

### 7.1 Acciones Inmediatas (0-6 meses)
Propón quick wins que aprovechen capacidades existentes:
- Acciones de bajo costo y alto impacto
- Mejoras operativas inmediatas
- Articulaciones básicas entre equipos
- Optimización de recursos existentes

Usa bullet points para listar acciones específicas con responsables sugeridos.

### 7.2 Iniciativas de Mediano Plazo (6-18 meses)
Describe proyectos que requieren planificación:
- Adquisición de equipamiento prioritario
- Programas de capacitación y formación
- Desarrollo de alianzas estratégicas
- Proyectos piloto colaborativos

### 7.3 Transformaciones Estratégicas (18+ meses)
Narra visiones de largo plazo:
- Creación de espacios o unidades especializadas
- Inversiones mayores en infraestructura
- Posicionamiento institucional en IA
- Desarrollo de programas académicos

### 7.4 Recomendaciones de Infraestructura
Propón mejoras específicas en recursos:
- Equipos y tecnologías prioritarias a adquirir
- Arquitectura tecnológica recomendada
- Estrategia de actualización y renovación

### 7.5 Recomendaciones de Articulación y Gobernanza
Sugiere mejoras organizacionales:
- Mecanismos de coordinación entre equipos
- Espacios de encuentro y colaboración
- Modelo de gestión de recursos compartidos

### 7.6 Recomendaciones de Sostenibilidad
Propón estrategias de financiación:
- Fuentes de recursos a explorar
- Modelos de sostenibilidad
- Priorización de inversiones

FORMATO: Cada propuesta debe ser específica e indicar el impacto esperado.
Conecta las recomendaciones con las capacidades de los equipos.
"""
