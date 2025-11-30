"""
Generador de reportes en LaTeX y compilación a PDF.
"""
import os
import re
import subprocess
from pathlib import Path


# Ruta a pdflatex (MacTeX)
PDFLATEX_PATH = "/Library/TeX/texbin/pdflatex"


def escapar_latex(texto: str) -> str:
    """
    Escapa caracteres especiales de LaTeX.
    """
    if not texto:
        return ""
    
    # Caracteres especiales de LaTeX
    replacements = [
        ('\\', r'\textbackslash{}'),
        ('&', r'\&'),
        ('%', r'\%'),
        ('$', r'\$'),
        ('#', r'\#'),
        ('_', r'\_'),
        ('{', r'\{'),
        ('}', r'\}'),
        ('~', r'\textasciitilde{}'),
        ('^', r'\textasciicircum{}'),
    ]
    
    for old, new in replacements:
        texto = texto.replace(old, new)
    
    return texto


def procesar_formato_en_linea(texto: str) -> str:
    """
    Procesa una línea de texto: primero escapa caracteres especiales,
    luego convierte negritas e itálicas de Markdown a LaTeX.
    
    El orden es importante:
    1. Identificar negritas/itálicas y extraerlas
    2. Escapar el texto normal
    3. Reconstruir con comandos LaTeX
    """
    if not texto:
        return ""
    
    resultado = []
    i = 0
    
    while i < len(texto):
        # Buscar negritas **texto**
        if texto[i:i+2] == '**':
            # Buscar cierre
            cierre = texto.find('**', i+2)
            if cierre != -1:
                contenido = texto[i+2:cierre]
                resultado.append(f'\\textbf{{{escapar_latex(contenido)}}}')
                i = cierre + 2
                continue
        
        # Buscar itálicas *texto* (no precedidas por *)
        if texto[i] == '*' and (i == 0 or texto[i-1] != '*') and (i+1 < len(texto) and texto[i+1] != '*'):
            # Buscar cierre (un solo *)
            cierre = -1
            for j in range(i+1, len(texto)):
                if texto[j] == '*' and (j+1 >= len(texto) or texto[j+1] != '*'):
                    cierre = j
                    break
            if cierre != -1:
                contenido = texto[i+1:cierre]
                resultado.append(f'\\textit{{{escapar_latex(contenido)}}}')
                i = cierre + 1
                continue
        
        # Caracter normal - acumular para escapar después
        # Buscar hasta el próximo * o fin de línea
        inicio = i
        while i < len(texto) and texto[i] != '*':
            i += 1
        resultado.append(escapar_latex(texto[inicio:i]))
    
    return ''.join(resultado)


def markdown_a_latex(markdown: str) -> str:
    """
    Convierte Markdown básico a LaTeX.
    """
    lines = markdown.split('\n')
    latex_lines = []
    in_itemize = False
    
    for line in lines:
        original_line = line
        
        # Saltar líneas vacías
        if not line.strip():
            if in_itemize:
                latex_lines.append(r'\end{itemize}')
                in_itemize = False
            latex_lines.append('')
            continue
        
        # Headers
        if line.startswith('# '):
            if in_itemize:
                latex_lines.append(r'\end{itemize}')
                in_itemize = False
            # Título principal - ya manejado en el template
            continue
        elif line.startswith('### '):
            if in_itemize:
                latex_lines.append(r'\end{itemize}')
                in_itemize = False
            titulo = line[4:].strip()
            # El título ya tiene su propia numeración, usar section* (sin numerar)
            latex_lines.append(f'\\subsection*{{{escapar_latex(titulo)}}}')
            continue
        elif line.startswith('#### '):
            if in_itemize:
                latex_lines.append(r'\end{itemize}')
                in_itemize = False
            titulo = line[5:].strip()
            # Usar subsubsection* sin numeración automática
            latex_lines.append(f'\\subsubsection*{{{escapar_latex(titulo)}}}')
            continue
        elif line.startswith('## '):
            if in_itemize:
                latex_lines.append(r'\end{itemize}')
                in_itemize = False
            titulo = line[3:].strip()
            # Usar section* sin numeración automática
            latex_lines.append(f'\\section*{{{escapar_latex(titulo)}}}')
            continue
        
        # Línea horizontal
        if line.strip() == '---':
            if in_itemize:
                latex_lines.append(r'\end{itemize}')
                in_itemize = False
            latex_lines.append(r'\vspace{0.5em}\hrule\vspace{0.5em}')
            continue
        
        # Listas con viñetas
        if line.strip().startswith('- '):
            if not in_itemize:
                latex_lines.append(r'\begin{itemize}')
                in_itemize = True
            contenido = line.strip()[2:]
            # Primero escapar, luego procesar negritas
            contenido = procesar_formato_en_linea(contenido)
            latex_lines.append(f'  \\item {contenido}')
            continue
        
        # Si estábamos en lista y ya no es item, cerrar
        if in_itemize and not line.strip().startswith('- '):
            latex_lines.append(r'\end{itemize}')
            in_itemize = False
        
        # Procesar formato en línea (negritas, itálicas) con escape correcto
        line = procesar_formato_en_linea(line)
        
        latex_lines.append(line)
    
    # Cerrar itemize si quedó abierto
    if in_itemize:
        latex_lines.append(r'\end{itemize}')
    
    return '\n'.join(latex_lines)


