#!/usr/bin/env python3
"""
Sistema Multi-Agente para Análisis de Entrevistas UTP

Este script procesa transcripciones de entrevistas sobre inteligencia artificial
y genera reportes estructurados utilizando un sistema de 7 agentes especializados.

Uso:
    python main.py                          # Procesa todas las transcripciones en data/raw/
    python main.py archivo.txt              # Procesa un archivo específico
    python main.py --paralelo               # Ejecuta agentes en paralelo
    python main.py --help                   # Muestra ayuda
"""
import os
import sys
import argparse
from pathlib import Path

# Agregar el directorio src al path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from config import DATA_RAW_DIR, DATA_OUTPUTS_DIR
from agents import AgenteIntegrador
from utils.file_loader import (
    cargar_transcripcion,
    listar_transcripciones,
    extraer_nombre_entrevistado,
    guardar_reporte
)
from utils.latex_generator import guardar_latex_y_pdf


def procesar_transcripcion(
    ruta_archivo: str,
    integrador: AgenteIntegrador,
    output_dir: str,
    paralelo: bool = False,
    verbose: bool = True
) -> tuple:
    """
    Procesa una transcripción y genera los reportes.
    
    Args:
        ruta_archivo: Ruta al archivo de transcripción.
        integrador: Instancia del agente integrador.
        output_dir: Directorio base donde guardar el reporte.
        paralelo: Si True, ejecuta agentes en paralelo.
        verbose: Si True, muestra progreso.
        
    Returns:
        Tupla con rutas a los archivos PDF generados (detallado, narrativo).
    """
    nombre_entrevistado = extraer_nombre_entrevistado(ruta_archivo)
    
    # Crear carpeta individual para este entrevistado
    carpeta_entrevistado = os.path.join(output_dir, nombre_entrevistado)
    os.makedirs(carpeta_entrevistado, exist_ok=True)
    
    if verbose:
        print(f"\n{'='*60}")
        print(f"Procesando: {nombre_entrevistado}")
        print(f"{'='*60}")
    
    # Cargar transcripción
    if verbose:
        print(f"  Cargando transcripción...")
    transcripcion = cargar_transcripcion(ruta_archivo)
    
    # Procesar con el integrador
    if verbose:
        modo = "paralelo" if paralelo else "secuencial"
        print(f"  Ejecutando sistema multi-agente (modo {modo})...")
    
    reportes = integrador.procesar(
        transcripcion=transcripcion,
        nombre_entrevistado=nombre_entrevistado,
        paralelo=paralelo,
        verbose=verbose
    )
    
    # Generar PDFs con LaTeX (directamente, sin guardar MD)
    if verbose:
        print(f"\n  Generando PDFs con LaTeX...")
    
    try:
        ruta_pdf_detallado = guardar_latex_y_pdf(
            reportes['detallado'], 
            nombre_entrevistado, 
            carpeta_entrevistado, 
            tipo="detallado"
        )
        ruta_pdf_narrativo = guardar_latex_y_pdf(
            reportes['narrativo'], 
            nombre_entrevistado,
            carpeta_entrevistado, 
            tipo="narrativo"
        )
        
        if verbose:
            print(f"  ✓ PDF detallado: {ruta_pdf_detallado}")
            print(f"  ✓ PDF narrativo: {ruta_pdf_narrativo}")
        
        return (ruta_pdf_detallado, ruta_pdf_narrativo)
    except Exception as e:
        if verbose:
            print(f"  ⚠ Error generando PDFs: {e}")
            import traceback
            traceback.print_exc()
        raise


