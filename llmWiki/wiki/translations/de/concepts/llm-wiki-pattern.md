---
title: "LLM-Wiki-Muster"
type: concept
tags: [wissensmanagement, llm, methodik, wiki]
sources: [llm-wiki-101.md, karpathy-llm-wiki-explained.md]
lang: de
translation_of: "../../../concepts/llm-wiki-pattern"
created: 2026-05-22
updated: 2026-05-22
---

# LLM-Wiki-Muster

**Kurzfassung:** Eine Methodik, bei der ein LLM schrittweise ein persistentes Wiki aus verlinkten Markdown-Dateien aufbaut und pflegt – gespeist aus einer kuratierten Quellensammlung. Wissen akkumuliert sich über Ingests hinweg, anstatt bei jeder Anfrage neu abgeleitet zu werden. Damit löst es das Akkumulationsproblem, das der [[retrieval-augmented-generation]] innewohnt.

---

## Definition

Das LLM-Wiki-Muster ersetzt die anfragebezogene Suche durch eine LLM-gepflegte Wissensbasis. Wird eine Quelle hinzugefügt, liest das LLM sie, extrahiert Kerninformationen und integriert sie in ein wachsendes Wiki – es aktualisiert Entitätsseiten, überarbeitet Zusammenfassungen, kennzeichnet Widersprüche und festigt Querverweise. Das Wiki ist ein **persistentes, sich akkumulierendes Artefakt**.

## Dreischichtige Architektur

```
Rohdaten  →  Wiki  →  Schema
(unveränderlich)  (LLM-eigene Markdown-Dateien)  (Agenten-Konfiguration)
```

**Rohdaten:** Kuratierte Artikel, Paper, Bilder. Vom LLM nie verändert. Die primäre Wahrheitsquelle.

**Wiki:** Vom LLM erstellte und gepflegte Markdown-Seiten. Konzepte, Modelle, Entitäten, Vergleiche, eine Übersicht. Das LLM erstellt Seiten, aktualisiert sie bei neuen Ingests und pflegt Querverweise.

**Schema (CLAUDE.md / AGENTS.md):** Teilt dem Agenten mit, wie das Wiki strukturiert ist, welche Konventionen zu befolgen sind und welche Workflows anzuwenden sind. Wird gemeinsam von Mensch und LLM weiterentwickelt. Die zentrale Konfigurationsdatei, die den Agenten zu einem disziplinierten Wiki-Betreuer macht.

## Kernoperationen

| Operation | Auslöser | Ergebnis |
|-----------|----------|----------|
| **Ingest** | Neue Quelle hinzugefügt | Zusammenfassungsseite + 5–15 aktualisierte Seiten + Index-/Log-Einträge |
| **Abfrage** | Benutzerfrage | Synthetisierte Antwort; wertvolle Antworten werden als neue Seiten abgelegt |
| **Lint** | Periodische Wartung | Bericht über Widersprüche/Waisen/Lücken; genehmigte Korrekturen werden angewendet |

## Infrastrukturdateien

- **`index.md`:** Inhaltsorientierter Katalog aller Seiten mit einzeiligen Zusammenfassungen. Das LLM liest dies zuerst bei jeder Abfrage. Ausreichend bis ca. 200–300 Seiten ohne Vektorsuche.
- **`log.md`:** Chronologisches, unveränderliches Protokoll jedes Ingests, jeder Abfrage und jedes Lint-Durchlaufs. Analysierbar mit `grep "^## \["`.

## Warum es funktioniert

Der Wartungsaufwand traditioneller Wikis wächst schneller als ihr Nutzen – Menschen geben sie auf. LLMs erledigen Buchführungsaufgaben (Querverweise, Konsistenz, Indexaktualisierungen) ohne Ermüdung und zu nahezu null Grenzkosten pro Ingest. Die Aufgabe des Menschen reduziert sich auf: Quellen kuratieren, Fragen stellen, über Bedeutung nachdenken.

## Der „File-back"-Befehl

Eine wichtige praktische Technik: Wann immer eine Abfrage eine wertvolle Antwort liefert, diesen Satz anhängen:

> *„Speichere diese Synthese als neue Seite im Wiki und verknüpfe sie."*

Dies ist der Mechanismus, der dafür sorgt, dass Abfrageergebnisse im Wiki akkumulieren, anstatt im Chat-Verlauf zu verschwinden.

## Lint-Intervall

Monatlich empfohlen. Prompt: *„Führe eine vollständige Überprüfung des Wiki-Ordners durch – suche nach defekten Links, doppelten Tags oder häufig erwähnten Konzepten ohne eigene Seite."*

## Die IDE-Analogie

> *„Dein Texteditor ist die IDE. Das KI ist der Programmierer. Dein Wissen ist die Codebasis."*

## Werkzeuge (optional)

- **Obsidian** – Wiki durchsuchen, Graphenansicht, Marp-Folienexport, Dataview-Abfragen
- **Obsidian Web Clipper** – Webartikel als Markdown für `rawSources/` konvertieren
- **qmd** – Lokale Hybridsuche (BM25/Vektor) über Markdown, wenn index.md nicht mehr ausreicht
- **Git** – Versionshistorie, Branches, Zusammenarbeit

## Geistiger Ursprung

Karpathy verbindet das Muster mit Vannevar Bushs **Memex** (1945) – ein persönlicher Wissensspeicher mit assoziativen Pfaden zwischen Dokumenten. Bushs ungelöstes Problem war der Wartungsaufwand; LLMs lösen dieses Problem.

## Verwandte Konzepte

- [[retrieval-augmented-generation]] – der Ansatz, den dieses Muster für persönliche Wissensbasen verbessert
- [[andrej-karpathy]] – Urheber des Musters

## Quellen

- [[llm-wiki-101]]
- [[karpathy-llm-wiki-explained]]
