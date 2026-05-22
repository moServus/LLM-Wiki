---
title: "Génération Augmentée par Récupération (RAG)"
type: concept
tags: [rag, récupération, llm, connaissance, architecture]
sources: [llm-wiki-101.md]
lang: fr
translation_of: "../../../concepts/retrieval-augmented-generation"
created: 2026-05-22
updated: 2026-05-22
---

# Génération Augmentée par Récupération (RAG)

**Résumé :** Le RAG ancre les réponses des LLM en récupérant des fragments de documents pertinents au moment de la requête et en les incluant dans la fenêtre de contexte. C'est l'approche dominante pour les Q&R sur documents, mais elle présente une faiblesse majeure : la connaissance est redérivée à partir de zéro à chaque requête, sans accumulation entre les sessions.

---

## Définition

Le RAG est une technique qui augmente la génération d'un LLM avec un contexte récupéré depuis un corpus externe. Au moment de la requête, un système de récupération (typiquement une recherche vectorielle basée sur des embeddings) récupère les fragments les plus pertinents d'une collection de documents ; ces fragments sont ajoutés au début du prompt, et le LLM génère une réponse ancrée dans ceux-ci.

## Fonctionnement

```
Requête
  ↓
Encoder la requête → recherche par similarité vectorielle sur les fragments indexés
  ↓
Récupérer les top-k fragments
  ↓
Prompt = système + fragments récupérés + requête
  ↓
Le LLM génère une réponse ancrée
```

## Variantes principales

| Variante | Description |
|---------|-------------|
| RAG naïf | Récupération puis génération en une seule étape |
| HyDE | Générer une réponse hypothétique, l'encoder, récupérer des fragments similaires |
| Re-ranking | Deux étapes : récupération rapide puis reranking par cross-encoder |
| RAG multi-hop | Étapes de récupération itératives pour les questions nécessitant plusieurs raisonnements |
| RAG agentique | Le LLM décide quand et quoi récupérer pendant la génération |

## Points forts

- Fonctionne sur n'importe quel corpus sans fine-tuning du LLM
- La connaissance peut être mise à jour en mettant à jour l'index sans réentraînement
- L'ancrage réduit les hallucinations sur les questions factuelles
- Passe à l'échelle sur de grandes collections de documents avec une recherche approximative efficace

## Limites

- **Pas d'accumulation :** le LLM redécouvre la connaissance à partir de zéro à chaque requête ; la synthèse multi-documents doit être refaite à chaque fois
- **Problème de frontières de fragments :** les informations pertinentes peuvent chevaucher les frontières de fragments et n'être que partiellement récupérées
- **Plafond de qualité de récupération :** le LLM ne peut pas raisonner sur des informations non récupérées
- **Surcharge d'infrastructure :** nécessite un modèle d'embedding, un store vectoriel et un pipeline d'indexation
- **Latence :** la récupération ajoute un aller-retour avant la génération

## RAG vs. Modèle LLM Wiki

| Dimension | RAG | [[llm-wiki-pattern]] |
|-----------|-----|---------------------|
| Compilation des connaissances | Par requête | À l'ingestion (une fois) |
| Synthèse multi-documents | Redérivée à chaque fois | Pré-construite dans les pages wiki |
| Détection de contradictions | Aucune | Signalée lors de l'ingestion |
| Infrastructure | Store vectoriel + embeddings | Fichiers markdown plats |
| Plafond d'échelle | Très élevé | ~200–300 pages avant besoin d'outils de recherche |
| Effort humain | Faible (uploader des docs) | Plus élevé (curation + révision) |

Le [[llm-wiki-pattern]] ne remplace pas le RAG en général ; il est mieux adapté aux bases de connaissances **personnelles, curatées, activement maintenues** où l'accumulation et la synthèse importent plus que l'échelle.

## Implémentations courantes

- LangChain / LlamaIndex (Python)
- OpenAI Assistants API file search
- NotebookLM (Google)
- Perplexity (échelle web)

## Concepts liés

- [[llm-wiki-pattern]] — architecture alternative pour les bases de connaissances personnelles

## Sources

- [[llm-wiki-101]]
