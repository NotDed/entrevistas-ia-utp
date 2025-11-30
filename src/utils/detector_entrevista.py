"""
Detector de tipo de entrevista: individual vs grupal.
Analiza la transcripción para determinar si hay uno o múltiples entrevistados.
"""
import re
from typing import Dict, List, Optional
from dataclasses import dataclass


@dataclass
class InfoEntrevista:
    """Información sobre el tipo de entrevista detectada."""
    es_grupal: bool
    num_participantes: int
    nombres: List[str]
    area_dependencia: Optional[str]
    genero_predominante: str  # 'femenino', 'masculino', 'mixto'
    
    @property
    def titulo_participantes(self) -> str:
        """Retorna el título apropiado para los participantes."""
        if self.es_grupal:
            return "Entrevistados"
        return "Entrevistado"
    
    @property
    def pronombre(self) -> str:
        """Retorna el pronombre apropiado."""
        if self.es_grupal:
            if self.genero_predominante == 'femenino':
                return "ellas"
            elif self.genero_predominante == 'masculino':
                return "ellos"
            else:
                return "ellos/as"
        else:
            if self.genero_predominante == 'femenino':
                return "ella"
            else:
                return "él"
    
    @property
    def articulo_investigador(self) -> str:
        """Retorna 'el/la/los/las investigador(es/as)'."""
        if self.es_grupal:
            if self.genero_predominante == 'femenino':
                return "las investigadoras"
            elif self.genero_predominante == 'masculino':
                return "los investigadores"
            else:
                return "los investigadores"
        else:
            if self.genero_predominante == 'femenino':
                return "la investigadora"
            else:
                return "el investigador"


# Patrones que indican múltiples participantes
PATRONES_GRUPAL = [
    r'\b(nosotros|nosotras)\b',
    r'\b(nuestro|nuestra|nuestros|nuestras)\s+(grupo|equipo|área|dependencia)',
    r'\ben\s+(el|la)\s+(área|dependencia|facultad|grupo)\b.*\b(trabajamos|hacemos|desarrollamos)\b',
    r'\b(representante|representantes)\s+de\b',
    r'\b(somos|estamos)\s+\d+\s+(personas|integrantes|miembros)\b',
    r'\b(mi compañero|mi compañera|mis compañeros|mis compañeras)\b',
    r'\b(entre|junto con)\s+(los|las|nosotros)\b',
]

# Palabras clave de áreas/dependencias UTP
AREAS_UTP = [
    'Vicerrectoría', 'Decanatura', 'Facultad', 'Departamento', 'Centro',
    'Oficina', 'División', 'Unidad', 'Coordinación', 'Dirección',
    'CRIE', 'Registro y Control', 'Bienestar', 'Planeación',
    'Recursos Tecnológicos', 'Biblioteca', 'Comunicaciones',
    'Investigaciones', 'Extensión', 'Docencia',
]

# Nombres femeninos comunes
NOMBRES_FEMENINOS = [
    'maría', 'maria', 'ana', 'laura', 'sandra', 'diana', 'luz', 'gloria', 
    'patricia', 'martha', 'marta', 'claudia', 'adriana', 'carolina', 
    'mónica', 'monica', 'paola', 'andrea', 'catalina', 'natalia',
    'alejandra', 'juliana', 'daniela', 'valentina', 'camila', 'sofía', 
    'sofia', 'isabel', 'carmen', 'rosa', 'liliana', 'angela', 'ángela',
    'beatriz', 'cecilia', 'paula', 'milena', 'lucía', 'lucia', 'elena',
    'adriana', 'marcela', 'pilar', 'esperanza', 'olga', 'stella',
]


def detectar_genero_nombre(nombre: str) -> str:
    """Detecta el género basado en el nombre."""
    nombre_lower = nombre.lower()
    
    for nombre_fem in NOMBRES_FEMENINOS:
        if nombre_fem in nombre_lower:
            return 'femenino'
    
    # Comprobar primera palabra del nombre
    primer_nombre = nombre_lower.split()[0] if nombre_lower.split() else nombre_lower
    if primer_nombre in NOMBRES_FEMENINOS:
        return 'femenino'
    
    # Terminaciones femeninas comunes (excepto algunas)
    if primer_nombre.endswith('a') and primer_nombre not in ['joshua', 'garcia', 'joshua']:
        return 'femenino'
    
    return 'masculino'


