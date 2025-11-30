# Sistema Multi-Agente para Análisis de Entrevistas UTP

Sistema de procesamiento de entrevistas transcritas sobre inteligencia artificial (IA) en la Universidad Tecnológica de Pereira (UTP). Utiliza 7 agentes especializados para extraer y organizar información de las transcripciones en reportes estructurados.

## 🎯 Objetivo

A partir de transcripciones de entrevistas, el sistema genera reportes individuales estructurados en 7 secciones, donde cada agente se encarga de una parte específica:

1. **Datos básicos del entrevistado**
2. **Resumen general de la entrevista**
3. **Experiencia técnica y práctica aplicada**
4. **Desarrollo, innovación y transferencia tecnológica**
5. **Colaboración, liderazgo y visión estratégica**
6. **Motivación y proyección profesional**
7. **Hallazgos clave**

## 📋 Reglas del Sistema

- Trabaja **ÚNICAMENTE** con información explícita en la transcripción
- No inventa, infiere ni completa datos no mencionados
- Si una información no aparece, escribe: "No mencionado"
- Mantiene tono formal, claro y orientado a informes

## 🚀 Instalación

```bash
# Clonar o descargar el proyecto
cd entrevistas

# Crear entorno virtual (recomendado)
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate

# Instalar dependencias
pip install -r requirements.txt

# Configurar API key de OpenAI
cp .env.example .env
# Editar .env y agregar tu OPENAI_API_KEY
```

## ⚙️ Configuración

Edita el archivo `.env` con tu configuración:

```env
OPENAI_API_KEY=sk-tu-api-key-aqui
OPENAI_MODEL=gpt-4o-mini    # O gpt-4o para mejor calidad
MAX_TOKENS=4000
TEMPERATURE=0.3
```

## 📁 Estructura del Proyecto

```
entrevistas/
├── README.md
├── requirements.txt
├── .env.example
├── .gitignore
│
├── data/
│   ├── raw/                    # Transcripciones originales (.txt)
│   └── outputs/                # Reportes generados (.md)
│
└── src/
    ├── main.py                 # Script principal
    ├── config.py               # Configuración del sistema
    │
    ├── agents/
    │   ├── base_agent.py       # Clase base para agentes
    │   ├── agente_datos_basicos.py
    │   ├── agente_resumen_general.py
    │   ├── agente_experiencia_tecnica.py
    │   ├── agente_desarrollo_innovacion.py
    │   ├── agente_colaboracion_liderazgo.py
    │   ├── agente_motivacion_proyeccion.py
    │   ├── agente_hallazgos_clave.py
    │   └── agente_integrador.py    # Orquestador
    │
    └── utils/
        └── file_loader.py      # Utilidades de carga de archivos
```

## 🎮 Uso

### Procesar todas las transcripciones

```bash
cd src
python main.py
```

### Procesar un archivo específico

```bash
python main.py "nombre_archivo.txt"
```

### Modo paralelo (más rápido)

```bash
python main.py --paralelo
```

### Ver todas las opciones

```bash
python main.py --help
```

## 📊 Ejemplo de Salida

El sistema genera un archivo Markdown con estructura:

```markdown
# Reporte Individual de Entrevista

**Entrevistado:** Ana María López Echeverry
**Contexto:** Entrevista sobre IA en la UTP
**Fecha de generación:** 29 de noviembre de 2025

---

## I. Datos básicos del entrevistado
...

## II. Resumen general de la entrevista
...

[... secciones III-VII ...]

---
*Reporte generado automáticamente...*
```

## 🤖 Arquitectura de Agentes

```
┌─────────────────────────────────────────────────────────────┐
│                    AGENTE INTEGRADOR                        │
│                 (Orquesta y concatena)                      │
└─────────────────────────────────────────────────────────────┘
                            │
        ┌───────────────────┼───────────────────┐
        │                   │                   │
        ▼                   ▼                   ▼
┌───────────────┐   ┌───────────────┐   ┌───────────────┐
│ Agente Datos  │   │ Agente        │   │ Agente        │
│ Básicos       │   │ Resumen       │   │ Experiencia   │
│ (Sección I)   │   │ (Sección II)  │   │ (Sección III) │
└───────────────┘   └───────────────┘   └───────────────┘
        │                   │                   │
        ▼                   ▼                   ▼
┌───────────────┐   ┌───────────────┐   ┌───────────────┐
│ Agente        │   │ Agente        │   │ Agente        │
│ Innovación    │   │ Colaboración  │   │ Motivación    │
│ (Sección IV)  │   │ (Sección V)   │   │ (Sección VI)  │
└───────────────┘   └───────────────┘   └───────────────┘
                            │
                            ▼
                    ┌───────────────┐
                    │ Agente        │
                    │ Hallazgos     │
                    │ (Sección VII) │
                    └───────────────┘
```

## 📝 Notas

- Las transcripciones deben estar en formato `.txt`
- El nombre del archivo se usa para identificar al entrevistado
- Los reportes se guardan en `data/outputs/` como archivos Markdown

## 🔧 Personalización

Para modificar el comportamiento de un agente, edita su archivo correspondiente en `src/agents/`. Cada agente define:

- `nombre_seccion`: Título de la sección
- `prompt_sistema`: Rol del agente
- `instrucciones_extraccion`: Qué información extraer y cómo formatearla

## 📄 Licencia

Proyecto desarrollado para la Universidad Tecnológica de Pereira (UTP).
