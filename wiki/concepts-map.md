# Concepts Map

> How the key ideas in the LLM space connect to each other.

The [interactive version](../docs/index.html) of this map is a live D3.js graph — browse it for a visual overview. This page is the human-readable companion.

---

## Core Clusters

### Foundation Layer
The concepts everything else builds on:

- **Transformer Architecture** → the backbone of all modern LLMs
  - → *Attention Mechanism* (how transformers focus on relevant tokens)
  - → *Tokenization* (how text becomes model input)
  - → *Embeddings* (how meaning is encoded as vectors)
  - → *Positional Encoding* (how order is preserved)

### Training & Alignment
How models learn and are made useful:

- **Pre-training** → large-scale next-token prediction on internet text
  - → *RLHF* (Reinforcement Learning from Human Feedback)
  - → *Constitutional AI* (rule-based alignment from Anthropic)
  - → *Instruction Tuning* (training to follow instructions)
  - → *Fine-tuning* → *LoRA*, *QLoRA*, *PEFT* (efficient adaptation)

### Inference & Prompting
How you get good outputs:

- **Prompting** → the interface between user intent and model behavior
  - → *Zero-shot prompting*
  - → *Few-shot prompting*
  - → *Chain-of-thought prompting* (reasoning step by step)
  - → *System prompts* (shaping model persona and constraints)
  - → *Prompt injection* (adversarial misuse)

### Retrieval & Memory
How LLMs access external knowledge:

- **RAG** (Retrieval-Augmented Generation) → combines LLMs with search
  - → *Vector databases* (Pinecone, Weaviate, Chroma)
  - → *Embeddings* (shared with Foundation Layer)
  - → *Semantic search*
  - → *Chunking strategies*

### Models & Providers
Notable LLMs and their relationships:

- **GPT family** (OpenAI) → GPT-3 → InstructGPT → GPT-4
- **Claude family** (Anthropic) → Constitutional AI lineage
- **Gemini family** (Google DeepMind)
- **Llama family** (Meta) → open weights → *Mistral*, *Mixtral*, community forks
- **Smaller / efficient models** → Phi, Gemma, Qwen

### Tools & Frameworks
The software ecosystem:

- **LangChain** → chains and agents framework
- **LlamaIndex** → RAG and data connectors
- **Hugging Face** → model hub, transformers library
- **Ollama** → run models locally
- **LiteLLM** → unified API across providers

---

## Key Relationships

| From | Relationship | To |
|------|-------------|-----|
| Transformer | enables | All modern LLMs |
| Embeddings | powers | RAG, semantic search |
| RLHF | produces | Instruction-following models |
| Fine-tuning | specializes | Pre-trained models |
| Chain-of-thought | improves | Reasoning tasks |
| RAG | extends | LLM knowledge cutoff |
| LoRA | makes efficient | Fine-tuning |
| Constitutional AI | alternative to | RLHF |

---

## How to Extend This Map

When you add a new concept to the wiki, ask yourself:

1. **What does it build on?** (add a "builds on" edge pointing to foundational concepts)
2. **What does it enable?** (add an "enables" edge to downstream concepts)
3. **What does it contrast with?** (add a "contrasts with" edge to alternative approaches)
4. **Which cluster does it belong to?** (assign a group in `graph-data.js`)

---

## Related Pages

- [What is an LLM Wiki?](what-is-llm-wiki.md)
- [Daily Workflow Integration](daily-workflow.md)
- [Tools & Setup Guide](tools-setup.md)
