#!/usr/bin/env python3
"""
Script principal del consolidador de infraestructura IA.

Este script lee todas las transcripciones de entrevistas y genera
un reporte consolidado sobre la infraestructura de IA en la UTP.

Uso:
    python consolidador_main.py                    # Genera reporte consolidado
    python consolidador_main.py --help             # Muestra ayuda
"""
import os
import sys
from pathlib import Path

# Agregar el directorio src al path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from config import DATA_RAW_DIR, DATA_OUTPUTS_DIR
from utils.file_loader import cargar_transcripcion, listar_transcripciones, extraer_nombre_entrevistado
from utils.latex_generator import generar_latex_reporte, compilar_pdf
from agente_consolidador import AgenteConsolidadorInfraestructura


def preparar_transcripciones(directorio: str, verbose: bool = True) -> str:
    """
    Carga y concatena todas las transcripciones con etiquetas.
    
    Args:
        directorio: Directorio con las transcripciones.
        verbose: Si True, muestra progreso.
        
    Returns:
        Texto con todas las transcripciones etiquetadas.
    """
    archivos = listar_transcripciones(directorio)
    
    if not archivos:
        raise ValueError(f"No se encontraron transcripciones en {directorio}")
    
    if verbose:
        print(f"\nCargando {len(archivos)} transcripciones...")
    
    transcripciones = []
    
    for archivo in archivos:
        nombre = extraer_nombre_entrevistado(archivo)
        contenido = cargar_transcripcion(archivo)
        
        if verbose:
            print(f"  ✓ {nombre}")
        
        # Etiquetar cada transcripción
        transcripcion_etiquetada = f"""
{'='*60}
ENTREVISTA: {nombre}
{'='*60}

{contenido}
"""
        transcripciones.append(transcripcion_etiquetada)
    
    return "\n\n".join(transcripciones)


def generar_latex_consolidado(contenido_md: str) -> str:
    """
    Genera el documento LaTeX para el reporte consolidado.
    
    Args:
        contenido_md: Contenido en Markdown.
        
    Returns:
        Documento LaTeX completo.
    """
    from utils.latex_generator import markdown_a_latex, escapar_latex
    
    contenido_latex = markdown_a_latex(contenido_md)
    
    template = r"""\documentclass[11pt,a4paper]{article}

% Paquetes esenciales
\usepackage[utf8]{inputenc}
\usepackage[T1]{fontenc}
\usepackage[spanish]{babel}
\usepackage{geometry}
\usepackage{setspace}
\usepackage{parskip}
\usepackage{titlesec}
\usepackage{enumitem}
\usepackage{xcolor}
\usepackage{fancyhdr}
\usepackage{hyperref}

% Configuración de página
\geometry{
    top=2.5cm,
    bottom=2.5cm,
    left=2.5cm,
    right=2.5cm
}

% Colores UTP
\definecolor{utpverde}{RGB}{0, 128, 0}
\definecolor{utpazul}{RGB}{0, 51, 102}
\definecolor{utpgris}{RGB}{128, 128, 128}

% Configuración de títulos
\titleformat{\section}
    {\Large\bfseries\color{utpazul}}
    {\thesection.}{1em}{}
\titleformat{\subsection}
    {\large\bfseries\color{utpverde}}
    {\thesubsection}{1em}{}
\titleformat{\subsubsection}
    {\normalsize\bfseries}
    {\thesubsubsection}{1em}{}

% Espaciado
\setlength{\parskip}{0.8em}
\setlength{\parindent}{0pt}

% Listas compactas
\setlist[itemize]{topsep=0.3em, itemsep=0.2em, parsep=0.1em}

% Encabezado y pie de página
\pagestyle{fancy}
\fancyhf{}
\fancyhead[L]{\small\color{utpgris}Infraestructura IA - UTP}
\fancyhead[R]{\small\color{utpgris}\thepage}
\renewcommand{\headrulewidth}{0.4pt}

% Hipervínculos
\hypersetup{
    colorlinks=true,
    linkcolor=utpazul,
    urlcolor=utpazul
}

\begin{document}

% Portada
\begin{center}
    {\LARGE\bfseries\color{utpazul} Reporte Consolidado de Infraestructura}
    
    \vspace{0.3em}
    
    {\LARGE\bfseries\color{utpazul} para Inteligencia Artificial}
    
    \vspace{1em}
    
    {\large Universidad Tecnológica de Pereira}
    
    \vspace{0.5em}
    
    {\small\color{utpgris} Generado a partir de 7 entrevistas con investigadores y personal de la UTP}
    
    \vspace{0.3em}
    
    {\small\color{utpgris} Fecha de generación: \today}
\end{center}

\vspace{1em}
\hrule
\vspace{1em}

""" + contenido_latex + r"""

\end{document}
"""
    return template


def main():
    """Función principal del consolidador."""
    print("\n" + "="*60)
    print("  CONSOLIDADOR DE INFRAESTRUCTURA IA - UTP")
    print("="*60)
    
    # Preparar transcripciones
    try:
        transcripciones = preparar_transcripciones(DATA_RAW_DIR)
    except ValueError as e:
        print(f"\nError: {e}")
        sys.exit(1)
    
    # Crear agente consolidador
    print("\n" + "-"*60)
    print("Analizando transcripciones con IA...")
    print("-"*60)
    
    agente = AgenteConsolidadorInfraestructura()
    
    # Generar reporte consolidado
    print("\n  Generando reporte consolidado...")
    print("  (Esto puede tomar varios minutos debido al volumen de texto)")
    
    try:
        reporte_md = agente.ejecutar(transcripciones)
        print("  ✓ Análisis completado")
    except Exception as e:
        print(f"\n  ✗ Error generando reporte: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
    
    # Generar PDF
    print("\n  Generando PDF...")
    
    try:
        # Generar LaTeX
        latex = generar_latex_consolidado(reporte_md)
        
        # Guardar .tex temporal
        ruta_tex = os.path.join(DATA_OUTPUTS_DIR, "reporte_consolidado_infraestructura.tex")
        with open(ruta_tex, 'w', encoding='utf-8') as f:
            f.write(latex)
        
        # Compilar a PDF
        ruta_pdf = compilar_pdf(ruta_tex, DATA_OUTPUTS_DIR)
        
        print(f"  ✓ PDF generado: {ruta_pdf}")
        
    except Exception as e:
        print(f"\n  ✗ Error generando PDF: {e}")
        # Guardar al menos el Markdown
        ruta_md = os.path.join(DATA_OUTPUTS_DIR, "reporte_consolidado_infraestructura.md")
        with open(ruta_md, 'w', encoding='utf-8') as f:
            f.write(reporte_md)
        print(f"  Se guardó el reporte en Markdown: {ruta_md}")
    
    print("\n" + "="*60)
    print("  CONSOLIDACIÓN COMPLETADA")
    print("="*60 + "\n")


if __name__ == "__main__":
    main()
