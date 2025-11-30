"""
Agente integrador que orquesta todos los agentes especializados
y genera el reporte final consolidado.
"""
import asyncio
import re
from datetime import datetime
from typing import Dict, List, Optional

from .base_agent import BaseAgent
from .agente_correccion import AgenteCorreccion
from .agente_datos_basicos import AgenteDatosBasicos
from .agente_resumen_general import AgenteResumenGeneral
from .agente_experiencia_tecnica import AgenteExperienciaTecnica
from .agente_desarrollo_innovacion import AgenteDesarrolloInnovacion
from .agente_colaboracion_liderazgo import AgenteColaboracionLiderazgo
from .agente_motivacion_proyeccion import AgenteMotivacionProyeccion
from .agente_hallazgos_clave import AgenteHallazgosClave
from .agente_narrativo import AgenteNarrativo


def limpiar_markdown(texto: str) -> str:
    """
    Limpia artefactos de markdown que el LLM puede añadir.
    Elimina bloques de código ```markdown``` que envuelven el contenido.
    """
    # Eliminar ```markdown al inicio y ``` al final
    texto = re.sub(r'^```(?:markdown)?\s*\n?', '', texto.strip())
    texto = re.sub(r'\n?```\s*$', '', texto.strip())
    return texto.strip()


class AgenteIntegrador:
    """
    Orquesta la ejecución de todos los agentes especializados y
    concatena sus resultados en un reporte final estructurado.
    """
    
    def __init__(self):
        # Agente de corrección (se ejecuta primero)
        self.agente_correccion = AgenteCorreccion()
        
        # Agentes de análisis en orden
        self.agentes: List[BaseAgent] = [
            AgenteDatosBasicos(),
            AgenteResumenGeneral(),
            AgenteExperienciaTecnica(),
            AgenteDesarrolloInnovacion(),
            AgenteColaboracionLiderazgo(),
            AgenteMotivacionProyeccion(),
            AgenteHallazgosClave(),
        ]
        
        # Agente para reporte narrativo (se ejecuta aparte)
        self.agente_narrativo = AgenteNarrativo()
        
        # Almacenar correcciones para incluir en el reporte
        self.correcciones_realizadas = ""
    
    def generar_encabezado(self, nombre_entrevistado: str) -> str:
        """
        Genera el encabezado del reporte.
        
        Args:
            nombre_entrevistado: Nombre del entrevistado.
            
        Returns:
            Encabezado en formato Markdown.
        """
        fecha_generacion = datetime.now().strftime("%d de %B de %Y")
        
        return f"""# Reporte Individual de Entrevista

**Entrevistado:** {nombre_entrevistado}  
**Contexto:** Entrevista sobre Inteligencia Artificial en la Universidad Tecnológica de Pereira (UTP)  
**Fecha de generación del reporte:** {fecha_generacion}

---

"""
    
    def generar_pie_reporte(self) -> str:
        """
        Genera el pie de página del reporte.
        
        Returns:
            Pie de página en formato Markdown (vacío para presentación oficial).
        """
        return ""
    
    def generar_encabezado_narrativo(self, nombre_entrevistado: str) -> str:
        """
        Genera el encabezado del reporte narrativo (simplificado).
        
        Args:
            nombre_entrevistado: Nombre del entrevistado.
            
        Returns:
            Encabezado en formato Markdown.
        """
        return f"""# {nombre_entrevistado}

"""
    
    def procesar_secuencial(
        self, 
        transcripcion: str, 
        nombre_entrevistado: str,
        verbose: bool = True
    ) -> str:
        """
        Procesa la transcripción ejecutando los agentes secuencialmente.
        
        Args:
            transcripcion: Texto completo de la transcripción.
            nombre_entrevistado: Nombre del entrevistado para el encabezado.
            verbose: Si True, muestra progreso en consola.
            
        Returns:
            Reporte completo en formato Markdown.
        """
        # PASO 0: Corregir errores de transcripción
        if verbose:
            print(f"  [0/8] Corrigiendo errores de transcripción...")
        
        resultado_correccion = self.agente_correccion.process(transcripcion)
        transcripcion_corregida = resultado_correccion['texto_corregido']
        self.correcciones_realizadas = resultado_correccion['correcciones']
        
        if verbose:
            n_correcciones = self.agente_correccion.contar_correcciones(self.correcciones_realizadas)
            print(f"  [0/8] ✓ Corrección completada ({n_correcciones} correcciones)")
        
        # Procesar con los agentes de análisis usando la transcripción corregida
        secciones = []
        total_agentes = len(self.agentes)
        
        for i, agente in enumerate(self.agentes, 1):
            if verbose:
                print(f"  [{i}/{total_agentes}] Procesando: {agente.nombre_seccion}...")
            
            # El agente de datos básicos recibe el nombre del entrevistado
            if isinstance(agente, AgenteDatosBasicos):
                resultado = agente.process(transcripcion_corregida, nombre_entrevistado)
            else:
                resultado = agente.process(transcripcion_corregida)
            
            resultado = limpiar_markdown(resultado)
            secciones.append(resultado)
            
            if verbose:
                print(f"  [{i}/{total_agentes}] ✓ Completado: {agente.nombre_seccion}")
        
        # Generar reporte narrativo
        if verbose:
            print(f"  [Narrativo] Generando reporte narrativo...")
        
        resultado_narrativo = self.agente_narrativo.process(transcripcion_corregida, nombre_entrevistado)
        resultado_narrativo = limpiar_markdown(resultado_narrativo)
        
        if verbose:
            print(f"  [Narrativo] ✓ Reporte narrativo completado")
        
        # Ensamblar reporte detallado
        reporte_detallado = self.generar_encabezado(nombre_entrevistado)
        
        # Agregar nota sobre correcciones si las hay
        resumen_correcciones = self.agente_correccion.obtener_resumen_correcciones(self.correcciones_realizadas)
        if resumen_correcciones:
            reporte_detallado += resumen_correcciones + "\n\n---\n\n"
        
        reporte_detallado += "\n\n".join(secciones)
        reporte_detallado += self.generar_pie_reporte()
        
        # Ensamblar reporte narrativo
        reporte_narrativo = self.generar_encabezado_narrativo(nombre_entrevistado)
        reporte_narrativo += resultado_narrativo
        reporte_narrativo += self.generar_pie_reporte()
        
        return {
            'detallado': reporte_detallado,
            'narrativo': reporte_narrativo
        }
    
    async def procesar_paralelo(
        self, 
        transcripcion: str, 
        nombre_entrevistado: str,
        verbose: bool = True
    ) -> dict:
        """
        Procesa la transcripción ejecutando los agentes en paralelo.
        
        Args:
            transcripcion: Texto completo de la transcripción.
            nombre_entrevistado: Nombre del entrevistado para el encabezado.
            verbose: Si True, muestra progreso en consola.
            
        Returns:
            Diccionario con 'detallado' y 'narrativo'.
        """
        # PASO 0: Corregir errores de transcripción (secuencial, antes del paralelo)
        if verbose:
            print(f"  [0] Corrigiendo errores de transcripción...")
        
        resultado_correccion = self.agente_correccion.process(transcripcion)
        transcripcion_corregida = resultado_correccion['texto_corregido']
        self.correcciones_realizadas = resultado_correccion['correcciones']
        
        if verbose:
            n_correcciones = self.agente_correccion.contar_correcciones(self.correcciones_realizadas)
            print(f"  [0] ✓ Corrección completada ({n_correcciones} correcciones)")
            print(f"  Ejecutando {len(self.agentes) + 1} agentes en paralelo...")
        
        # Crear tareas - el primer agente (datos básicos) recibe el nombre
        async def procesar_agente(agente, idx):
            if isinstance(agente, AgenteDatosBasicos):
                return agente.process(transcripcion_corregida, nombre_entrevistado)
            else:
                return await agente.process_async(transcripcion_corregida)
        
        # Ejecutar todos los agentes en paralelo (incluyendo narrativo)
        tareas = [procesar_agente(agente, i) for i, agente in enumerate(self.agentes)]
        tareas.append(self.agente_narrativo.process_async(transcripcion_corregida, nombre_entrevistado))
        
        resultados = await asyncio.gather(*tareas)
        
        # Separar resultados: los primeros son del reporte detallado, el último es narrativo
        resultados_detallado = [limpiar_markdown(r) for r in resultados[:-1]]
        resultado_narrativo = limpiar_markdown(resultados[-1])
        
        if verbose:
            print(f"  ✓ Todos los agentes completados")
        
        # Construir reporte detallado
        reporte_detallado = self.generar_encabezado(nombre_entrevistado)
        
        # Agregar nota sobre correcciones si las hay
        resumen_correcciones = self.agente_correccion.obtener_resumen_correcciones(self.correcciones_realizadas)
        if resumen_correcciones:
            reporte_detallado += resumen_correcciones + "\n\n---\n\n"
        
        reporte_detallado += "\n\n".join(resultados_detallado)
        reporte_detallado += self.generar_pie_reporte()
        
        # Construir reporte narrativo
        reporte_narrativo = self.generar_encabezado_narrativo(nombre_entrevistado)
        reporte_narrativo += resultado_narrativo
        reporte_narrativo += self.generar_pie_reporte()
        
        return {
            'detallado': reporte_detallado,
            'narrativo': reporte_narrativo
        }
    
    def procesar(
        self, 
        transcripcion: str, 
        nombre_entrevistado: str,
        paralelo: bool = False,
        verbose: bool = True
    ) -> dict:
        """
        Método principal para procesar una transcripción.
        
        Args:
            transcripcion: Texto completo de la transcripción.
            nombre_entrevistado: Nombre del entrevistado para el encabezado.
            paralelo: Si True, ejecuta agentes en paralelo.
            verbose: Si True, muestra progreso en consola.
            
        Returns:
            Diccionario con 'detallado' (reporte estructurado) y 'narrativo' (perfil general).
        """
        if paralelo:
            return asyncio.run(
                self.procesar_paralelo(transcripcion, nombre_entrevistado, verbose)
            )
        else:
            return self.procesar_secuencial(transcripcion, nombre_entrevistado, verbose)
