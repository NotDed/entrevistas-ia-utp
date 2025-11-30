"""
Agente para generar un reporte narrativo general de la entrevista.
Genera un documento separado que describe de manera fluida lo que
discutió el entrevistado sin seguir la estructura de preguntas.
"""
from .base_agent import BaseAgent


def detectar_genero(nombre: str) -> str:
    """
    Detecta el género probable basándose en el nombre.
    Retorna 'femenino' o 'masculino'.
    """
    nombre_lower = nombre.lower()
    
    # Nombres femeninos comunes en español
    nombres_femeninos = [
        'maría', 'maria', 'ana', 'laura', 'sandra', 'diana', 'luz', 'gloria', 
        'patricia', 'martha', 'marta', 'claudia', 'adriana', 'carolina', 
        'mónica', 'monica', 'paola', 'andrea', 'catalina', 'natalia',
        'alejandra', 'juliana', 'daniela', 'valentina', 'camila', 'sofía', 
        'sofia', 'isabel', 'carmen', 'rosa', 'liliana', 'angela', 'ángela',
        'beatriz', 'cecilia', 'paula', 'milena', 'lucía', 'lucia', 'elena'
    ]
    
    # Terminaciones típicamente femeninas
    for nombre_fem in nombres_femeninos:
        if nombre_fem in nombre_lower:
            return 'femenino'
    
    # Comprobar primera palabra del nombre
    primer_nombre = nombre_lower.split()[0] if nombre_lower.split() else nombre_lower
    if primer_nombre in nombres_femeninos:
        return 'femenino'
    
    # Terminaciones femeninas comunes
    if primer_nombre.endswith('a') and not primer_nombre.endswith('ía'):
        # Muchos nombres femeninos terminan en 'a'
        # Excepciones: Andrés, Tomás no aplican aquí
        return 'femenino'
    
    return 'masculino'