def detectar_tipo_entrevista(transcripcion: str, nombre_archivo: str = "") -> InfoEntrevista:
    """
    Analiza la transcripción para determinar si es individual o grupal.
    
    Args:
        transcripcion: Texto completo de la transcripción.
        nombre_archivo: Nombre del archivo (puede contener pistas).
        
    Returns:
        InfoEntrevista con los detalles detectados.
    """
    texto_lower = transcripcion.lower()
    
    # Contar indicadores de entrevista grupal
    indicadores_grupal = 0
    for patron in PATRONES_GRUPAL:
        matches = re.findall(patron, texto_lower, re.IGNORECASE)
        indicadores_grupal += len(matches)
    
    # Buscar menciones de "yo" vs "nosotros"
    menciones_yo = len(re.findall(r'\byo\b', texto_lower))
    menciones_nosotros = len(re.findall(r'\b(nosotros|nosotras)\b', texto_lower))
    
    # Detectar si hay múltiples hablantes con nombres distintos
    # Buscar patrones como "Speaker 1:", "Hablante 2:", nombres seguidos de ":"
    patrones_hablantes = re.findall(r'(?:speaker|hablante|participante)\s*\d+|([A-ZÁÉÍÓÚ][a-záéíóú]+(?:\s+[A-ZÁÉÍÓÚ][a-záéíóú]+)*)\s*:', transcripcion)
    hablantes_unicos = set([h for h in patrones_hablantes if h and len(h) > 2])
    
    # Detectar área/dependencia mencionada
    area_detectada = None
    for area in AREAS_UTP:
        if area.lower() in texto_lower:
            # Buscar el contexto completo
            match = re.search(rf'(?:de(?:l)?|en)\s+(?:la\s+)?({area}[^,.\n]*)', transcripcion, re.IGNORECASE)
            if match:
                area_detectada = match.group(1).strip()
                break
    
    # Determinar si es grupal
    es_grupal = (
        indicadores_grupal >= 3 or
        menciones_nosotros > menciones_yo * 0.5 or
        len(hablantes_unicos) > 2
    )
    
    # Extraer nombres del archivo o transcripción
    nombres = []
    if nombre_archivo:
        # Limpiar nombre del archivo
        nombre_limpio = nombre_archivo.replace('_original', '').replace('_transcripcion', '').replace('.txt', '')
        
        # Verificar si contiene múltiples nombres (separados por "y", "&", ",")
        if re.search(r'\s+y\s+|\s*&\s*|\s*,\s*', nombre_limpio):
            nombres = re.split(r'\s+y\s+|\s*&\s*|\s*,\s*', nombre_limpio)
            es_grupal = True
        else:
            nombres = [nombre_limpio]
    
    # Determinar género predominante
    if nombres:
        generos = [detectar_genero_nombre(n) for n in nombres]
        femeninos = generos.count('femenino')
        masculinos = generos.count('masculino')
        
        if femeninos > masculinos:
            genero = 'femenino'
        elif masculinos > femeninos:
            genero = 'masculino'
        else:
            genero = 'mixto'
    else:
        genero = 'masculino'  # Default
    
    return InfoEntrevista(
        es_grupal=es_grupal,
        num_participantes=len(nombres) if es_grupal else 1,
        nombres=nombres,
        area_dependencia=area_detectada,
        genero_predominante=genero
    )


def generar_instruccion_contexto(info: InfoEntrevista) -> str:
    """
    Genera una instrucción de contexto para los agentes basada en el tipo de entrevista.
    
    Args:
        info: Información de la entrevista detectada.
        
    Returns:
        Texto con instrucciones de contexto para el prompt.
    """
    if info.es_grupal:
        nombres_str = ", ".join(info.nombres) if info.nombres else "múltiples participantes"
        area_str = f" del área de {info.area_dependencia}" if info.area_dependencia else ""
        
        return f"""
=== CONTEXTO DE LA ENTREVISTA ===
Esta es una ENTREVISTA GRUPAL con {info.num_participantes} participantes{area_str}.
Participantes: {nombres_str}

IMPORTANTE - REDACCIÓN PARA ENTREVISTA GRUPAL:
- Usa plural: "los entrevistados", "las participantes", "{info.articulo_investigador}"
- Consolida las respuestas de todos los participantes
- Indica cuando hay perspectivas diferentes entre participantes
- Atribuye ideas específicas a participantes cuando sea claro quién las expresó
- Usa "{info.pronombre}" como pronombre principal
=====================================
"""
    else:
        nombre_str = info.nombres[0] if info.nombres else "el entrevistado"
        genero_txt = "FEMENINO" if info.genero_predominante == 'femenino' else "MASCULINO"
        
        return f"""
=== CONTEXTO DE LA ENTREVISTA ===
Entrevista INDIVIDUAL con: {nombre_str}
Género: {genero_txt}

Usa concordancia de género correcta:
- "{info.articulo_investigador}", "{info.pronombre}"
=====================================
"""
