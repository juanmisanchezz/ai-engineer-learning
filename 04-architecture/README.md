# Matcheando un matcha

Proyecto 3 del máster de AI Engineering (thePower), Módulo 4: arquitectura de sistemas conversacionales. Las respuestas de la práctica están en [docs/respuestas.md](docs/respuestas.md).

*English version below.*

Asistente conversacional que atiende las consultas de los clientes de una tienda de matcha y les recomienda el matcha que mejor encaja con sus preferencias según el stock disponible

## Estructura del proyecto

```
matcheando-un-matcha/
├── README.md
├── docs/
│   ├── respuestas.md
│   ├── estructura-proyecto.png
│   └── ejecucion-main.png
└── src/
    ├── main.py
    ├── presentation/
    │   └── chat_routes.py
    ├── application/
    │   └── recommendation_agent.py
    ├── domain/
    │   └── matcha_rules.py
    └── infrastructure/
        ├── stock_client.py
        └── llm/
            ├── openai_client.py
            └── anthropic_client.py
```

## Organización por capas

- Presentation: Se encarga de la entrada y salida de texto del cliente - Asistente
- Application: Coordina la conversación y decide el siguiente paso
- Domain: Guarda las normas de la tienda
- Infrastructure: Aquí están las conexiones con los sistemas externos como --> **los LLMs y el sistema del stock**

## Decisiones

- Al separar en 4 capas, cada una tiene un único trabajo. Si cambia una regla de la tienda (qué matcha es "suave"), solo toco Domain y si cambio de proveedor de LLM, solo toco Infrastructure, sin romper el chat ni las reglas

- El número de LLMs en el proyecto son 2 por lo que he considerado crear una carpeta y organizarlo ahí. Si algún día hay que cambiar de proveedor solo hay que ir a esa carpeta y modificarlo

## Ejecución

```
python3 src/main.py
```

---

## English version

**Matcheando un matcha** is a conversational assistant for a matcha tea shop: it answers customer questions and recommends the matcha that best fits their preferences, based on the available stock. This is project 3 of my AI Engineering master (thePower), module 4: architecture of conversational systems. No real code yet; the goal is to design the folder structure and separate the layers.

**Layers**

- Presentation: customer input and output (the chat)
- Application: coordinates the conversation and decides the next step
- Domain: the shop's business rules
- Infrastructure: connections to external systems (the LLMs and the stock system)

**Decisions**

- Four layers, one job each: if a shop rule changes, only Domain changes; if the LLM provider changes, only Infrastructure changes.
- `infrastructure/llm/` groups the two LLM clients (OpenAI and Anthropic), so switching provider only touches that folder.

**Run**

```
python3 src/main.py
```
