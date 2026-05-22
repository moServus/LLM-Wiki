---
title: "Generación Aumentada por Recuperación (RAG)"
type: concept
tags: [rag, recuperación, llm, conocimiento, arquitectura]
sources: [llm-wiki-101.md]
lang: es
translation_of: "../../../concepts/retrieval-augmented-generation"
created: 2026-05-22
updated: 2026-05-22
---

# Generación Aumentada por Recuperación (RAG)

**Resumen:** El RAG fundamenta las respuestas de los LLM recuperando fragmentos de documentos relevantes en el momento de la consulta e incluyéndolos en la ventana de contexto. Es el enfoque dominante para Q&A sobre documentos, pero tiene una debilidad clave: el conocimiento se rederiva desde cero en cada consulta, sin acumulación entre sesiones.

---

## Definición

El RAG es una técnica que aumenta la generación de un LLM con contexto recuperado de un corpus externo. En el momento de la consulta, un sistema de recuperación (típicamente búsqueda vectorial basada en embeddings) recupera los fragmentos más relevantes de una colección de documentos; estos fragmentos se anteponen al prompt y el LLM genera una respuesta fundamentada en ellos.

## Cómo funciona

```
Consulta
  ↓
Codificar la consulta → búsqueda por similitud vectorial sobre fragmentos indexados
  ↓
Recuperar los top-k fragmentos
  ↓
Prompt = sistema + fragmentos recuperados + consulta
  ↓
El LLM genera una respuesta fundamentada
```

## Variantes principales

| Variante | Descripción |
|---------|-------------|
| RAG naïve | Recuperación luego generación en un solo paso |
| HyDE | Generar una respuesta hipotética, codificarla, recuperar fragmentos similares |
| Re-ranking | Dos etapas: recuperación rápida luego re-ranking con cross-encoder |
| RAG multi-hop | Pasos de recuperación iterativos para preguntas que requieren múltiples razonamientos |
| RAG agéntico | El LLM decide cuándo y qué recuperar durante la generación |

## Fortalezas

- Funciona en cualquier corpus sin fine-tuning del LLM
- El conocimiento puede actualizarse actualizando el índice sin reentrenar
- El anclaje reduce las alucinaciones en preguntas factuales
- Escala en grandes colecciones de documentos con búsqueda aproximada eficiente

## Limitaciones

- **Sin acumulación:** el LLM redescubre el conocimiento desde cero en cada consulta; la síntesis multi-documento debe rehacerse cada vez
- **Problema de límites de fragmentos:** la información relevante puede cruzar límites de fragmentos y recuperarse solo parcialmente
- **Techo de calidad de recuperación:** el LLM no puede razonar sobre información no recuperada
- **Sobrecarga de infraestructura:** requiere modelo de embedding, store vectorial y pipeline de indexación
- **Latencia:** la recuperación añade un viaje de ida y vuelta antes de la generación

## RAG vs. Patrón LLM Wiki

| Dimensión | RAG | [[llm-wiki-pattern]] |
|-----------|-----|---------------------|
| Compilación del conocimiento | Por consulta | En la ingestión (una vez) |
| Síntesis multi-documento | Rederivada cada vez | Pre-construida en páginas wiki |
| Detección de contradicciones | Ninguna | Señalada durante la ingestión |
| Infraestructura | Store vectorial + embeddings | Archivos markdown planos |
| Techo de escala | Muy alto | ~200–300 páginas antes de necesitar herramientas de búsqueda |
| Esfuerzo humano | Bajo (subir documentos) | Mayor (curación + revisión) |

El [[llm-wiki-pattern]] no reemplaza el RAG en general; es más adecuado para bases de conocimiento **personales, curadas, mantenidas activamente** donde la acumulación y la síntesis importan más que la escala.

## Implementaciones comunes

- LangChain / LlamaIndex (Python)
- OpenAI Assistants API file search
- NotebookLM (Google)
- Perplexity (escala web)

## Conceptos relacionados

- [[llm-wiki-pattern]] — arquitectura alternativa para bases de conocimiento personales

## Fuentes

- [[llm-wiki-101]]
