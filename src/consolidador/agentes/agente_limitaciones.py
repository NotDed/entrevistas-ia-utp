"""
Agente especializado en identificar limitaciones y desafíos.
"""
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from consolidador.base_agent_consolidador import BaseAgentConsolidador


class AgenteLimitaciones(BaseAgentConsolidador):
    """
    Extrae y sintetiza las limitaciones, desafíos, brechas y 
    obstáculos identificados para el desarrollo de IA en la UTP.
    """
    
    @property
    def nombre_seccion(self) -> str:
        return "V. Limitaciones y Desafíos Identificados"
    
    @property
    def prompt_sistema(self) -> str:
        return """Eres un consultor estratégico especializado en diagnóstico organizacional.
Tu tarea es identificar y sintetizar las LIMITACIONES, DESAFÍOS y BRECHAS que enfrenta
la Universidad Tecnológica de Pereira en el área de Inteligencia Artificial.

Busca identificar:
- Carencias de infraestructura
- Limitaciones de recursos humanos
- Brechas tecnológicas
- Obstáculos administrativos o institucionales
- Falta de recursos financieros
- Desafíos de coordinación
- Barreras para la investigación
- Problemas recurrentes mencionados"""
    
    @property
    def instrucciones_extraccion(self) -> str:
        return """
INSTRUCCIONES PARA LA SECCIÓN "V. Limitaciones y Desafíos Identificados":

Organiza la información en las siguientes subsecciones:

### 5.1 Limitaciones de Infraestructura
- Carencias en hardware y equipamiento
- Problemas de capacidad computacional
- Falta de recursos específicos (GPUs, servidores, etc.)
- Obsolescencia tecnológica

### 5.2 Brechas en Recursos Humanos
- Falta de personal especializado
- Carga laboral excesiva
- Necesidades de capacitación
- Dificultad para retener talento

### 5.3 Restricciones Financieras
- Limitaciones presupuestales
- Dificultad para adquirir recursos
- Dependencia de financiación externa
- Costos de licencias y servicios

### 5.4 Desafíos Institucionales
- Barreras administrativas
- Procesos burocráticos
- Falta de políticas claras en IA
- Desarticulación entre dependencias

### 5.5 Barreras Técnicas
- Limitaciones en acceso a datos
- Problemas de integración tecnológica
- Falta de estándares comunes
- Deuda técnica acumulada

### 5.6 Desafíos de Colaboración
- Trabajo aislado entre grupos
- Dificultad para compartir recursos
- Falta de espacios de articulación
- Competencia por recursos escasos

FORMATO: Presenta las limitaciones de manera objetiva y constructiva.
Agrupa problemas similares y destaca los más recurrentes o críticos.
"""
