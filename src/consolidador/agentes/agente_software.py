"""
Agente especializado en software, frameworks y herramientas.
"""
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from consolidador.base_agent_consolidador import BaseAgentConsolidador


class AgenteSoftware(BaseAgentConsolidador):
    """
    Extrae información sobre lenguajes de programación, frameworks de ML/IA,
    plataformas y herramientas utilizadas en proyectos de IA en la UTP.
    """
    
    @property
    def nombre_seccion(self) -> str:
        return "III. Ecosistema de Software y Herramientas"
    
    @property
    def prompt_sistema(self) -> str:
        return """Eres un experto en tecnologías de Inteligencia Artificial y Machine Learning,
con capacidad para reconocer las decisiones técnicas de los equipos de trabajo.

Tu tarea es documentar el ecosistema de software utilizado en la UTP,
reconociendo las elecciones tecnológicas que han hecho los diferentes grupos.

Debes:
- Catalogar las tecnologías adoptadas por los equipos
- Reconocer la diversidad de stacks tecnológicos
- Valorar las decisiones técnicas y su fundamentación
- Identificar patrones comunes y especializaciones
- Presentar el panorama tecnológico de forma clara y organizada

Escribe de forma narrativa, contextualizando las tecnologías con su uso."""
    
    @property
    def instrucciones_extraccion(self) -> str:
        return """
INSTRUCCIONES PARA LA SECCIÓN "III. Ecosistema de Software y Herramientas":

Comienza con un párrafo que presente la diversidad tecnológica del ecosistema de IA en la UTP.

### 3.1 Lenguajes de Programación
Narra cuáles son los lenguajes preferidos y por qué:
- **Python** como lenguaje predominante y sus aplicaciones
- Otros lenguajes utilizados (R, MATLAB, Julia, etc.)
- Contextos de uso de cada lenguaje

### 3.2 Frameworks de Machine Learning y Deep Learning
Describe las herramientas de ML/DL adoptadas:
- Frameworks principales: **TensorFlow**, **PyTorch**, **Keras**
- Bibliotecas de ML clásico: scikit-learn, XGBoost
- Razones de preferencia de los equipos

Usa bullet points para listar frameworks específicos.

### 3.3 Herramientas de Datos y Visualización
Explica cómo los equipos manejan sus datos:
- Bibliotecas de manipulación (Pandas, NumPy)
- Herramientas de visualización
- Bases de datos utilizadas

### 3.4 Plataformas y Entornos de Desarrollo
Describe los ambientes de trabajo:
- Entornos de desarrollo (Jupyter, VS Code)
- Plataformas de experimentación
- Herramientas de versionado y colaboración

### 3.5 Modelos y Recursos Preentrenados
Detalla el uso de modelos existentes:
- Modelos de lenguaje (GPT, BERT, LLaMA)
- Repositorios utilizados (Hugging Face)
- Estrategias de fine-tuning

### 3.6 Software Especializado por Área
Identifica herramientas específicas según el dominio:
- Visión por computador
- Procesamiento de lenguaje natural
- Series temporales y pronóstico
- Otras áreas de aplicación

FORMATO: Alterna explicaciones narrativas con listas de tecnologías específicas.
"""
