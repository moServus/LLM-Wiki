---
title: "Wiki ML/IA — Vue d'ensemble"
type: overview
tags: [vue-densemble, synthèse]
lang: fr
translation_of: "../../../overview"
created: 2026-05-22
updated: 2026-05-22
---

# Wiki ML/IA — Vue d'ensemble

**Résumé :** Ce wiki est une synthèse vivante de la recherche en machine learning et IA. Il couvre actuellement la méthodologie de gestion des connaissances pour les wikis basés sur les LLM et les concepts fondamentaux de récupération. Il s'enrichit à chaque source ingérée.

---

## État du wiki

2 sources ingérées (22/05/2026). 5 pages substantielles : 2 concepts, 1 personne, 2 résumés d'articles.

---

## Thèmes principaux

### Gestion des connaissances avec les LLM
La première source établit le [[llm-wiki-pattern]] comme méthodologie pour ce wiki lui-même — une méta-source. La tension centrale documentée est **RAG vs. wiki persistant** : le RAG redérive la connaissance par requête ; le wiki la compile une fois et l'accumule au fil des ingestions. Voir [[retrieval-augmented-generation]] pour l'approche de base que ce modèle améliore.

---

## Questions ouvertes

- À quel nombre de sources/pages la navigation `index.md` seule devient-elle insuffisante, et quels outils de recherche (ex. `qmd`) sont nécessaires ?
- Comment les contradictions entre sources doivent-elles être détectées et résolues en pratique ?
- Quelle granularité de pages fonctionne le mieux — une page par concept, ou des pages thématiques fusionnées ?

---

## Développements récents

- **22/05/2026 :** Wiki initialisé. Deux sources ingérées : article LLM Wiki de Karpathy + tutoriel YouTube (traductions DE/FR/IT/ES). Pages créées pour [[llm-wiki-pattern]], [[retrieval-augmented-generation]], [[andrej-karpathy]]. [[llm-wiki-pattern]] mis à jour avec le détail de la commande file-back et la cadence mensuelle de lint.

---

## Navigation

- [[index]] — catalogue complet des pages
- [[log]] — historique des opérations (anglais uniquement)
