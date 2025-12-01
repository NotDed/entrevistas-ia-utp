"""
Integrador de agentes consolidadores.

Orquesta la ejecución de múltiples agentes especializados para generar
un reporte consolidado completo sobre capacidades de IA en la UTP.
"""
import sys
import os
import asyncio
from typing import List, Dict, Optional

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from consolidador.agentes import (
    AgenteGruposLabs,
    AgenteHardware,
    AgenteSoftware,
    AgenteFortalezas,
    AgenteLimitaciones,
    AgenteOportunidades,
    AgentePropuestas,
    AgenteConclusiones,
)


class IntegradorConsolidado:
    """
    Orquestador que ejecuta los agentes consolidadores especializados
    y ensambla el reporte final.
    
    Puede ejecutar los agentes en paralelo o secuencialmente.
    """
    
    def __init__(self, verbose: bool = True):
        self.verbose = verbose
        self.agentes = [
            AgenteGruposLabs(),
            AgenteHardware(),
            AgenteSoftware(),
            AgenteFortalezas(),
            AgenteLimitaciones(),
            AgenteOportunidades(),
            AgentePropuestas(),
            AgenteConclusiones(),
        ]
    
    def _log(self, mensaje: str):
        """Imprime mensaje si verbose está activado."""
        if self.verbose:
            print(mensaje)
    
    def procesar(self, transcripciones: str, paralelo: bool = False) -> str:
        """
        Procesa las transcripciones con todos los agentes y genera el reporte.
        
        Args:
            transcripciones: Texto concatenado de todas las entrevistas
            paralelo: Si True, ejecuta agentes en paralelo; si False, secuencial
            
        Returns:
            Reporte consolidado en formato Markdown
        """
        if paralelo:
            return asyncio.run(self._procesar_paralelo(transcripciones))
        else:
            return self._procesar_secuencial(transcripciones)
    
    def _procesar_secuencial(self, transcripciones: str) -> str:
        """Ejecuta los agentes uno por uno."""
        secciones = []
        total = len(self.agentes)
        
        for i, agente in enumerate(self.agentes, 1):
            self._log(f"  [{i}/{total}] Generando: {agente.nombre_seccion}...")
            
            try:
                seccion = agente.ejecutar(transcripciones)
                secciones.append(seccion)
                self._log(f"  [{i}/{total}] ✓ Completado: {agente.nombre_seccion}")
            except Exception as e:
                self._log(f"  [{i}/{total}] ✗ Error en {agente.nombre_seccion}: {e}")
                secciones.append(f"## {agente.nombre_seccion}\n\n*Error al generar esta sección.*\n")
        
        return self._ensamblar_reporte(secciones)
    
    async def _procesar_paralelo(self, transcripciones: str) -> str:
        """Ejecuta los agentes en paralelo."""
        self._log(f"  Ejecutando {len(self.agentes)} agentes en paralelo...")
        
        async def ejecutar_agente(agente, idx: int):
            try:
                resultado = await agente.ejecutar_async(transcripciones)
                self._log(f"  ✓ Completado: {agente.nombre_seccion}")
                return (idx, resultado)
            except Exception as e:
                self._log(f"  ✗ Error en {agente.nombre_seccion}: {e}")
                return (idx, f"## {agente.nombre_seccion}\n\n*Error al generar esta sección.*\n")
        
        tareas = [
            ejecutar_agente(agente, i) 
            for i, agente in enumerate(self.agentes)
        ]
        
        resultados = await asyncio.gather(*tareas)
        
        # Ordenar resultados por índice original
        resultados_ordenados = sorted(resultados, key=lambda x: x[0])
        secciones = [r[1] for r in resultados_ordenados]
        
        self._log(f"  ✓ Todos los agentes completados")
        
        return self._ensamblar_reporte(secciones)
    
    def _ensamblar_reporte(self, secciones: List[str]) -> str:
        """
        Ensambla el reporte final combinando todas las secciones.
        
        Args:
            secciones: Lista de contenidos Markdown de cada sección
            
        Returns:
            Reporte completo en Markdown
        """
        # Encabezado del reporte
        encabezado = """# Reporte Consolidado de Capacidades en Inteligencia Artificial

## Universidad Tecnológica de Pereira

---

Este documento presenta un análisis integral de las capacidades, infraestructura, 
fortalezas, limitaciones y oportunidades en el área de Inteligencia Artificial 
en la Universidad Tecnológica de Pereira, basado en entrevistas con investigadores 
y personal clave de diferentes dependencias.

---

"""
        
        # Combinar secciones con separadores
        contenido = "\n\n---\n\n".join(secciones)
        
        # Pie de página
        pie = """

---

*Documento generado mediante análisis automatizado con agentes de IA especializados.*
"""
        
        return encabezado + contenido + pie
    
    def obtener_agentes(self) -> List[Dict[str, str]]:
        """Retorna información sobre los agentes disponibles."""
        return [
            {
                "nombre": agente.nombre_seccion,
                "clase": agente.__class__.__name__
            }
            for agente in self.agentes
        ]
