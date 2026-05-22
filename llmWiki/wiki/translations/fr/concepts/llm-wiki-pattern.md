---
title: "Modèle LLM Wiki"
type: concept
tags: [gestion-des-connaissances, llm, méthodologie, wiki]
sources: [llm-wiki-101.md, karpathy-llm-wiki-explained.md]
lang: fr
translation_of: "../../../concepts/llm-wiki-pattern"
created: 2026-05-22
updated: 2026-05-22
---

# Modèle LLM Wiki

**Résumé :** Une méthodologie dans laquelle un LLM construit et maintient de manière incrémentale un wiki persistant de fichiers markdown interconnectés, alimenté par une collection de sources curatées. La connaissance s'accumule au fil des ingestions plutôt que d'être redérivée à chaque requête, résolvant le problème d'accumulation inhérent à la [[retrieval-augmented-generation]].

---

## Définition

Le modèle LLM Wiki remplace la récupération par requête par une base de connaissances maintenue par un LLM. Lorsqu'une source est ajoutée, le LLM la lit, en extrait les informations clés et les intègre dans un wiki évolutif — mettant à jour les pages d'entités, révisant les résumés, signalant les contradictions et renforçant les références croisées. Le wiki est un **artefact persistant et cumulatif**.

## Architecture en trois couches

```
Sources brutes  →  Wiki  →  Schéma
(immuables)  (markdown géré par le LLM)  (configuration de l'agent)
```

**Sources brutes :** Articles, papers, images curatés. Jamais modifiés par le LLM. La source de vérité.

**Wiki :** Pages markdown créées et maintenues par le LLM. Concepts, modèles, entités, comparaisons, une vue d'ensemble. Le LLM crée des pages, les met à jour lors de nouvelles ingestions et maintient les références croisées.

**Schéma (CLAUDE.md / AGENTS.md) :** Indique à l'agent comment le wiki est structuré, quelles conventions suivre et quels workflows appliquer. Co-évolue entre l'humain et le LLM. Le fichier de configuration clé qui fait de l'agent un gardien discipliné du wiki.

## Opérations principales

| Opération | Déclencheur | Résultat |
|-----------|-------------|---------|
| **Ingestion** | Nouvelle source ajoutée | Page de résumé + 5–15 pages mises à jour + entrées index/log |
| **Requête** | Question de l'utilisateur | Réponse synthétisée ; les réponses précieuses sont archivées comme nouvelles pages |
| **Lint** | Maintenance périodique | Rapport sur contradictions/orphelins/lacunes ; corrections approuvées appliquées |

## Fichiers d'infrastructure

- **`index.md` :** Catalogue orienté contenu de toutes les pages avec des résumés d'une ligne. Le LLM le lit en premier à chaque requête. Suffisant jusqu'à ~200–300 pages sans embeddings vectoriels.
- **`log.md` :** Enregistrement chronologique, en ajout seulement, de chaque ingestion, requête et passe de lint. Analysable avec `grep "^## \["`.

## Pourquoi ça fonctionne

Le coût de maintenance des wikis traditionnels augmente plus vite que leur valeur — les humains les abandonnent. Les LLMs gèrent les tâches comptables (références croisées, cohérence, mises à jour de l'index) sans fatigue, à un coût marginal quasi nul par ingestion. Le rôle de l'humain se réduit à : curation des sources, formulation de questions, réflexion sur le sens.

## La commande « file back »

Une technique pratique clé : chaque fois qu'une requête produit une réponse précieuse, ajouter cette phrase :

> *« Enregistre cette synthèse comme nouvelle page dans le Wiki et crée un lien. »*

C'est le mécanisme qui permet aux résultats des requêtes de s'accumuler dans le wiki plutôt que de disparaître dans l'historique du chat.

## Cadence de lint

Mensuelle recommandée. Prompt : *« Effectue un bilan complet du dossier Wiki — cherche les liens brisés, les balises en double ou les concepts fréquemment mentionnés mais sans page dédiée. »*

## L'analogie IDE

> *« Ton éditeur de texte est l'IDE. L'IA est le programmeur. Ta connaissance est la base de code. »*

## Outils (optionnels)

- **Obsidian** – parcourir le wiki, vue graphique, export diapositives Marp, requêtes Dataview
- **Obsidian Web Clipper** – convertir des articles web en markdown pour `rawSources/`
- **qmd** – recherche hybride locale (BM25/vecteur) sur markdown quand index.md ne suffit plus
- **Git** – historique des versions, branches, collaboration

## Filiation intellectuelle

Karpathy relie le modèle au **Memex** de Vannevar Bush (1945) — un store de connaissances personnel avec des pistes associatives entre documents. Le problème non résolu de Bush était le coût de maintenance ; les LLMs le résolvent.

## Concepts liés

- [[retrieval-augmented-generation]] — l'approche que ce modèle améliore pour les bases de connaissances personnelles
- [[andrej-karpathy]] — créateur du modèle

## Sources

- [[llm-wiki-101]]
- [[karpathy-llm-wiki-explained]]
