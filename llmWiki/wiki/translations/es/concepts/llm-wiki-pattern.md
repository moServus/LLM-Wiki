---
title: "Patrón LLM Wiki"
type: concept
tags: [gestión-del-conocimiento, llm, metodología, wiki]
sources: [llm-wiki-101.md, karpathy-llm-wiki-explained.md]
lang: es
translation_of: "../../../concepts/llm-wiki-pattern"
created: 2026-05-22
updated: 2026-05-22
---

# Patrón LLM Wiki

**Resumen:** Una metodología en la que un LLM construye y mantiene de forma incremental un wiki persistente de archivos markdown interconectados, alimentado por una colección curada de fuentes. El conocimiento se acumula a través de las ingestiones en lugar de rederiverse en cada consulta, resolviendo el problema de acumulación inherente a la [[retrieval-augmented-generation]].

---

## Definición

El patrón LLM Wiki reemplaza la recuperación por consulta con una base de conocimiento mantenida por un LLM. Cuando se añade una fuente, el LLM la lee, extrae la información clave y la integra en un wiki en evolución — actualizando páginas de entidades, revisando resúmenes, marcando contradicciones y reforzando referencias cruzadas. El wiki es un **artefacto persistente y acumulativo**.

## Arquitectura de tres capas

```
Fuentes brutas  →  Wiki  →  Esquema
(inmutables)  (markdown gestionado por el LLM)  (configuración del agente)
```

**Fuentes brutas:** Artículos, papers, imágenes curados. Nunca modificados por el LLM. La fuente de verdad primaria.

**Wiki:** Páginas markdown creadas y mantenidas por el LLM. Conceptos, modelos, entidades, comparaciones, una visión general. El LLM crea páginas, las actualiza con nuevas ingestiones y mantiene las referencias cruzadas.

**Esquema (CLAUDE.md / AGENTS.md):** Indica al agente cómo está estructurado el wiki, qué convenciones seguir y qué flujos de trabajo aplicar. Co-evoluciona entre el ser humano y el LLM. El archivo de configuración clave que convierte al agente en un guardián disciplinado del wiki.

## Operaciones principales

| Operación | Disparador | Resultado |
|-----------|------------|-----------|
| **Ingestión** | Nueva fuente añadida | Página de resumen + 5–15 páginas actualizadas + entradas de índice/log |
| **Consulta** | Pregunta del usuario | Respuesta sintetizada; respuestas valiosas archivadas como nuevas páginas |
| **Lint** | Mantenimiento periódico | Informe sobre contradicciones/huérfanos/lagunas; correcciones aprobadas aplicadas |

## Archivos de infraestructura

- **`index.md`:** Catálogo orientado al contenido de todas las páginas con resúmenes de una línea. El LLM lo lee primero en cada consulta. Suficiente hasta ~200–300 páginas sin embeddings vectoriales.
- **`log.md`:** Registro cronológico de solo adición de cada ingestión, consulta y pasada de lint. Analizable con `grep "^## \["`.

## Por qué funciona

El coste de mantenimiento de los wikis tradicionales crece más rápido que su valor — los seres humanos los abandonan. Los LLMs gestionan las tareas contables (referencias cruzadas, consistencia, actualizaciones del índice) sin fatiga, a un coste marginal casi nulo por ingestión. El papel del ser humano se reduce a: curar fuentes, hacer preguntas, reflexionar sobre el significado.

## El comando «file back»

Una técnica práctica clave: cada vez que una consulta produce una respuesta valiosa, añadir esta frase:

> *«Guarda esta síntesis como nueva página en el Wiki y enlázala.»*

Este es el mecanismo que hace que los resultados de las consultas se acumulen en el wiki en lugar de desaparecer en el historial del chat.

## Cadencia de lint

Mensual recomendada. Prompt: *«Realiza una revisión completa de la carpeta Wiki — busca enlaces rotos, etiquetas duplicadas o conceptos mencionados frecuentemente pero sin página propia dedicada.»*

## La analogía IDE

> *«Tu editor de texto es el IDE. La IA es el programador. Tu conocimiento es la base de código.»*

## Herramientas (opcionales)

- **Obsidian** – navegar el wiki, vista de grafo, exportación de diapositivas Marp, consultas Dataview
- **Obsidian Web Clipper** – convertir artículos web en markdown para `rawSources/`
- **qmd** – búsqueda híbrida local (BM25/vector) sobre markdown cuando index.md ya no es suficiente
- **Git** – historial de versiones, ramas, colaboración

## Linaje intelectual

Karpathy conecta el patrón con el **Memex** de Vannevar Bush (1945) — un almacén personal de conocimiento con rutas asociativas entre documentos. El problema no resuelto de Bush era el coste de mantenimiento; los LLMs lo resuelven.

## Conceptos relacionados

- [[retrieval-augmented-generation]] — el enfoque que este patrón mejora para bases de conocimiento personales
- [[andrej-karpathy]] — creador del patrón

## Fuentes

- [[llm-wiki-101]]
- [[karpathy-llm-wiki-explained]]
