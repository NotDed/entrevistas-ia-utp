"""
Agente para detectar y corregir errores contextuales de transcripción.
Este agente se ejecuta primero y prepara el texto para los demás agentes.
"""
from .base_agent import BaseAgent


class AgenteCorreccion(BaseAgent):
    """
    Detecta y corrige errores de transcripción automática basándose en el contexto.
    Especialmente útil para:
    - Nombres de tecnologías (tensor flau → TensorFlow, quedas → Keras)
    - Nombres de personas e instituciones
    - Términos técnicos de IA
    - Acrónimos y siglas
    """
    
    @property
    def nombre_seccion(self) -> str:
        return "Corrección de transcripción"
    
    @property
    def prompt_sistema(self) -> str:
        return """Eres un agente especializado en corregir errores de transcripción automática 
en entrevistas sobre inteligencia artificial realizadas en la Universidad Tecnológica de Pereira (UTP).

Las transcripciones automáticas suelen contener errores de reconocimiento de voz, especialmente en:

1. NOMBRES DE TECNOLOGÍAS Y FRAMEWORKS:
   - "tensor flau", "tensor flow", "tensor flo" → TensorFlow
   - "quedas", "keras", "queras" → Keras
   - "pai torch", "pai tors", "paytorch" → PyTorch
   - "phyton", "paiton", "python" → Python
   - "scikit learn", "saiki learn" → scikit-learn
   - "numpy", "nam pai" → NumPy
   - "pandas", "pandas" → pandas
   - "jupyter", "yupiter" → Jupyter
   - "colab", "co lab", "google colab" → Google Colab
   - "hugging face", "jaging feis" → Hugging Face
   - "open ai", "open ey ai" → OpenAI
   - "chat gpt", "chat yipi ti" → ChatGPT
   - "llm", "ele ele eme" → LLM (Large Language Model)

2. TÉRMINOS TÉCNICOS DE IA:
   - "machine learning", "machine lerning" → machine learning
   - "deep learning", "dip lerning" → deep learning
   - "neural network", "neuronal network" → red neuronal
   - "convolutional", "convolucional" → convolucional
   - "clustering", "clastering" → clustering
   - "overfitting", "over fiting" → overfitting
   - "dataset", "data set" → dataset
   - "API", "a pi ai" → API
   - "GPU", "yi pi yu" → GPU
   - "CPU", "ci pi yu" → CPU
   - "RAM", "ram" → RAM
   - "raspberry pi", "rasberry pai", "narras berry" → Raspberry Pi
   - "lora", "lo ra" → LoRa (Long Range)

3. INSTITUCIONES Y GRUPOS DE INVESTIGACIÓN UTP:
   (Referencia: https://vicerrectorias.utp.edu.co/viie/todos-los-grupos/)
   
   CORRECCIÓN CRÍTICA - MUY IMPORTANTE:
   - Cuando aparezca "grupo Nike", "al grupo Nike", "grupo nike" → SIEMPRE corregir a "grupo Nyquist"
   - "Nike" en contexto de grupo de investigación de la UTP → "Nyquist"
   - NO existe un grupo de investigación llamado "Nike" en la UTP. El nombre correcto es "Nyquist".
   
   Otras correcciones de grupos:
   - "UTP", "u te pe" → UTP (Universidad Tecnológica de Pereira)
   - "GIROPS", "jirops", "girops" → GIROPS
   - "sirius", "sirios" → SIRIUS
   - "grande", "grando" → GRANDE
   - "geio", "geo" → GEIO
   - "gta", "g t a" → GTA
   - "omicron" → OMICRON
   - "campos electromagnéticos" → Campos Electromagnéticos
   - "ce3" → CE3
   - "bioelectrica" → Bioeléctrica
   - "laboratorio de metrología" → Laboratorio de Metrología
   - "gestión ambiental" → Gestión Ambiental
   - "gaia" → GAIA
   - "colciencias", "col ciencias" → Colciencias/Minciencias
   - "SiB Colombia", "sib colombia", "sid Colombia" → SiB Colombia

4. OTROS ERRORES COMUNES:
   - Palabras cortadas o incompletas
   - Homófonos incorrectos
   - Puntuación faltante o incorrecta
   - Nombres propios mal transcritos

Tu tarea es:
1. Identificar errores de transcripción basándote en el CONTEXTO
2. Corregir estos errores manteniendo el sentido original
3. NO cambiar el contenido ni añadir información
4. Mantener el formato y estructura del texto original
5. Generar una lista de las correcciones realizadas"""
    
    @property
    def instrucciones_extraccion(self) -> str:
        return """
INSTRUCCIONES PARA CORRECCIÓN DE TRANSCRIPCIÓN:

1. Lee toda la transcripción para entender el contexto
2. Identifica errores de reconocimiento de voz (especialmente tecnologías, nombres, términos técnicos)
3. Corrige los errores basándote en el contexto técnico y académico
4. Mantén el estilo conversacional original

ATENCIÓN ESPECIAL A GRUPOS DE INVESTIGACIÓN UTP:
- Si ves "Nike", "nike", "naiqui" en contexto de grupo de investigación → corregir a "Nyquist"
- Si ves "jirops", "girops" → corregir a "GIROPS"
- Nyquist es un grupo de investigación en procesamiento de señales de la UTP
- La lista completa de grupos está en: https://vicerrectorias.utp.edu.co/viie/todos-los-grupos/

FORMATO DE SALIDA OBLIGATORIO:
Debes devolver EXACTAMENTE este formato con las dos secciones:

[Aquí va la transcripción corregida completa]

---CORRECCIONES---
- error original → corrección aplicada
- error original → corrección aplicada
(lista todas las correcciones realizadas)

Si no hay correcciones necesarias, escribe:
---CORRECCIONES---
- Sin correcciones significativas detectadas

IMPORTANTE: Siempre incluir la sección ---CORRECCIONES--- aunque no haya correcciones.
"""

    # Correcciones conocidas que siempre deben aplicarse (errores frecuentes de transcripción)
    CORRECCIONES_CONOCIDAS = [
        # Grupos de investigación UTP (lista completa en https://vicerrectorias.utp.edu.co/viie/todos-los-grupos/)
        (r'\bgrupo Nike\b', 'grupo Nyquist'),
        (r'\bgrupo nike\b', 'grupo Nyquist'),
        (r'\bal grupo Nike\b', 'al grupo Nyquist'),
        (r'\bNIKe\b', 'Nyquist'),
        (r'\bjirops\b', 'GIROPS'),
        (r'\bgirops\b', 'GIROPS'),
        (r'\bsirius\b', 'SIRIUS'),
        (r'\bgeio\b', 'GEIO'),
        (r'\bgaope\b', 'GAOPE'),
        (r'\bcafe\b(?=.*electromagn)', 'CAFE'),
        (r'\bgicto\b', 'GICTO'),
        (r'\bdinop\b', 'DINOP'),
        (r'\bdicoped\b', 'DICOPED'),
        (r'\beis\b(?=.*ecolog)', 'EIS'),
        (r'\bgrieni\b', 'GRIENI'),
        (r'\bise\b(?=.*estad)', 'ISE'),
        (r'\bgia\b(?=.*inteligencia)', 'GIA'),
        (r'\bice3\b', 'ICE3'),
        (r'\bgredya\b', 'GREDYA'),
        (r'\bgiadsc\b', 'GIADSc'),
        (r'\bgida\b', 'GIDA'),
        (r'\bgifamol\b', 'GIFAMOL'),
        (r'\bgigede\b', 'GIGEDE'),
        (r'\bgenergetica\b', 'GENERGETICA'),
        (r'\bgimcci\b', 'GIMCCI'),
        (r'\bgiped\b', 'GIPED'),
        (r'\bgispaps\b', 'GISPAPS'),
        (r'\bgerh\b', 'GERH'),
        (r'\bgiga\b(?=.*geometr)', 'GIGA'),
        (r'\bgirus\b', 'GIRUS'),
        (r'\bgimav\b', 'GIMAV'),
        (r'\bgimi\b', 'GIMI'),
        (r'\bgimosic\b', 'GIMOSIC'),
        (r'\bgipemac\b', 'GIPEMAC'),
        (r'\bgipco\b', 'GIPCO'),
        (r'\bmecabot\b', 'MECABOT'),
        (r'\bmeocri\b', 'MEOCRI'),
        (r'\blider\b(?=.*laboratorio)', 'LÍDER'),
        (r'\bmenta\b(?=.*tic)', 'MENTA'),
        # Tecnologías
        (r'\btensor flau\b', 'TensorFlow'),
        (r'\btensor flo\b', 'TensorFlow'),
        (r'\bnarras berry\b', 'Raspberry Pi'),
        (r'\bquedas\b', 'Keras'),
        (r'\bsid Colombia\b', 'SiB Colombia'),
        # Otros errores comunes
        (r'\by el avión trabajando\b', 'y ha venido trabajando'),
    ]

    def _aplicar_correcciones_conocidas(self, texto: str) -> tuple:
        """
        Aplica correcciones conocidas que siempre deben realizarse.
        
        Args:
            texto: Texto a corregir.
            
        Returns:
            Tupla (texto_corregido, lista_correcciones).
        """
        import re
        correcciones_aplicadas = []
        
        for patron, reemplazo in self.CORRECCIONES_CONOCIDAS:
            if re.search(patron, texto, re.IGNORECASE):
                texto = re.sub(patron, reemplazo, texto, flags=re.IGNORECASE)
                correcciones_aplicadas.append(f"- {patron} → {reemplazo}")
        
        return texto, correcciones_aplicadas

    def _aplicar_correcciones(self, texto: str, correcciones: str) -> str:
        """
        Aplica las correcciones detectadas al texto original.
        
        Args:
            texto: Texto original.
            correcciones: Lista de correcciones en formato "original → corregido".
            
        Returns:
            Texto con las correcciones aplicadas.
        """
        import re
        
        if not correcciones:
            return texto
        
        for linea in correcciones.split('\n'):
            linea = linea.strip()
            if not linea:
                continue
            
            # Buscar patrones de corrección: "original" → "corregido" o similar
            match = None
            for separador in ['→', '->', '=>']:
                if separador in linea:
                    partes = linea.split(separador)
                    if len(partes) == 2:
                        original = partes[0].strip().strip('-•*"\'').strip()
                        corregido = partes[1].strip().strip('"\'').strip()
                        if original and corregido:
                            # Aplicar reemplazo case-insensitive
                            texto = re.sub(
                                re.escape(original), 
                                corregido, 
                                texto, 
                                flags=re.IGNORECASE
                            )
                        break
        
        return texto

    def process(self, transcripcion: str) -> dict:
        """
        Procesa la transcripción y devuelve el texto corregido y la lista de correcciones.
        
        Args:
            transcripcion: Texto original de la transcripción.
            
        Returns:
            Diccionario con 'texto_corregido' y 'correcciones'.
        """
        import time
        
        max_retries = 3
        prompt_usuario = f"""{self.instrucciones_extraccion}

---
TRANSCRIPCIÓN ORIGINAL:
---
{transcripcion}
---

Corrige los errores de transcripción y lista las correcciones realizadas.
"""
        
        for attempt in range(max_retries):
            try:
                if self.provider == "openai":
                    # Modelos nuevos usan max_completion_tokens
                    use_new_param = any(x in self.model for x in ['gpt-4.1', 'gpt-5', 'o1', 'o3'])
                    params = {
                        "model": self.model,
                        "messages": [
                            {"role": "system", "content": self.prompt_sistema},
                            {"role": "user", "content": prompt_usuario}
                        ],
                        "temperature": 0.1
                    }
                    if use_new_param:
                        params["max_completion_tokens"] = self.max_tokens * 2
                    else:
                        params["max_tokens"] = self.max_tokens * 2
                    
                    response = self.client.chat.completions.create(**params)
                    resultado = response.choices[0].message.content.strip()
                else:  # gemini
                    from google.genai import types
                    prompt_completo = f"{self.prompt_sistema}\n\n{prompt_usuario}"
                    response = self.client.models.generate_content(
                        model=self.model,
                        contents=prompt_completo,
                        config=types.GenerateContentConfig(
                            max_output_tokens=self.max_tokens * 2,
                            temperature=0.1
                        )
                    )
                    resultado = response.text.strip()
                
                # Parsear el resultado
                # Buscar el separador de correcciones de manera más flexible
                separadores = ["---CORRECCIONES---", "---correcciones---", "CORRECCIONES:", "Correcciones:"]
                texto_corregido = resultado
                correcciones = ""
                
                for sep in separadores:
                    if sep.lower() in resultado.lower():
                        idx = resultado.lower().find(sep.lower())
                        texto_corregido = resultado[:idx].strip()
                        correcciones = resultado[idx + len(sep):].strip()
                        break
                
                # Si el texto corregido está vacío o muy corto, aplicar correcciones manualmente
                if not texto_corregido or len(texto_corregido) < len(transcripcion) * 0.5:
                    texto_corregido = transcripcion
                    # Aplicar las correcciones detectadas al texto original
                    texto_corregido = self._aplicar_correcciones(texto_corregido, correcciones)
                
                # SIEMPRE aplicar correcciones conocidas al final (fallback)
                texto_corregido, correcciones_adicionales = self._aplicar_correcciones_conocidas(texto_corregido)
                
                # Combinar correcciones
                if correcciones_adicionales:
                    if correcciones:
                        correcciones = correcciones + "\n" + "\n".join(correcciones_adicionales)
                    else:
                        correcciones = "\n".join(correcciones_adicionales)
                
                return {
                    'texto_corregido': texto_corregido,
                    'correcciones': correcciones
                }
                
            except Exception as e:
                error_str = str(e)
                if "429" in error_str or "RESOURCE_EXHAUSTED" in error_str or "rate" in error_str.lower():
                    wait_time = 10 * (attempt + 1)
                    print(f"      ⏳ Rate limit. Esperando {wait_time}s...")
                    time.sleep(wait_time)
                    continue
                return {
                    'texto_corregido': transcripcion,
                    'correcciones': f"Error al procesar: {str(e)}"
                }
        
        return {
            'texto_corregido': transcripcion,
            'correcciones': "Error: Rate limit excedido."
        }
    
    def obtener_resumen_correcciones(self, correcciones: str) -> str:
        """
        Ya no se incluye nota de correcciones en el reporte final.
        
        Returns:
            Cadena vacía (las correcciones se aplican pero no se documentan).
        """
        return ""
    
    def contar_correcciones(self, correcciones: str) -> int:
        """
        Cuenta el número de correcciones detectadas.
        """
        if not correcciones:
            return 0
        
        count = 0
        for l in correcciones.split('\n'):
            l = l.strip()
            if l.startswith('-') or l.startswith('•') or l.startswith('*'):
                count += 1
            elif '→' in l or '->' in l or '=>' in l:
                count += 1
        return count
