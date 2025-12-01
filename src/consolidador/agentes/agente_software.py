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
        return """Eres un experto en tecnologías de Inteligencia Artificial y Machine Learning.
Tu tarea es catalogar el ecosistema completo de software, frameworks, bibliotecas y 
herramientas utilizadas para proyectos de IA en la Universidad Tecnológica de Pereira.

Debes identificar:
- Lenguajes de programación predominantes
- Frameworks de Machine Learning y Deep Learning
- Bibliotecas especializadas
- Plataformas de desarrollo y experimentación
- Herramientas de gestión de datos
- Software especializado por área de aplicación"""
    
    @property
    def instrucciones_extraccion(self) -> str:
        return """
INSTRUCCIONES PARA LA SECCIÓN "III. Ecosistema de Software y Herramientas":

Organiza la información en las siguientes subsecciones:

### 3.1 Lenguajes de Programación
- Lenguajes principales utilizados (Python, R, Julia, MATLAB, etc.)
- Nivel de adopción en la comunidad
- Casos de uso por lenguaje

### 3.2 Frameworks de Machine Learning
- Frameworks de Deep Learning (TensorFlow, PyTorch, Keras, etc.)
- Bibliotecas de ML clásico (scikit-learn, XGBoost, etc.)
- Preferencias y razones de adopción

### 3.3 Herramientas de Procesamiento de Datos
- Bibliotecas de manipulación de datos (Pandas, NumPy, etc.)
- Herramientas de visualización
- Bases de datos utilizadas

### 3.4 Plataformas y Entornos
- Entornos de desarrollo (Jupyter, VS Code, etc.)
- Plataformas de experimentación (MLflow, Weights & Biases, etc.)
- Herramientas de versionado y colaboración

### 3.5 Software Especializado
- Herramientas específicas por área (visión por computador, NLP, etc.)
- Software propietario vs open source
- APIs y servicios externos utilizados

### 3.6 Modelos y Recursos Preentrenados
- Modelos de lenguaje utilizados (GPT, BERT, LLaMA, etc.)
- Repositorios de modelos (Hugging Face, etc.)
- Estrategias de fine-tuning

FORMATO: Agrupa las tecnologías por categoría, indicando nivel de uso cuando sea posible.
"""