class AgenteNarrativo(BaseAgent):
    """
    Genera un reporte narrativo que cuenta de manera fluida y natural
    lo que el entrevistado compartió durante la entrevista.
    """
    
    @property
    def nombre_seccion(self) -> str:
        return "Reporte Narrativo"
    
    @property
    def prompt_sistema(self) -> str:
        return """Eres un redactor experto en sintetizar entrevistas de manera narrativa y fluida.

Tu tarea es crear un documento que cuente la historia profesional del entrevistado (o grupo de entrevistados)
en relación con la inteligencia artificial, de forma natural y legible.

El documento debe:
- Fluir como una narrativa coherente, no como respuestas a preguntas
- Capturar la esencia de lo que el/los entrevistado(s) compartieron
- Ser accesible para lectores no técnicos pero informativo
- Destacar la trayectoria, experiencias y visión

ESTILO:
- Tercera persona
- Tono profesional pero ameno
- Párrafos bien estructurados
- Sin listas ni bullets (excepto al final si es necesario)
- Evitar repeticiones como "el entrevistado mencionó", "comentó que"

PARA ENTREVISTAS GRUPALES:
- Usa plural consistentemente: "los participantes", "el equipo de trabajo"
- Consolida perspectivas cuando coinciden
- Señala diferencias cuando las hay: "mientras uno enfatiza X, otro destaca Y"
- Representa la voz colectiva del área/dependencia

GÉNERO DEL ENTREVISTADO (para individuales):
Antes de escribir, determina el género de la persona basándote en su nombre:
- Si el nombre es FEMENINO: usa "esta investigadora", "ella", "la profesora"
- Si el nombre es MASCULINO: usa "este investigador", "él", "el profesor"

IMPORTANTE - FORMATO:
- NO incluyas títulos como "## Reporte Narrativo" ni encabezados de sección
- Comienza directamente con el primer párrafo narrativo
- Solo incluye el contenido, sin encabezados decorativos

IMPORTANTE:
- NO estructures por preguntas o bloques de la entrevista
- Crea una narrativa coherente que conecte los temas
- Incluye detalles específicos: proyectos, tecnologías, colaboradores, instituciones"""
    
    @property
    def instrucciones_extraccion(self) -> str:
        return """
INSTRUCCIONES PARA EL REPORTE NARRATIVO:

Genera un documento narrativo de 4-6 párrafos que cuente la historia del entrevistado.

NO INCLUYAS ENCABEZADOS como "## Reporte Narrativo" - empieza directamente con el texto.

ESTRUCTURA SUGERIDA:

**Párrafo 1 - Introducción y contexto:**
¿Quién es esta persona en el ecosistema de IA de la UTP? ¿Cuál es su rol y trayectoria general?

**Párrafo 2 - Proyectos y experiencia técnica:**
¿En qué ha trabajado? Describe los proyectos más relevantes de manera narrativa.
Incluye: tecnologías usadas, dominios de aplicación, resultados logrados.

**Párrafo 3 - Colaboraciones y redes:**
¿Con quiénes trabaja? ¿Cómo se relaciona con otros grupos, instituciones o actores externos?
Nombra colaboradores, grupos de investigación, alianzas.

**Párrafo 4 - Desafíos y contexto:**
¿Qué obstáculos ha enfrentado? ¿Cuál es el contexto en el que trabaja?
Describe las dificultades y cómo las ha navegado.

**Párrafo 5 - Visión y propuestas:**
¿Hacia dónde quiere ir? ¿Qué propone para la UTP?
Captura su visión estratégica y propuestas concretas.

**Párrafo 6 (opcional) - Cierre:**
Un párrafo de síntesis que capture la esencia de su aporte potencial.

---

**Puntos destacados** (3-5 bullets al final):
Los aspectos más memorables o diferenciadores de este entrevistado.

TONO: Profesional, informativo, fluido. Como un perfil en una revista o un resumen ejecutivo narrativo.
"""
    
    def construir_prompt_usuario_con_nombre(self, transcripcion: str, nombre_entrevistado: str, info_entrevista = None) -> str:
        """
        Construye el prompt de usuario con la transcripción y el nombre.
        Incluye instrucciones explícitas de género y tipo de entrevista.
        
        Args:
            transcripcion: Texto de la transcripción.
            nombre_entrevistado: Nombre del entrevistado o área.
            info_entrevista: InfoEntrevista con detalles de tipo de entrevista.
        """
        from config import REGLAS_GLOBALES
        
        # Determinar si es grupal y ajustar instrucciones
        if info_entrevista and info_entrevista.es_grupal:
            participantes = ", ".join(info_entrevista.nombres) if info_entrevista.nombres else "múltiples participantes"
            area = info_entrevista.area_dependencia or "área no especificada"
            
            instruccion_contexto = f"""
=== INFORMACIÓN DE LA ENTREVISTA ===
TIPO: ENTREVISTA GRUPAL
Participantes: {participantes}
Área/Dependencia: {area}
Número de participantes: {info_entrevista.num_participantes}

IMPORTANTE - REDACCIÓN PARA GRUPO:
- Usa plural: "los entrevistados", "el equipo", "los participantes"
- Consolida las perspectivas de todos en una narrativa coherente
- Menciona cuando hay diferencias de opinión o experiencias variadas
- Usa: "{info_entrevista.articulo_investigador}"
- Pronombre principal: "{info_entrevista.pronombre}"
===================================
"""
        else:
            genero = detectar_genero(nombre_entrevistado)
            
            if genero == 'femenino':
                instruccion_contexto = f"""
=== INFORMACIÓN DEL ENTREVISTADO ===
Nombre: {nombre_entrevistado}
Género: FEMENINO

IMPORTANTE - CONCORDANCIA DE GÉNERO:
Debes usar OBLIGATORIAMENTE pronombres y sustantivos FEMENINOS:
- "esta investigadora", "la profesora", "ella"
- "ha desarrollado", "lidera", "su trabajo la ha llevado"
- "la docente", "la experta", "esta profesional"
NUNCA uses "el investigador", "él", "este profesional" para esta persona.
===================================
"""
            else:
                instruccion_contexto = f"""
=== INFORMACIÓN DEL ENTREVISTADO ===
Nombre: {nombre_entrevistado}
Género: MASCULINO

Usa pronombres y sustantivos masculinos:
- "este investigador", "el profesor", "él"
===================================
"""
        
        return f"""
{instruccion_contexto}

{REGLAS_GLOBALES}

{self.instrucciones_extraccion}

---
TRANSCRIPCIÓN DE LA ENTREVISTA:
---
{transcripcion}
---

Genera el reporte narrativo en formato Markdown. Comienza directamente con el texto, sin encabezados.
"""
    
    def process(self, transcripcion: str, nombre_entrevistado: str = None, info_entrevista = None) -> str:
        """
        Procesa la transcripción y genera el reporte narrativo.
        
        Args:
            transcripcion: Texto de la transcripción.
            nombre_entrevistado: Nombre del entrevistado para determinar género.
            info_entrevista: InfoEntrevista con detalles de tipo de entrevista.
            
        Returns:
            Reporte narrativo en formato Markdown.
        """
        if nombre_entrevistado or info_entrevista:
            prompt_usuario = self.construir_prompt_usuario_con_nombre(transcripcion, nombre_entrevistado, info_entrevista)
        else:
            prompt_usuario = self.construir_prompt_usuario(transcripcion)
        
        if self.provider == "openai":
            return self._llamar_openai(self.prompt_sistema, prompt_usuario)
        else:
            prompt_completo = f"{self.prompt_sistema}\n\n{prompt_usuario}"
            return self._llamar_gemini(prompt_completo)
    
    async def process_async(self, transcripcion: str, nombre_entrevistado: str = None, info_entrevista = None) -> str:
        """
        Versión asíncrona de process.
        """
        import asyncio
        loop = asyncio.get_event_loop()
        return await loop.run_in_executor(
            None, lambda: self.process(transcripcion, nombre_entrevistado, info_entrevista)
        )
