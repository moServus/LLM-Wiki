---
title: "Generazione Aumentata dal Recupero (RAG)"
type: concept
tags: [rag, recupero, llm, conoscenza, architettura]
sources: [llm-wiki-101.md]
lang: it
translation_of: "../../../concepts/retrieval-augmented-generation"
created: 2026-05-22
updated: 2026-05-22
---

# Generazione Aumentata dal Recupero (RAG)

**Sintesi:** Il RAG ancora le risposte degli LLM recuperando frammenti di documenti rilevanti al momento della query e includendoli nella finestra di contesto. È l'approccio dominante per le Q&A su documenti, ma ha una debolezza fondamentale: la conoscenza viene riderivata da zero ad ogni query, senza alcuna accumulazione tra le sessioni.

---

## Definizione

Il RAG è una tecnica che aumenta la generazione di un LLM con contesto recuperato da un corpus esterno. Al momento della query, un sistema di recupero (tipicamente ricerca vettoriale basata su embedding) recupera i frammenti più rilevanti da una collezione di documenti; questi frammenti vengono anteposti al prompt e l'LLM genera una risposta ancorata in essi.

## Come funziona

```
Query
  ↓
Codificare la query → ricerca per similarità vettoriale sui frammenti indicizzati
  ↓
Recuperare i top-k frammenti
  ↓
Prompt = sistema + frammenti recuperati + query
  ↓
L'LLM genera una risposta ancorata
```

## Varianti principali

| Variante | Descrizione |
|---------|-------------|
| RAG naïve | Recupero poi generazione in un singolo passaggio |
| HyDE | Generare una risposta ipotetica, codificarla, recuperare frammenti simili |
| Re-ranking | Due fasi: recupero rapido poi reranking con cross-encoder |
| RAG multi-hop | Fasi di recupero iterative per domande che richiedono più ragionamenti |
| RAG agentivo | L'LLM decide quando e cosa recuperare durante la generazione |

## Punti di forza

- Funziona su qualsiasi corpus senza fine-tuning dell'LLM
- La conoscenza può essere aggiornata aggiornando l'indice senza riaddestrare
- L'ancoraggio riduce le allucinazioni sulle domande fattuali
- Scala su grandi collezioni di documenti con ricerca approssimata efficiente

## Limitazioni

- **Nessuna accumulazione:** l'LLM riscopre la conoscenza da zero ad ogni query; la sintesi multi-documento deve essere rifatta ogni volta
- **Problema dei confini dei frammenti:** le informazioni rilevanti possono attraversare i confini dei frammenti ed essere recuperate solo parzialmente
- **Tetto della qualità di recupero:** l'LLM non può ragionare su informazioni non recuperate
- **Overhead infrastrutturale:** richiede modello di embedding, store vettoriale e pipeline di indicizzazione
- **Latenza:** il recupero aggiunge un round-trip prima della generazione

## RAG vs. Schema LLM Wiki

| Dimensione | RAG | [[llm-wiki-pattern]] |
|-----------|-----|---------------------|
| Compilazione della conoscenza | Per query | All'ingestione (una volta) |
| Sintesi multi-documento | Riderivata ogni volta | Pre-costruita nelle pagine wiki |
| Rilevamento di contraddizioni | Nessuno | Segnalato durante l'ingestione |
| Infrastruttura | Store vettoriale + embedding | File markdown piatti |
| Tetto di scala | Molto alto | ~200–300 pagine prima di necessitare strumenti di ricerca |
| Sforzo umano | Basso (caricare documenti) | Più alto (cura + revisione) |

Lo [[llm-wiki-pattern]] non sostituisce il RAG in generale; è più adatto a basi di conoscenza **personali, curate, attivamente mantenute** dove l'accumulazione e la sintesi contano più della scala.

## Implementazioni comuni

- LangChain / LlamaIndex (Python)
- OpenAI Assistants API file search
- NotebookLM (Google)
- Perplexity (scala web)

## Concetti correlati

- [[llm-wiki-pattern]] — architettura alternativa per basi di conoscenza personali

## Fonti

- [[llm-wiki-101]]
