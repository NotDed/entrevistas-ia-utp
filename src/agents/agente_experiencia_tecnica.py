"""
Agente para extraer experiencia técnica y práctica aplicada.
Genera la sección III del reporte.
"""
from .base_agent import BaseAgent


class AgenteExperienciaTecnica(BaseAgent):
    """
    Extrae información sobre proyectos de IA, herramientas utilizadas,
    arquitecturas y metodologías aplicadas.
    """
    
    @property
    def nombre_seccion(self) -> str:
        return "III. Experiencia técnica y práctica aplicada"
    
    @property
    def prompt_sistema(self) -> str:
        return """Eres un agente especializado en extraer información del BLOQUE 1: EXPERIENCIA TÉCNICA Y PRÁCTICA APLICADA de entrevistas sobre IA en la UTP.

Este bloque cubre 4 preguntas:
1. Experiencia más relevante: Proyecto más representativo, rol específico y resultados concretos.
2. Articulación con grupos de investigación: Colaboración con grupos UTP, aportes al ecosistema de IA.
3. Diseño y herramientas: Arquitecturas, metodologías, frameworks utilizados.
4. Integración institucional: Cómo se integran los resultados con procesos institucionales.

IMPORTANTE: 
- Corrige errores de transcripción ("tensor flau" = TensorFlow, "quedas" = Keras).
- NO incluyas "No mencionado". Solo reporta lo que SÍ aparece.
- EVITA frases redundantes. Ve directo a los hechos.
- Usa texto corrido, no tablas."""
    
    @property
    def instrucciones_extraccion(self) -> str:
        return """
INSTRUCCIONES PARA LA SECCIÓN "III. Experiencia técnica y práctica aplicada":

### 3.1 Experiencia más relevante
Responde específicamente:
- ¿Cuál es el nombre o descripción del proyecto?
- ¿Qué problema resuelve y para quién?
- ¿Cuál fue el rol específico (desarrollador, líder, investigador)?
- ¿Qué resultados cuantificables o tangibles se lograron?
- ¿En qué estado está el proyecto (prototipo, piloto, producción)?

### 3.2 Articulación con grupos de investigación
- ¿Con qué grupos específicos de la UTP ha colaborado?
- ¿Qué rol jugó cada grupo en el proyecto?
- ¿Qué recursos o conocimientos aportaron?
- ¿Hay estudiantes o egresados involucrados? ¿En qué roles?

### 3.3 Diseño y herramientas
- ¿Qué lenguajes de programación usa?
- ¿Qué frameworks específicos (TensorFlow, PyTorch, Keras, scikit-learn)?
- ¿Qué arquitecturas de modelos (CNN, RNN, Transformers, etc.)?
- ¿Por qué eligió estas herramientas sobre otras alternativas?
- ¿Qué entornos de desarrollo usa (Colab, servidores locales, nube)?

### 3.4 Integración institucional
- ¿Qué dependencia o proceso institucional usa los resultados?
- ¿Cuántos usuarios o beneficiarios tiene?
- ¿Qué impacto medible ha generado?
- ¿Hay planes de expansión o replicación?

Si algún aspecto no se menciona, omitir esa subsección. NO incluir encabezados vacíos.
"""
