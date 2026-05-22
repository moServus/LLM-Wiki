---
title: "ML/KI-Wiki — Übersicht"
type: overview
tags: [übersicht, synthese]
lang: de
translation_of: "../../../overview"
created: 2026-05-22
updated: 2026-05-22
---

# ML/KI-Wiki — Übersicht

**Kurzfassung:** Dieses Wiki ist eine lebendige Synthese von Forschung zu maschinellem Lernen und KI. Es behandelt derzeit Wissensmanagemethodologie für LLM-basierte Wikis und grundlegende Retrieval-Konzepte. Es wächst mit jeder eingespeisten Quelle.

---

## Zustand des Wikis

2 Quellen eingespeist (22.05.2026). 5 inhaltliche Seiten: 2 Konzepte, 1 Person, 2 Paper-Zusammenfassungen.

---

## Hauptthemen

### Wissensmanagement mit LLMs
Die erste Quelle etabliert das [[llm-wiki-pattern]] als Methodik für dieses Wiki selbst – eine Meta-Quelle. Die dokumentierte Kernspannung ist **RAG vs. persistentes Wiki**: RAG leitet Wissen pro Anfrage neu ab; das Wiki kompiliert es einmalig und akkumuliert es über Ingests hinweg. Siehe [[retrieval-augmented-generation]] für den Basisansatz, den dieses Muster verbessert.

---

## Offene Fragen

- Ab welcher Quellen-/Seitenanzahl reicht die reine `index.md`-Navigation nicht mehr aus, und welche Suchwerkzeuge (z.B. `qmd`) werden benötigt?
- Wie sollen Widersprüche zwischen Quellen in der Praxis erkannt und aufgelöst werden?
- Welche Seitengranularität funktioniert am besten – eine Seite pro Konzept oder zusammengeführte Themenseiten?

---

## Neueste Entwicklungen

- **22.05.2026:** Wiki initialisiert. Zwei Quellen eingespeist: Karpathy LLM-Wiki-Artikel + YouTube-Walkthrough (DE/FR/IT/ES-Übersetzungen). Seiten für [[llm-wiki-pattern]], [[retrieval-augmented-generation]], [[andrej-karpathy]] erstellt. [[llm-wiki-pattern]] mit File-back-Befehlsdetail und monatlichem Lint-Intervall aktualisiert.

---

## Navigation

- [[index]] — vollständiger Seitenkatalog
- [[log]] — Betriebshistorie (nur Englisch)
