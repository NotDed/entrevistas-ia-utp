#!/usr/bin/env python3
"""
Script principal del consolidador de infraestructura IA.

Este script lee todas las transcripciones de entrevistas, las corrige
y genera un reporte consolidado sobre la infraestructura de IA en la UTP.

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
from agents.agente_correccion import AgenteCorreccion
from agente_consolidador import AgenteConsolidadorInfraestructura


def corregir_transcripcion(transcripcion: str, agente_correccion: AgenteCorreccion) -> str:
    """
    Corrige errores de transcripción usando el agente de corrección.
    
    Args:
        transcripcion: Texto de la transcripción original.
        agente_correccion: Instancia del agente de corrección.
        
    Returns:
        Transcripción corregida.
    """
    resultado = agente_correccion.process(transcripcion)
    
    # El agente devuelve el texto corregido seguido de las correcciones
    # Extraer solo el texto corregido (antes de "---CORRECCIONES---")
    if "---CORRECCIONES---" in resultado:
        texto_corregido = resultado.split("---CORRECCIONES---")[0].strip()
        return texto_corregido
    elif "CORRECCIONES REALIZADAS" in resultado:
        texto_corregido = resultado.split("CORRECCIONES REALIZADAS")[0].strip()
        return texto_corregido
    
    return resultado


def preparar_transcripciones(directorio: str, agente_correccion: AgenteCorreccion = None, verbose: bool = True) -> str:
    """
    Carga, corrige y concatena todas las transcripciones con etiquetas.
    
    Args:
        directorio: Directorio con las transcripciones.
        agente_correccion: Agente para corregir las transcripciones.
        verbose: Si True, muestra progreso.
        
    Returns:
        Texto con todas las transcripciones etiquetadas y corregidas.
    """
    archivos = listar_transcripciones(directorio)
    
    if not archivos:
        raise ValueError(f"No se encontraron transcripciones en {directorio}")
    
    if verbose:
        if agente_correccion:
            print(f"\nCargando y corrigiendo {len(archivos)} transcripciones...")
        else:
            print(f"\nCargando {len(archivos)} transcripciones...")
    
    transcripciones = []
    
    for i, archivo in enumerate(archivos, 1):
        nombre = extraer_nombre_entrevistado(archivo)
        contenido = cargar_transcripcion(archivo)
        
        # Corregir transcripción si hay agente disponible
        if agente_correccion:
            if verbose:
                print(f"  [{i}/{len(archivos)}] Corrigiendo: {nombre}...")
            contenido = corregir_transcripcion(contenido, agente_correccion)
        
        if verbose:
            print(f"  [{i}/{len(archivos)}] ✓ {nombre}")
        
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
\usepackage{microtype}
\usepackage{csquotes}

% Configuración de página
\geometry{
    top=2.5cm,
    bottom=2.5cm,
    left=3cm,
    right=2.5cm
}

% Colores institucionales
\definecolor{utpazul}{RGB}{0, 51, 102}
\definecolor{utpverde}{RGB}{34, 139, 34}
\definecolor{utpgris}{RGB}{80, 80, 80}
\definecolor{acento}{RGB}{70, 130, 180}

% Configuración de títulos - jerarquía clara
\titleformat{\section}
    {\Large\bfseries\color{utpazul}}
    {\thesection.}{0.6em}{}
\titlespacing{\section}{0pt}{2em}{0.8em}

\titleformat{\subsection}
    {\large\bfseries\color{utpazul!85}}
    {}{0em}{}
\titlespacing{\subsection}{0pt}{1.5em}{0.5em}

\titleformat{\subsubsection}
    {\normalsize\bfseries\color{utpgris!90}}
    {}{0em}{}
\titlespacing{\subsubsection}{0.5em}{1em}{0.3em}

\titleformat{\paragraph}[runin]
    {\normalsize\bfseries\color{acento}}
    {}{0em}{}[.]
\titlespacing{\paragraph}{1em}{0.8em}{0.5em}

% Espaciado de párrafos
\setlength{\parskip}{0.6em}
\setlength{\parindent}{0em}

% Configuración de listas - simples y claras
\setlist[itemize]{
    topsep=0.4em,
    itemsep=0.3em,
    parsep=0.1em
}
\setlist[itemize,1]{
    label=\textcolor{utpazul}{$\bullet$},
    leftmargin=1.8em,
    labelsep=0.6em
}
\setlist[itemize,2]{
    label=\textcolor{acento}{$\circ$},
    leftmargin=2.5em,
    labelsep=0.5em
}
\setlist[itemize,3]{
    label=\textcolor{utpgris}{--},
    leftmargin=2em,
    labelsep=0.4em
}

% Encabezado y pie de página
\pagestyle{fancy}
\fancyhf{}
\fancyhead[L]{\small\color{utpgris}\textit{Reporte Consolidado de Infraestructura IA}}
\fancyhead[R]{\small\color{utpgris}\thepage}
\fancyfoot[C]{\small\color{utpgris}Universidad Tecnológica de Pereira}
\renewcommand{\headrulewidth}{0.4pt}
\renewcommand{\footrulewidth}{0.2pt}

% Hipervínculos
\hypersetup{
    colorlinks=true,
    linkcolor=utpazul,
    urlcolor=utpverde
}

% Interlineado
\setstretch{1.15}

\begin{document}

% Portada
\thispagestyle{empty}
\begin{center}
    \vspace*{2cm}
    
    {\Huge\bfseries\color{utpazul} Reporte Consolidado}
    
    \vspace{0.5em}
    
    {\Huge\bfseries\color{utpazul} de Infraestructura}
    
    \vspace{0.5em}
    
    {\Huge\bfseries\color{utpazul} para Inteligencia Artificial}
    
    \vspace{2em}
    
    {\Large Universidad Tecnológica de Pereira}
    
    \vspace{3em}
    
    \hrule
    \vspace{1em}
    
    {\large\color{utpgris} Análisis consolidado a partir de 7 entrevistas}
    
    \vspace{0.5em}
    
    {\large\color{utpgris} con investigadores y personal de la UTP}
    
    \vspace{1em}
    \hrule
    
    \vspace{3em}
    
    {\color{utpgris} Fecha de generación: \today}
\end{center}

\newpage
\setcounter{page}{1}

""" + contenido_latex + r"""

\end{document}
"""
    return template


