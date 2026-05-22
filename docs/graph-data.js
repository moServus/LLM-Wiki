// LLM Wiki — Concept Graph Data
// Edit this file to add new nodes and links when you create new wiki pages.
//
// Groups: core | technique | model | tool | paper
// Add nodes: { id, label, group, url, description }
// Add links: { source, target, label }

const graphData = {
  nodes: [
    // ── Core / Foundation ──────────────────────────────────────────────────
    { id: "transformer", label: "Transformer\nArchitecture", group: "core", url: "../wiki/concepts-map.md", description: "The backbone of all modern LLMs — introduced in 'Attention Is All You Need' (2017)" },
    { id: "attention", label: "Attention\nMechanism", group: "core", url: "../wiki/concepts-map.md", description: "Allows the model to focus on relevant parts of the input when generating each token" },
    { id: "embeddings", label: "Embeddings", group: "core", url: "../wiki/concepts-map.md", description: "Dense vector representations that encode meaning in high-dimensional space" },
    { id: "tokenization", label: "Tokenization", group: "core", url: "../wiki/concepts-map.md", description: "How text is broken into tokens (subwords) before being fed to a model" },
    { id: "positional-encoding", label: "Positional\nEncoding", group: "core", url: "../wiki/concepts-map.md", description: "Injects sequence order information into token representations" },
    { id: "pretraining", label: "Pre-training", group: "core", url: "../wiki/concepts-map.md", description: "Large-scale self-supervised learning on internet text via next-token prediction" },

    // ── Techniques ─────────────────────────────────────────────────────────
    { id: "rlhf", label: "RLHF", group: "technique", url: "../wiki/concepts-map.md", description: "Reinforcement Learning from Human Feedback — aligns models to human preferences" },
    { id: "constitutional-ai", label: "Constitutional\nAI", group: "technique", url: "../wiki/concepts-map.md", description: "Anthropic's approach to alignment using a set of principles rather than only human labels" },
    { id: "instruction-tuning", label: "Instruction\nTuning", group: "technique", url: "../wiki/concepts-map.md", description: "Fine-tuning on (instruction, response) pairs to make models follow directions" },
    { id: "fine-tuning", label: "Fine-tuning", group: "technique", url: "../wiki/concepts-map.md", description: "Adapting a pre-trained model to a specific task or domain" },
    { id: "lora", label: "LoRA / QLoRA", group: "technique", url: "../wiki/concepts-map.md", description: "Low-Rank Adaptation — efficient fine-tuning by updating only small adapter matrices" },
    { id: "rag", label: "RAG", group: "technique", url: "../wiki/concepts-map.md", description: "Retrieval-Augmented Generation — combines LLMs with external knowledge retrieval" },
    { id: "chain-of-thought", label: "Chain-of-\nThought", group: "technique", url: "../wiki/concepts-map.md", description: "Prompting technique that elicits step-by-step reasoning to improve accuracy" },
    { id: "few-shot", label: "Few-shot\nPrompting", group: "technique", url: "../wiki/concepts-map.md", description: "Providing examples in the prompt to guide model behavior" },
    { id: "zero-shot", label: "Zero-shot\nPrompting", group: "technique", url: "../wiki/concepts-map.md", description: "Asking the model to perform a task with no examples" },
    { id: "semantic-search", label: "Semantic\nSearch", group: "technique", url: "../wiki/concepts-map.md", description: "Finding documents by meaning rather than keyword matching" },
    { id: "agents", label: "LLM Agents", group: "technique", url: "../wiki/concepts-map.md", description: "LLMs that can take actions, use tools, and plan multi-step tasks" },

    // ── Models ─────────────────────────────────────────────────────────────
    { id: "gpt4", label: "GPT-4\n(OpenAI)", group: "model", url: "../wiki/concepts-map.md", description: "OpenAI's flagship model — multimodal, highly capable" },
    { id: "claude", label: "Claude\n(Anthropic)", group: "model", url: "../wiki/concepts-map.md", description: "Anthropic's LLM family, trained with Constitutional AI" },
    { id: "gemini", label: "Gemini\n(Google)", group: "model", url: "../wiki/concepts-map.md", description: "Google DeepMind's multimodal LLM family" },
    { id: "llama", label: "Llama\n(Meta)", group: "model", url: "../wiki/concepts-map.md", description: "Meta's open-weights LLM — foundation for many community models" },
    { id: "mistral", label: "Mistral /\nMixtral", group: "model", url: "../wiki/concepts-map.md", description: "Efficient open models — Mixtral uses Mixture-of-Experts architecture" },

    // ── Tools ──────────────────────────────────────────────────────────────
    { id: "langchain", label: "LangChain", group: "tool", url: "../wiki/tools-setup.md", description: "Framework for building LLM chains and agents" },
    { id: "llamaindex", label: "LlamaIndex", group: "tool", url: "../wiki/tools-setup.md", description: "Data framework for connecting LLMs with external data sources" },
    { id: "huggingface", label: "Hugging Face", group: "tool", url: "../wiki/tools-setup.md", description: "Model hub and transformers library — the de facto open-source LLM platform" },
    { id: "ollama", label: "Ollama", group: "tool", url: "../wiki/tools-setup.md", description: "Run LLMs locally with a simple CLI" },
    { id: "vector-db", label: "Vector\nDatabases", group: "tool", url: "../wiki/tools-setup.md", description: "Specialized databases for storing and querying embeddings (Pinecone, Chroma, Weaviate)" },

    // ── Papers ─────────────────────────────────────────────────────────────
    { id: "attention-paper", label: "Attention Is\nAll You Need", group: "paper", url: "../wiki/concepts-map.md", description: "Vaswani et al. (2017) — introduced the Transformer architecture" },
    { id: "instructgpt", label: "InstructGPT\n(2022)", group: "paper", url: "../wiki/concepts-map.md", description: "OpenAI paper introducing RLHF for aligning GPT-3" },
  ],

  links: [
    // Foundation
    { source: "attention-paper", target: "transformer", label: "introduced" },
    { source: "transformer", target: "attention", label: "uses" },
    { source: "transformer", target: "embeddings", label: "uses" },
    { source: "transformer", target: "tokenization", label: "requires" },
    { source: "transformer", target: "positional-encoding", label: "uses" },
    { source: "transformer", target: "pretraining", label: "trained via" },

    // Training & Alignment
    { source: "pretraining", target: "fine-tuning", label: "precedes" },
    { source: "pretraining", target: "rlhf", label: "precedes" },
    { source: "instructgpt", target: "rlhf", label: "introduced" },
    { source: "rlhf", target: "instruction-tuning", label: "produces" },
    { source: "constitutional-ai", target: "rlhf", label: "alternative to" },
    { source: "fine-tuning", target: "lora", label: "made efficient by" },

    // Models ← Techniques
    { source: "gpt4", target: "rlhf", label: "trained with" },
    { source: "claude", target: "constitutional-ai", label: "trained with" },
    { source: "llama", target: "pretraining", label: "uses" },
    { source: "mistral", target: "llama", label: "builds on" },
    { source: "llama", target: "fine-tuning", label: "enables" },

    // RAG cluster
    { source: "rag", target: "embeddings", label: "uses" },
    { source: "rag", target: "semantic-search", label: "uses" },
    { source: "rag", target: "vector-db", label: "stores in" },
    { source: "semantic-search", target: "embeddings", label: "uses" },

    // Prompting cluster
    { source: "chain-of-thought", target: "few-shot", label: "variant of" },
    { source: "few-shot", target: "zero-shot", label: "contrast" },
    { source: "agents", target: "chain-of-thought", label: "uses" },
    { source: "agents", target: "langchain", label: "built with" },

    // Tools
    { source: "langchain", target: "rag", label: "implements" },
    { source: "llamaindex", target: "rag", label: "specializes in" },
    { source: "llamaindex", target: "vector-db", label: "integrates" },
    { source: "huggingface", target: "llama", label: "hosts" },
    { source: "huggingface", target: "mistral", label: "hosts" },
    { source: "ollama", target: "llama", label: "runs locally" },
    { source: "vector-db", target: "embeddings", label: "indexes" },
  ]
};
