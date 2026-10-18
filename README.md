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
| 07 | Next project | — | ⏳ Coming soon |

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
