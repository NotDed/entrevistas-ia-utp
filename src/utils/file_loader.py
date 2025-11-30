"""
Utilidades para carga y manejo de archivos de transcripciones.
"""
import os
from pathlib import Path
from typing import List, Tuple


def cargar_transcripcion(ruta_archivo: str) -> str:
    """
    Carga una transcripción desde un archivo de texto.
    Detecta automáticamente la codificación.
    
    Args:
        ruta_archivo: Ruta al archivo de transcripción.
        
    Returns:
        Contenido de la transcripción como string.
    """
    # Intentar diferentes codificaciones
    codificaciones = ['utf-8', 'utf-16', 'utf-16-le', 'utf-16-be', 'latin-1', 'cp1252']
    
    for encoding in codificaciones:
        try:
            with open(ruta_archivo, 'r', encoding=encoding) as f:
                return f.read()
        except (UnicodeDecodeError, UnicodeError):
            continue
    
    # Fallback: leer como binario y decodificar
    with open(ruta_archivo, 'rb') as f:
        content = f.read()
        # Detectar BOM y decodificar apropiadamente
        if content.startswith(b'\xff\xfe') or content.startswith(b'\xfe\xff'):
            return content.decode('utf-16')
        return content.decode('latin-1')


def listar_transcripciones(directorio: str) -> List[str]:
    """
    Lista todos los archivos de transcripción en un directorio.
    
    Args:
        directorio: Ruta al directorio con transcripciones.
        
    Returns:
        Lista de rutas completas a los archivos .txt
    """
    directorio_path = Path(directorio)
    if not directorio_path.exists():
        return []
    
    return [str(f) for f in directorio_path.glob("*.txt")]


def extraer_nombre_entrevistado(ruta_archivo: str) -> str:
    """
    Extrae el nombre del entrevistado del nombre del archivo.
    
    Args:
        ruta_archivo: Ruta al archivo de transcripción.
        
    Returns:
        Nombre del entrevistado (sin extensión ni sufijos como _original).
    """
    nombre_archivo = Path(ruta_archivo).stem
    # Remover sufijos comunes
    for sufijo in ['_original', '_transcripcion', '_entrevista']:
        nombre_archivo = nombre_archivo.replace(sufijo, '')
    return nombre_archivo.strip()


def guardar_reporte(contenido: str, ruta_salida: str) -> None:
    """
    Guarda el reporte generado en un archivo Markdown.
    
    Args:
        contenido: Contenido del reporte en Markdown.
        ruta_salida: Ruta donde guardar el archivo.
    """
    # Crear directorio si no existe
    os.makedirs(os.path.dirname(ruta_salida), exist_ok=True)
    
    with open(ruta_salida, 'w', encoding='utf-8') as f:
        f.write(contenido)
