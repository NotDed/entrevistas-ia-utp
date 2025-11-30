"""
Configuración del sistema multi-agente para análisis de entrevistas.
"""
import os
from dotenv import load_dotenv

load_dotenv()

# Proveedor de LLM ("openai" o "gemini")
LLM_PROVIDER = os.getenv("LLM_PROVIDER", "openai")

# OpenAI Configuration
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
OPENAI_MODEL = os.getenv("OPENAI_MODEL", "gpt-4o-mini")

# Google Gemini Configuration
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
GEMINI_MODEL = os.getenv("GEMINI_MODEL", "gemini-2.0-flash")

# Configuración general
MAX_TOKENS = int(os.getenv("MAX_TOKENS", "4000"))
TEMPERATURE = float(os.getenv("TEMPERATURE", "0.3"))

# Paths
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_RAW_DIR = os.path.join(BASE_DIR, "data", "raw")
DATA_OUTPUTS_DIR = os.path.join(BASE_DIR, "data", "outputs")

# Reglas globales para todos los agentes
REGLAS_GLOBALES = """
REGLAS GLOBALES (OBLIGATORIAS):
- Trabajar ÚNICAMENTE con la información textual presente en la transcripción.
- No inventar, inferir ni completar datos que no estén explícitamente mencionados.
- IMPORTANTE: Las transcripciones pueden contener errores de transcripción automática (palabras mal escritas, nombres incorrectos, frases incompletas). Interpreta el contexto para entender el significado real.
- Si una información NO aparece en la transcripción, simplemente OMITE ese campo. NO escribas "No mencionado".
- Solo incluir información que SÍ fue mencionada. Omitir secciones o campos vacíos.
- Mantener un tono formal, claro y orientado a informes.
- Devolver SOLO el contenido de tu sección en Markdown, sin comentarios adicionales.
- No repetir las instrucciones ni reescribir la transcripción.
"""