def generar_latex_reporte(contenido_md: str, nombre_entrevistado: str, tipo: str = "detallado") -> str:
    """
    Genera el documento LaTeX completo para un reporte.
    
    Args:
        contenido_md: Contenido en Markdown.
        nombre_entrevistado: Nombre del entrevistado.
        tipo: "detallado" o "narrativo".
        
    Returns:
        Documento LaTeX completo.
    """
    # Convertir contenido
    contenido_latex = markdown_a_latex(contenido_md)
    
    # Configuración según tipo
    if tipo == "narrativo":
        # Perfil narrativo: solo el nombre, sin más encabezados
        portada = r"""
\begin{center}
    {\LARGE\bfseries\color{utpazul} """ + escapar_latex(nombre_entrevistado) + r"""}
\end{center}

\vspace{1em}

"""
    else:
        # Reporte detallado: encabezado completo
        portada = r"""
\begin{center}
    {\LARGE\bfseries\color{utpazul} Reporte Individual de Entrevista}
    
    \vspace{0.5em}
    
    {\large Entrevistado: """ + escapar_latex(nombre_entrevistado) + r"""}
    
    \vspace{0.3em}
    
    {\small Contexto: Entrevista sobre Inteligencia Artificial en la Universidad Tecnológica de Pereira (UTP)}
    
    \vspace{0.3em}
    
    {\small\color{utpgris} Fecha de generación: \today}
\end{center}

\vspace{1em}
\hrule
\vspace{1em}

"""
    
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
\usepackage{hyperref}
\usepackage{fancyhdr}
\usepackage{graphicx}

% Configuración de página
\geometry{
    left=2.5cm,
    right=2.5cm,
    top=2.5cm,
    bottom=2.5cm
}

% Colores institucionales UTP
\definecolor{utpazul}{RGB}{0, 47, 108}
\definecolor{utpgris}{RGB}{88, 89, 91}

% Configuración de hyperref
\hypersetup{
    colorlinks=true,
    linkcolor=utpazul,
    urlcolor=utpazul
}

% Configuración de títulos
\titleformat{\section}
    {\Large\bfseries\color{utpazul}}
    {\thesection.}{0.5em}{}
\titleformat{\subsection}
    {\large\bfseries\color{utpgris}}
    {\thesubsection}{0.5em}{}
\titleformat{\subsubsection}
    {\normalsize\bfseries}
    {\thesubsubsection}{0.5em}{}

% Espaciado
\setlength{\parindent}{0pt}
\setlength{\parskip}{0.8em}

% Configuración de listas
\setlist[itemize]{topsep=0.3em, itemsep=0.2em, parsep=0.2em}

% Encabezado y pie de página
\pagestyle{fancy}
\fancyhf{}
\fancyhead[L]{\small\color{utpgris}Universidad Tecnológica de Pereira}
\fancyhead[R]{\small\color{utpgris}Entrevistas IA}
\fancyfoot[C]{\thepage}
\renewcommand{\headrulewidth}{0.4pt}
\renewcommand{\footrulewidth}{0pt}

\begin{document}

""" + portada + contenido_latex + r"""

\end{document}
"""
    
    return template


def compilar_pdf(ruta_tex: str, output_dir: str) -> str:
    """
    Compila un archivo .tex a PDF usando pdflatex.
    
    Args:
        ruta_tex: Ruta al archivo .tex.
        output_dir: Directorio de salida para el PDF.
        
    Returns:
        Ruta al PDF generado.
    """
    # Ejecutar pdflatex dos veces para resolver referencias
    for _ in range(2):
        result = subprocess.run(
            [PDFLATEX_PATH, 
             "-interaction=nonstopmode",
             "-output-directory", output_dir,
             ruta_tex],
            capture_output=True,
            cwd=output_dir,
            env={**os.environ, 'LC_ALL': 'en_US.UTF-8'}
        )
    
    # Obtener nombre del PDF
    nombre_base = Path(ruta_tex).stem
    ruta_pdf = os.path.join(output_dir, f"{nombre_base}.pdf")
    
    if os.path.exists(ruta_pdf):
        # Limpiar archivos auxiliares (incluyendo .tex)
        for ext in ['.aux', '.log', '.out', '.toc', '.tex']:
            aux_file = os.path.join(output_dir, f"{nombre_base}{ext}")
            if os.path.exists(aux_file):
                os.remove(aux_file)
        return ruta_pdf
    else:
        # Leer el log para ver el error
        log_file = os.path.join(output_dir, f"{nombre_base}.log")
        error_msg = "Error desconocido"
        if os.path.exists(log_file):
            with open(log_file, 'r', encoding='latin-1') as f:
                log_content = f.read()
                # Buscar líneas de error
                for line in log_content.split('\n'):
                    if line.startswith('!') or 'Error' in line:
                        error_msg = line
                        break
        raise RuntimeError(f"Error compilando PDF: {error_msg}")


def guardar_latex_y_pdf(contenido_md: str, nombre_entrevistado: str, 
                         output_dir: str, tipo: str = "detallado") -> str:
    """
    Genera el archivo LaTeX y lo compila a PDF.
    
    Args:
        contenido_md: Contenido en Markdown.
        nombre_entrevistado: Nombre del entrevistado.
        output_dir: Directorio de salida.
        tipo: "detallado" o "narrativo".
        
    Returns:
        Ruta al PDF generado.
    """
    # Generar LaTeX
    latex = generar_latex_reporte(contenido_md, nombre_entrevistado, tipo)
    
    # Nombres de archivo (simplificados sin nombre del entrevistado)
    if tipo == "narrativo":
        nombre_base = "perfil"
    else:
        nombre_base = "reporte"
    
    ruta_tex = os.path.join(output_dir, f"{nombre_base}.tex")
    
    # Guardar .tex
    with open(ruta_tex, 'w', encoding='utf-8') as f:
        f.write(latex)
    
    # Compilar a PDF
    ruta_pdf = compilar_pdf(ruta_tex, output_dir)
    
    return ruta_pdf
