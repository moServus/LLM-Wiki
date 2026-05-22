---
title: "Schema LLM Wiki"
type: concept
tags: [gestione-della-conoscenza, llm, metodologia, wiki]
sources: [llm-wiki-101.md, karpathy-llm-wiki-explained.md]
lang: it
translation_of: "../../../concepts/llm-wiki-pattern"
created: 2026-05-22
updated: 2026-05-22
---

# Schema LLM Wiki

**Sintesi:** Una metodologia in cui un LLM costruisce e mantiene in modo incrementale un wiki persistente di file markdown interconnessi, alimentato da una raccolta curata di fonti. La conoscenza si accumula attraverso le ingestioni piuttosto che essere riderivata ad ogni query, risolvendo il problema di accumulo insito nella [[retrieval-augmented-generation]].

---

## Definizione

Lo schema LLM Wiki sostituisce il recupero per query con una base di conoscenza mantenuta da un LLM. Quando viene aggiunta una fonte, il LLM la legge, estrae le informazioni chiave e le integra in un wiki in evoluzione — aggiornando le pagine delle entità, revisionando i riassunti, segnalando le contraddizioni e rafforzando i riferimenti incrociati. Il wiki è un **artefatto persistente e cumulativo**.

## Architettura a tre livelli

```
Fonti grezze  →  Wiki  →  Schema
(immutabili)  (markdown gestito dall'LLM)  (configurazione agente)
```

**Fonti grezze:** Articoli, paper, immagini curati. Mai modificati dall'LLM. La fonte di verità primaria.

**Wiki:** Pagine markdown create e mantenute dall'LLM. Concetti, modelli, entità, confronti, una panoramica. L'LLM crea pagine, le aggiorna a nuove ingestioni e mantiene i riferimenti incrociati.

**Schema (CLAUDE.md / AGENTS.md):** Indica all'agente come è strutturato il wiki, quali convenzioni seguire e quali workflow applicare. Co-evolve tra essere umano e LLM. Il file di configurazione chiave che trasforma l'agente in un custode disciplinato del wiki.

## Operazioni principali

| Operazione | Trigger | Output |
|-----------|---------|--------|
| **Ingestione** | Nuova fonte aggiunta | Pagina riassuntiva + 5–15 pagine aggiornate + voci indice/log |
| **Query** | Domanda dell'utente | Risposta sintetizzata; risposte preziose archiviate come nuove pagine |
| **Lint** | Manutenzione periodica | Report su contraddizioni/orfani/lacune; correzioni approvate applicate |

## File di infrastruttura

- **`index.md`:** Catalogo orientato al contenuto di tutte le pagine con riassunti di una riga. L'LLM lo legge per primo ad ogni query. Sufficiente fino a ~200–300 pagine senza embedding vettoriali.
- **`log.md`:** Registro cronologico solo in aggiunta di ogni ingestione, query e passata di lint. Analizzabile con `grep "^## \["`.

## Perché funziona

Il costo di manutenzione dei wiki tradizionali cresce più velocemente del loro valore — gli esseri umani li abbandonano. Gli LLM gestiscono i compiti contabili (riferimenti incrociati, coerenza, aggiornamenti dell'indice) senza affaticamento, a costo marginale quasi nullo per ingestione. Il ruolo dell'essere umano si riduce a: curare le fonti, fare domande, riflettere sul significato.

## Il comando «file back»

Una tecnica pratica chiave: ogni volta che una query produce una risposta preziosa, aggiungere questa frase:

> *«Salva questa sintesi come nuova pagina nel Wiki e collegala.»*

Questo è il meccanismo che fa accumulare i risultati delle query nel wiki invece di scomparire nella cronologia della chat.

## Cadenza lint

Mensile raccomandata. Prompt: *«Esegui un controllo completo della cartella Wiki — cerca link interrotti, tag duplicati o concetti menzionati frequentemente ma privi di una propria pagina dedicata.»*

## L'analogia IDE

> *«Il tuo editor di testo è l'IDE. L'IA è il programmatore. La tua conoscenza è il codice sorgente.»*

## Strumenti (opzionali)

- **Obsidian** – sfogliare il wiki, vista grafico, export diapositive Marp, query Dataview
- **Obsidian Web Clipper** – convertire articoli web in markdown per `rawSources/`
- **qmd** – ricerca ibrida locale (BM25/vettore) su markdown quando index.md non è più sufficiente
- **Git** – cronologia versioni, branch, collaborazione

## Filiazione intellettuale

Karpathy collega il modello al **Memex** di Vannevar Bush (1945) — un archivio personale di conoscenza con percorsi associativi tra documenti. Il problema irrisolto di Bush era il costo di manutenzione; gli LLM lo risolvono.

## Concetti correlati

- [[retrieval-augmented-generation]] — l'approccio che questo schema migliora per le basi di conoscenza personali
- [[andrej-karpathy]] — ideatore dello schema

## Fonti

- [[llm-wiki-101]]
- [[karpathy-llm-wiki-explained]]
