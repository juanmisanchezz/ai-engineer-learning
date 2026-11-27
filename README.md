# AI Engineer — learning log

Exercises and projects from my AI Engineering studies (started September 2026). Small exercises live here grouped by module; bigger projects get their own repository and are linked from this index.

| # | Module | Content | Status |
|---|--------|---------|--------|
| 01 | [Python basics](01-python-basics/) | Variables and data types, functions, classes, general review (Jupyter notebooks) | ✅ Done |
| 02 | [Model selection](02-model-selection/) | Project 1: choosing an LLM for an online tea shop chatbot. 3 models tested on OpenRouter (PDF report) | ✅ Done |
| 03 | [Prompt engineering](03-prompt-engineering/) | Project 2: production system prompt with XML, few shot and security rules, tested against prompt injection (PDF report) | ✅ Done |
| 04 | [Architecture](04-architecture/) | Project 3: layered architecture (Presentation, Application, Domain, Infrastructure) for the tea shop chatbot, with folder structure and design decisions | ✅ Done |
| 05 | [LangChain](05-langchain/) | Project 4: terminal chat with LCEL that summarises texts in 3 bullet points, with a tool (`leer_texto`) and memory per `session_id`. Runs locally with Ollama + llama3.1 | ✅ Done |
| 06 | [LangGraph](https://github.com/juanmisanchezz/asistente-hotel-langgraph) | Project 5: hotel front-desk assistant built with LangGraph. Decides between answering or using 2 read-only tools, persistent memory per `thread_id` (SQLite), max. 2 tool calls per turn, controlled failures and offline tests. Own repository | ✅ Done |
| 07 | [Observability](https://github.com/juanmisanchezz/asistente-hotel-observabilidad) | Project 6: the project 5 assistant traced in Langfuse and LangSmith at the same time, two prompt versions stored in both platforms, v1 vs v2 compared on 10 held-out questions (tokens, latency, cost), a forced tool failure and delay located in the traces, and email/secret masking. Own repository | ✅ Done |
| 08 | [Open-source models](https://github.com/juanmisanchezz/clasificador-incidencias-hotel) | Project 7: hotel incident classifier with Qwen3-0.6B returning strict JSON (category, priority, reply). Instructions vs few-shot vs LoRA fine-tuning on 240 synthetic examples, trained in 12 min on a MacBook Air M4: 6 → 14 → 22 out of 30 on the test set. Adapter published on [Hugging Face](https://huggingface.co/juanmisanchezz/clasificador-incidencias-hotel-lora). Own repository | ✅ Done |
| 09 | [Closed-source models](https://github.com/juanmisanchezz/clasificador-hotel-gemini-claude) | Project 8: the same hotel incident classifier with closed models. Real fine-tuning of Gemini 3.1 Flash-Lite on Google Cloud (2 epochs, €0.42 checked on the bill) compared with Claude Haiku 4.5 and the three Qwen setups on the same 30 test cases, with latency, tokens and cost per 1,000 messages: Gemini base 26, tuned 27, Claude 23 out of 30. Own repository | ✅ Done |
| 10 | [Vector databases](https://github.com/juanmisanchezz/buscador-frases-pgvector) | Project 9: semantic search over short sentences from two hotels stored in PostgreSQL with pgvector (Neon). Local multilingual embeddings (384 dimensions), cosine distance with an HNSW index and every query filtered by `tenant_id`, so one hotel never sees the other's data. Own repository | ✅ Done |
| 11 | [RAG](https://github.com/juanmisanchezz/rag-hotel) | Project 10: minimal RAG over 3 documents of a fictional hotel. Chunking with LangChain, chunks and embeddings stored in pgvector, top 3 retrieved by cosine distance and passed to llama3.1 running locally with Ollama. Answers only from the documents and says "No lo sé." when the answer is not there. Own repository | ✅ Done |
| 12 | [Advanced RAG](https://github.com/juanmisanchezz/rag-hotel-reranker) | Project 11: the hotel RAG from project 10 with one improvement, a cross-encoder reranker (bge-reranker-v2-m3) that reorders the pgvector candidates. Same question before and after: pgvector alone picks the wrong chunk and answers "No lo sé."; with the reranker it picks the right one and answers correctly. Measured with RAGAS faithfulness, using llama3.1 as a local judge: 0.0 → 1.0. Own repository | ✅ Done |
| 13 | Next project | — | ⏳ Coming soon |

## Structure

```
ai-engineer-learning/
├── 01-python-basics/     # one notebook per topic
├── 02-model-selection/   # project 1: LLM selection report (PDF)
├── 03-prompt-engineering/ # project 2: prompt engineering + prompt injection (PDF)
├── 04-architecture/      # project 3: layered project structure + README with decisions
├── 05-langchain/         # project 4: LCEL summariser chat with tool + memory (Ollama)
├── _template/            # README template for every new project
└── README.md             # this index
```

## How I work

Each project folder has a short README with the problem, the approach, how to run it and what I learned — see [`_template/`](_template/).

Notebooks are written in Spanish (my native language); READMEs are in English.

## Related

Production work (LLM agents, automation, databases): [ai-agents-case-studies](https://github.com/juanmisanchezz/ai-agents-case-studies)