def main():
    """Función principal del sistema."""
    parser = argparse.ArgumentParser(
        description="Sistema Multi-Agente para Análisis de Entrevistas UTP",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Ejemplos:
  python main.py                              # Procesa todos los archivos en data/raw/
  python main.py "entrevista.txt"             # Procesa un archivo específico
  python main.py --paralelo                   # Ejecuta agentes en paralelo (más rápido)
  python main.py --directorio ./mis_datos     # Usa un directorio personalizado
        """
    )
    
    parser.add_argument(
        "archivo",
        nargs="?",
        help="Archivo de transcripción específico a procesar"
    )
    
    parser.add_argument(
        "--directorio", "-d",
        default=DATA_RAW_DIR,
        help=f"Directorio con transcripciones (default: {DATA_RAW_DIR})"
    )
    
    parser.add_argument(
        "--salida", "-o",
        default=DATA_OUTPUTS_DIR,
        help=f"Directorio para guardar reportes (default: {DATA_OUTPUTS_DIR})"
    )
    
    parser.add_argument(
        "--secuencial", "-seq",
        action="store_true",
        help="Ejecutar agentes secuencialmente (por defecto es paralelo)"
    )
    
    parser.add_argument(
        "--silencioso", "-s",
        action="store_true",
        help="Modo silencioso (sin mensajes de progreso)"
    )
    
    args = parser.parse_args()
    
    # Por defecto ejecutar en paralelo, a menos que se especifique --secuencial
    paralelo = not args.secuencial
    
    # Usar directorio de salida especificado o el default
    output_dir = args.salida
    
    # Crear directorio de salida si no existe
    os.makedirs(output_dir, exist_ok=True)
    
    # Inicializar integrador
    integrador = AgenteIntegrador()
    
    verbose = not args.silencioso
    
    if verbose:
        print("\n" + "="*60)
        print("  SISTEMA MULTI-AGENTE DE ANÁLISIS DE ENTREVISTAS UTP")
        print("="*60)
    
    # Determinar archivos a procesar
    if args.archivo:
        # Archivo específico
        if os.path.isabs(args.archivo):
            archivos = [args.archivo]
        else:
            # Buscar en directorio de datos o ruta relativa
            ruta_completa = os.path.join(args.directorio, args.archivo)
            if os.path.exists(ruta_completa):
                archivos = [ruta_completa]
            elif os.path.exists(args.archivo):
                archivos = [args.archivo]
            else:
                print(f"Error: No se encontró el archivo '{args.archivo}'")
                sys.exit(1)
    else:
        # Todos los archivos del directorio
        archivos = listar_transcripciones(args.directorio)
        
        if not archivos:
            print(f"\nNo se encontraron archivos .txt en: {args.directorio}")
            print("Coloca las transcripciones en ese directorio o especifica un archivo.")
            sys.exit(1)
    
    if verbose:
        print(f"\nArchivos a procesar: {len(archivos)}")
        for archivo in archivos:
            print(f"  - {os.path.basename(archivo)}")
    
    # Procesar cada archivo
    reportes_generados = []
    
    for archivo in archivos:
        try:
            rutas_reportes = procesar_transcripcion(
                ruta_archivo=archivo,
                integrador=integrador,
                output_dir=output_dir,
                paralelo=paralelo,
                verbose=verbose
            )
            reportes_generados.append(rutas_reportes)
        except Exception as e:
            print(f"\nError procesando {archivo}: {str(e)}")
            if verbose:
                import traceback
                traceback.print_exc()
    
    # Resumen final
    if verbose:
        print("\n" + "="*60)
        print("  RESUMEN")
        print("="*60)
        print(f"\nEntrevistas procesadas: {len(reportes_generados)}/{len(archivos)}")
        print(f"PDFs generados por entrevista: 2 (reporte.pdf + perfil.pdf)")
        for ruta_detallado, ruta_narrativo in reportes_generados:
            # Extraer nombre de la carpeta padre
            carpeta = os.path.dirname(ruta_detallado)
            nombre = os.path.basename(carpeta)
            print(f"\n  {nombre}/")
            print(f"    ✓ {os.path.basename(ruta_detallado)}")
            print(f"    ✓ {os.path.basename(ruta_narrativo)}")
        print()


if __name__ == "__main__":
    main()
