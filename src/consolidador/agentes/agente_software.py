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

IMPORTANTE: NO repitas tecnologías en múltiples subsecciones. Cada herramienta debe mencionarse UNA SOLA VEZ en la subsección más apropiada.

Comienza con un párrafo que presente la diversidad tecnológica del ecosistema de IA en la UTP.

### 3.1 Stack Tecnológico Principal
Presenta de forma integrada el conjunto de tecnologías base:
- Lenguaje principal (**Python**) y otros lenguajes complementarios (R, MATLAB, Julia)
- Ecosistema de librerías científicas: NumPy, Pandas, Matplotlib, etc.
- Contexto de uso y nivel de adopción

### 3.2 Frameworks de Machine Learning
Describe ÚNICAMENTE las herramientas de ML/DL (sin repetir librerías de datos):
- Deep Learning: **TensorFlow**, **PyTorch**, **Keras**
- ML clásico: scikit-learn, XGBoost, LightGBM
- Razones de preferencia según el tipo de proyecto

### 3.3 Plataformas y Entornos
Describe los ambientes de trabajo y plataformas cloud:
- Entornos de desarrollo (Jupyter, VS Code, Colab)
- Plataformas cloud (AWS, Google Cloud, Azure)
- Herramientas de versionado y MLOps

### 3.4 Modelos Preentrenados y LLMs
Detalla el uso de modelos existentes:
- Modelos de lenguaje utilizados (GPT, BERT, LLaMA, Whisper)
- Repositorios y fuentes (Hugging Face, OpenAI)
- Estrategias de fine-tuning y adaptación

### 3.5 Herramientas Especializadas por Dominio
Identifica software específico según área de aplicación:
- Visión por computador (OpenCV, YOLO, etc.)
- Procesamiento de señales y audio
- Series temporales y pronóstico
- Otras herramientas de nicho

FORMATO: Cada tecnología debe aparecer UNA SOLA VEZ. Agrupa de forma lógica sin redundancias.
"""
