"""
Agente consolidador de infraestructura IA.

Este agente analiza múltiples transcripciones de entrevistas y genera
un reporte consolidado sobre grupos de investigación, hardware, software
e infraestructura de IA en la Universidad Tecnológica de Pereira.
"""
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from config import (
    LLM_PROVIDER, 
    OPENAI_API_KEY, OPENAI_MODEL,
    GOOGLE_API_KEY, GEMINI_MODEL,
    TEMPERATURE
)


class AgenteConsolidadorInfraestructura:
    """
    Agente especializado en consolidar información de infraestructura IA
    de múltiples entrevistas en un documento unificado.
    
    No hereda de BaseAgent porque tiene un flujo diferente:
    procesa múltiples transcripciones en lugar de una sola.
    """
    
    nombre = "Consolidador de Infraestructura IA"
    
    # Tokens más altos para el consolidado (documento largo)
    max_tokens = 16000
    
    prompt_sistema = """Eres un analista experto redactando informes ejecutivos sobre infraestructura tecnológica universitaria. Tu tarea es consolidar información de múltiples entrevistas sobre Inteligencia Artificial en la Universidad Tecnológica de Pereira (UTP).

ESTILO DE REDACCIÓN - MUY IMPORTANTE:
- Usa la JERARQUÍA DE ENCABEZADOS para organizar, NO viñetas anidadas
- Estructura: ## Sección → ### Subsección → #### Sub-subsección → viñetas simples
- Las viñetas (-) son SOLO para listas finales de items concretos, NUNCA para categorías
- Cada viñeta debe ser un item final, no una categoría que contenga más viñetas
- Usa **negritas** para términos clave dentro del texto

EJEMPLO CORRECTO:
```
## II. Inventario de Hardware

### Grupo Nyquist

#### Equipos de Cómputo
- Portátil personal del investigador
- 2 equipos de altas prestaciones del grupo

#### Servidores
- Servidor propio del grupo con GPU dedicada
```

EJEMPLO INCORRECTO (NO hacer esto):
```
- **Grupo Nyquist:**
  - Equipos:
    - Portátil personal
    - 2 equipos de altas prestaciones
```

ESTRUCTURA DEL DOCUMENTO:

## I. Grupos y Laboratorios de IA

Para cada grupo identificado, usar esta estructura:

### [Nombre del Grupo]

#### Información General
- Facultad/Área a la que pertenece
- Investigadores principales mencionados

#### Líneas de Investigación en IA

##### [Nombre de cada línea]
Descripción breve de la línea y proyectos asociados.

## II. Inventario de Hardware

### [Nombre del Área/Grupo]

#### Equipos Propios
- Lista de equipos con especificaciones

#### Recursos Institucionales
- Lista de recursos compartidos

## III. Software y Frameworks

### Lenguajes de Programación
- Lista de lenguajes

### Frameworks de Machine Learning
- Lista con contexto de uso

### Plataformas Cloud
- Lista de servicios

### Herramientas Especializadas
- Lista de herramientas

## IV. Perspectivas de los Entrevistados

### Fortalezas Identificadas
- Viñetas con fortalezas (incluir citas y nombres)

### Limitaciones y Desafíos
- Viñetas con limitaciones

### Necesidades Expresadas
- Viñetas con necesidades

## V. Análisis de Capacidad

### Capacidad Actual
Párrafo evaluativo.

### Escalabilidad
Párrafo evaluativo.

### Brechas Críticas
- Lista de brechas

## VI. Propuestas de Mejora

### Corto Plazo
- Propuestas con justificación breve

### Mediano y Largo Plazo
- Propuestas estratégicas

## VII. Conclusiones

### Estado Actual
Párrafo de síntesis.

### Recomendaciones Priorizadas
1. Primera recomendación con justificación
2. Segunda recomendación
3. Tercera recomendación

REGLAS CRÍTICAS:
- NUNCA uses viñetas anidadas (viñeta dentro de viñeta)
- Si necesitas subcategorías, usa #### o ##### como encabezado
- Las viñetas son SOLO para el nivel más bajo de la jerarquía
- Basa todo en información explícita de las transcripciones
- Atribuye información al entrevistado correspondiente
"""
    
    def __init__(self):
        self.provider = LLM_PROVIDER.lower()
        self.temperature = TEMPERATURE
        
        if self.provider == "openai":
            from openai import OpenAI
            self.client = OpenAI(api_key=OPENAI_API_KEY)
            self.model = OPENAI_MODEL
        else:  # gemini
            from google import genai
            self.client = genai.Client(api_key=GOOGLE_API_KEY)
            self.model = GEMINI_MODEL
    
    def ejecutar(self, transcripciones_consolidadas: str) -> str:
        """
        Ejecuta el agente consolidador.
        
        Args:
            transcripciones_consolidadas: Texto con todas las transcripciones
                                          concatenadas y etiquetadas.
                                          
        Returns:
            Reporte consolidado en formato Markdown.
        """
        prompt_usuario = f"""Analiza las siguientes transcripciones de entrevistas sobre Inteligencia Artificial en la Universidad Tecnológica de Pereira y genera el reporte consolidado de infraestructura.

{transcripciones_consolidadas}

Genera el documento consolidado siguiendo la estructura indicada en tus instrucciones."""
        
        if self.provider == "openai":
            return self._llamar_openai(prompt_usuario)
        else:
            return self._llamar_gemini(prompt_usuario)
    
    def _llamar_openai(self, prompt_usuario: str) -> str:
        """Llama a la API de OpenAI."""
        # Usar max_completion_tokens para modelos nuevos
        use_new_param = any(x in self.model for x in ['gpt-4.1', 'gpt-5', 'o1', 'o3'])
        
        params = {
            "model": self.model,
            "messages": [
                {"role": "system", "content": self.prompt_sistema},
                {"role": "user", "content": prompt_usuario}
            ],
            "temperature": self.temperature,
        }
        
        if use_new_param:
            params["max_completion_tokens"] = self.max_tokens
        else:
            params["max_tokens"] = self.max_tokens
        
        response = self.client.chat.completions.create(**params)
        return response.choices[0].message.content
    
    def _llamar_gemini(self, prompt_usuario: str) -> str:
        """Llama a la API de Gemini."""
        from google.genai import types
        
        response = self.client.models.generate_content(
            model=self.model,
            contents=prompt_usuario,
            config=types.GenerateContentConfig(
                system_instruction=self.prompt_sistema,
                temperature=self.temperature,
                max_output_tokens=self.max_tokens
            )
        )
        return response.text