def main():
    """Función principal del consolidador."""
    import argparse
    
    parser = argparse.ArgumentParser(description="Consolidador de Infraestructura IA")
    parser.add_argument("--sin-correccion", action="store_true", 
                       help="Saltar corrección de transcripciones (más rápido)")
    args = parser.parse_args()
    
    print("\n" + "="*60)
    print("  CONSOLIDADOR DE INFRAESTRUCTURA IA - UTP")
    print("="*60)
    
    agente_correccion = None
    if not args.sin_correccion:
        # Crear agente de corrección
        print("\nInicializando agentes...")
        agente_correccion = AgenteCorreccion()
        print("  ✓ Agente de corrección listo")
    else:
        print("\n[Modo rápido: sin corrección de transcripciones]")
    
    # Preparar transcripciones (cargar y opcionalmente corregir)
    try:
        transcripciones = preparar_transcripciones(
            DATA_RAW_DIR, 
            agente_correccion=agente_correccion
        )
    except ValueError as e:
        print(f"\nError: {e}")
        sys.exit(1)
    
    # Crear agente consolidador
    print("\n" + "-"*60)
    print("Generando reporte consolidado...")
    print("-"*60)
    
    agente = AgenteConsolidadorInfraestructura()
    
    # Generar reporte consolidado
    print("\n  Analizando información de todas las entrevistas...")
    print("  (Esto puede tomar varios minutos)")
    
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
