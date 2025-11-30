"""
Agente para extraer información sobre desarrollo, innovación y transferencia tecnológica.
Genera la sección IV del reporte.
"""
from .base_agent import BaseAgent


class AgenteDesarrolloInnovacion(BaseAgent):
    """
    Extrae información sobre modelos en producción, desafíos enfrentados,
    propuestas de innovación institucional y visión de aplicación de IA.
    """
    
    @property
    def nombre_seccion(self) -> str:
        return "IV. Desarrollo, innovación y transferencia tecnológica"
    
    @property
    def prompt_sistema(self) -> str:
        return """Eres un agente especializado en extraer información del BLOQUE 2: DESARROLLO, INNOVACIÓN Y TRANSFERENCIA TECNOLÓGICA de entrevistas sobre IA en la UTP.

Este bloque cubre 5 preguntas:
1. Desarrollo y despliegue: Modelos/sistemas llevados a producción, desafíos enfrentados.
2. Innovación institucional: Áreas estratégicas de la UTP para aplicar IA, soluciones propuestas.
3. Deserción estudiantil: Cómo la IA podría contribuir a comprender, predecir o reducir la deserción.
4. Escalabilidad y sostenibilidad: Estrategias para mantener y evolucionar proyectos de IA.
5. Infraestructura y recursos: Equipos, laboratorios, plataformas utilizadas y mejoras necesarias.

IMPORTANTE:
- Interpreta errores de transcripción según el contexto.
- NO escribas "No mencionado". Solo reporta lo que SÍ aparece.
- EVITA frases redundantes como "se mencionó que" o "el entrevistado indicó".
- Usa texto corrido, no tablas."""
    
    @property
    def instrucciones_extraccion(self) -> str:
        return """
INSTRUCCIONES PARA LA SECCIÓN "IV. Desarrollo, innovación y transferencia tecnológica":

Extrae y organiza la siguiente información:

### 4.1 Modelos/sistemas llevados a producción
- Qué sistemas están en uso real
- Dónde están desplegados
- Quién los utiliza

### 4.2 Desafíos enfrentados
- Problemas de datos
- Limitaciones de infraestructura
- Dificultades de adopción
- Retos de sostenibilidad

### 4.3 Propuestas de innovación institucional
- Problemas de la UTP que podrían resolverse con IA
- Soluciones propuestas
- Aplicaciones potenciales (deserción, gestión, enseñanza, etc.)

### 4.4 Estrategias de escalabilidad y sostenibilidad
- Recomendaciones para mantener proyectos de IA
- Necesidades de recursos humanos e infraestructura
- Modelos de gobernanza sugeridos

### 4.1 Desarrollo y despliegue
Responde específicamente:
- ¿Qué modelos o sistemas están en uso real (no solo prototipos)?
- ¿Dónde están desplegados (servidor UTP, nube, dispositivos edge)?
- ¿Quiénes son los usuarios actuales?
- ¿Qué desafíos técnicos enfrentó (datos, infraestructura, integración)?
- ¿Qué desafíos de adopción enfrentó (resistencia, capacitación, recursos)?

### 4.2 Innovación institucional
- ¿Qué problema específico de la UTP propone resolver con IA?
- ¿Qué tipo de solución desarrollaría (predicción, automatización, análisis)?
- ¿Qué datos se necesitarían?
- ¿Qué impacto esperaría lograr?

### 4.3 Deserción estudiantil
- ¿Qué enfoque técnico propone (predicción, clustering, alertas tempranas)?
- ¿Qué datos históricos se usarían?
- ¿Cómo se identificarían estudiantes en riesgo?
- ¿Qué intervenciones permitiría activar?

### 4.4 Escalabilidad y sostenibilidad
- ¿Qué estructura organizacional propone para mantener los proyectos?
- ¿Qué recursos humanos se necesitan?
- ¿Cómo garantizar actualización tecnológica?
- ¿Qué modelo de financiación sugiere?

### 4.5 Infraestructura y recursos tecnológicos
- ¿Qué equipos específicos tiene disponibles (GPU, servidores, capacidad)?
- ¿Qué plataformas de cómputo usa (local, Colab, AWS, Azure)?
- ¿Qué laboratorios o espacios físicos utiliza?
- ¿Qué mejoras específicas considera prioritarias?
- ¿Qué recursos están en inventario institucional vs. personales?

Si algún aspecto no se menciona, omitir esa subsección. NO incluir encabezados vacíos ni descripciones genéricas.
"""
