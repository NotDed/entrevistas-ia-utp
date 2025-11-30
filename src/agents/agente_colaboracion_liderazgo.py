"""
Agente para extraer información sobre colaboración, liderazgo y visión estratégica.
Genera la sección V del reporte.
"""
from .base_agent import BaseAgent


class AgenteColaboracionLiderazgo(BaseAgent):
    """
    Extrae información sobre sinergias, competencias de liderazgo,
    y visión estratégica para la IA en la universidad.
    """
    
    @property
    def nombre_seccion(self) -> str:
        return "V. Colaboración, liderazgo y visión estratégica"
    
    @property
    def prompt_sistema(self) -> str:
        return """Eres un agente especializado en extraer información del BLOQUE 3: COLABORACIÓN, LIDERAZGO Y VISIÓN ESTRATÉGICA de entrevistas sobre IA en la UTP.

Este bloque cubre 3 preguntas:
1. Trabajo colaborativo: Aprendizajes y sinergias con otros grupos, facultades o instituciones.
2. Liderazgo técnico: Competencias humanas y técnicas para liderar grupos de IA.
3. Visión estratégica: Papel de la IA en la transformación de la UTP en los próximos 5 años.

IMPORTANTE:
- Interpreta errores de transcripción según el contexto.
- NO escribas "No mencionado". Solo reporta lo que SÍ aparece.
- EVITA frases como "el entrevistado considera" o "se identificaron". Ve directo al contenido.
- Usa texto corrido, no listas extensas."""
    
    @property
    def instrucciones_extraccion(self) -> str:
        return """
INSTRUCCIONES PARA LA SECCIÓN "V. Colaboración, liderazgo y visión estratégica":

Extrae y organiza la siguiente información:

### 5.1 Aprendizajes y sinergias identificadas
- Colaboraciones exitosas
- Beneficios de trabajar con otros grupos/instituciones
- Modelos de colaboración recomendados

### 5.2 Competencias para liderar equipos de IA
- Habilidades técnicas mencionadas
- Habilidades blandas/interpersonales
- Capacidades de gestión de proyectos

### 5.3 Visión estratégica para la IA en la UTP
- Rol que debería tener la IA en los próximos años
- Áreas prioritarias de desarrollo
- Posicionamiento institucional deseado

### 5.1 Trabajo colaborativo
Responde específicamente:
- ¿Con qué grupos, facultades o instituciones externas ha colaborado?
- ¿Qué proyecto concreto desarrollaron juntos?
- ¿Qué aprendizajes obtuvo de esa colaboración?
- ¿Qué modelo de colaboración funcionó mejor (convenios, proyectos conjuntos, redes)?
- ¿Qué barreras encontró para colaborar?

### 5.2 Liderazgo técnico
- ¿Qué competencias técnicas considera esenciales para liderar en IA?
- ¿Qué competencias humanas/blandas son necesarias?
- ¿Cómo transfiere conocimiento a su equipo (mentoría, documentación, talleres)?
- ¿Cómo maneja la rotación de estudiantes y la pérdida de conocimiento?
- ¿Cuántas personas ha formado en IA?

### 5.3 Visión estratégica
- ¿Qué papel específico debería jugar la IA en la UTP en 5 años?
- ¿En qué áreas concretas (docencia, investigación, gestión, extensión)?
- ¿Qué rol le gustaría cumplir personalmente en esa transformación?
- ¿Qué cambios institucionales serían necesarios?

Si algún aspecto no se menciona, omitir esa subsección. NO incluir encabezados vacíos.
"""
