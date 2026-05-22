---
title: "Retrieval-Augmented Generation (RAG)"
type: concept
tags: [rag, retrieval, llm, wissen, architektur]
sources: [llm-wiki-101.md]
lang: de
translation_of: "../../../concepts/retrieval-augmented-generation"
created: 2026-05-22
updated: 2026-05-22
---

# Retrieval-Augmented Generation (RAG)

**Kurzfassung:** RAG verankert LLM-Antworten, indem zur Abfragezeit relevante Dokumentfragmente abgerufen und in das Kontextfenster eingefügt werden. Es ist der vorherrschende Ansatz für Dokumenten-Q&A, hat jedoch einen zentralen Schwachpunkt: Wissen wird bei jeder Anfrage neu abgeleitet – sitzungsübergreifend akkumuliert sich nichts.

---

## Definition

RAG ist eine Technik, die die Generierung eines LLM durch abgerufenen Kontext aus einem externen Korpus ergänzt. Zur Abfragezeit ruft ein Retrieval-System (typischerweise Embedding-basierte Vektorsuche) die relevantesten Fragmente aus einer Dokumentensammlung ab; diese Fragmente werden dem Prompt vorangestellt, und das LLM generiert eine darin verankerte Antwort.

## Funktionsweise

```
Anfrage
  ↓
Anfrage einbetten → Vektorähnlichkeitssuche über indizierte Fragmente
  ↓
Top-k-Fragmente abrufen
  ↓
Prompt = System + abgerufene Fragmente + Anfrage
  ↓
LLM generiert verankerte Antwort
```

## Wichtige Varianten

| Variante | Beschreibung |
|---------|-------------|
| Naives RAG | Einstufiges Abrufen und Generieren |
| HyDE | Hypothetische Antwort generieren, einbetten, ähnliche Fragmente abrufen |
| Re-Ranking | Zweistufig: schnelles Abrufen, dann Cross-Encoder-Reranking |
| Multi-Hop RAG | Iterative Abrufschritte für Fragen mit mehreren Reasoning-Schritten |
| Agentisches RAG | LLM entscheidet während der Generierung, wann und was abzurufen ist |

## Stärken

- Funktioniert auf jedem Korpus ohne Fine-Tuning des LLM
- Wissen kann durch Aktualisierung des Index aktualisiert werden, ohne neu zu trainieren
- Verankerung reduziert Halluzinationen bei Faktenfragen
- Skaliert auf große Dokumentensammlungen mit effizienter Näherungssuche

## Schwächen

- **Keine Akkumulation:** Das LLM leitet Wissen bei jeder Anfrage neu ab; dokumentenübergreifende Synthese muss jedes Mal neu erstellt werden
- **Fragmentgrenzenproblem:** Relevante Informationen können Fragmentgrenzen überschreiten und nur teilweise abgerufen werden
- **Deckeneffekt der Abrufqualität:** Das LLM kann nicht über nicht abgerufene Informationen nachdenken
- **Infrastrukturaufwand:** Erfordert Embedding-Modell, Vektorspeicher und Indexierungspipeline
- **Latenz:** Das Abrufen fügt einen Roundtrip vor der Generierung hinzu

## RAG vs. LLM-Wiki-Muster

| Dimension | RAG | [[llm-wiki-pattern]] |
|-----------|-----|---------------------|
| Wissenskompilierung | Pro Anfrage | Beim Ingest (einmalig) |
| Dokumentenübergreifende Synthese | Jedes Mal neu abgeleitet | Vorgebaut in Wiki-Seiten |
| Widerspruchserkennung | Keine | Beim Ingest gekennzeichnet |
| Infrastruktur | Vektorspeicher + Embeddings | Flache Markdown-Dateien |
| Skalierungsgrenze | Sehr hoch | ~200–300 Seiten vor Bedarf an Suchwerkzeugen |
| Menschlicher Aufwand | Gering (Dokumente hochladen) | Höher (Kuration + Überprüfung) |

Das [[llm-wiki-pattern]] ersetzt RAG nicht generell; es eignet sich besser für **persönliche, kuratierte, aktiv gepflegte** Wissensbasen, bei denen Akkumulation und Synthese wichtiger sind als Skalierung.

## Gängige Implementierungen

- LangChain / LlamaIndex (Python)
- OpenAI Assistants API-Dateisuche
- NotebookLM (Google)
- Perplexity (Web-Maßstab)

## Verwandte Konzepte

- [[llm-wiki-pattern]] — alternative Architektur für persönliche Wissensbasen

## Quellen

- [[llm-wiki-101]]
