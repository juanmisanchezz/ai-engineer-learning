# Resumidor con LCEL

Proyecto 4 del máster de AI Engineering (thePower), Módulo 5: LangChain.

*English version below.*

Chat en la terminal que recuerda la conversación y, cuando le pides resumir un texto, lo lee de la carpeta `textos/` y lo resume en 3 viñetas. Funciona en local con Ollama y el modelo llama3.1, sin pagar ninguna API.

## Ejemplo de uso

```
Escribe tu mensaje: Hola, me llamo Juanmi
Hola Juanmi, ¿cómo estás? ¿En qué puedo ayudarte hoy?
Escribe tu mensaje: Resume el texto chocolate
* El chocolate llegó a Europa en el siglo XVI y se tomó como bebida hasta el siglo XIX.
* En 1875, Daniel Peter inventó el chocolate con leche y en 1879, Rodolphe Lindt inventó el conchado.
* Suiza es uno de los países donde más chocolate se consume por persona, con marcas como Lindt, Toblerone y Cailler.
Escribe tu mensaje: ¿Cómo me llamo?
Te llamabas Juanmi.
```

Capturas de dos ejecuciones en [capturas/](capturas/).

## Estructura del proyecto

```
resumidor-lcel/
├── README.md
├── requirements.txt
├── resumidor.py
├── textos/
│   ├── chocolate.txt
│   └── transporte.txt
└── capturas/
    ├── ejecucion-1.png
    └── ejecucion-2.png
```

## Piezas

- **Cadena LCEL:** `prompt | modelo | parser | forzar_3_vinetas`. El prompt le dice que resuma en 3 viñetas, el modelo lo hace, el parser se queda solo con el texto y mi función `forzar_3_vinetas` se asegura de que salen 3 viñetas y nada más
- **Tool `leer_texto`:** abre `textos/<nombre>.txt` y devuelve el texto entero. El modelo la pide cuando le digo "Resume el texto chocolate"
- **Memoria:** un armario (`historiales`) con una libreta por `session_id`. Cada mensaje mío, cada respuesta y cada uso de la tool se apunta en la libreta, y el modelo la lee entera en cada turno. Es lo mismo que el Session ID de la memoria en n8n

## Decisiones

- llama3.1 llamaba a la herramienta en todos los mensajes, incluso con "me llamo Juanmi" intentaba abrir `juanmi.txt`. Por eso decido en el código cuándo usarla: si el mensaje dice "resume" uso el modelo con la tool y si no, el modelo normal
- No uso `RunnableWithMessageHistory` porque guarda el historial él solo y aquí necesito meter también la llamada a la tool y su resultado (`ToolMessage`). Uso la misma libreta (`InMemoryChatMessageHistory`) pero la relleno yo
- Los textos están en archivos `.txt` y no dentro del código, así puedo añadir más textos sin tocar el programa

## Limitaciones

- En la memoria solo se guarda el resumen de 3 viñetas, no el texto entero. Si pregunto por un detalle que no sale en el resumen (por ejemplo "¿Qué es el GA?"), llama3.1 se lo puede inventar
- La memoria está en RAM: al cerrar el programa se pierde la conversación
- Al arrancar salen avisos de que `InMemoryChatMessageHistory` está obsoleto. Es la clase que vimos en clase y funciona

## Ejecución

1. Instalar [Ollama](https://ollama.com) y descargar el modelo:
   ```
   ollama pull llama3.1
   ```
2. Crear el entorno e instalar las librerías:
   ```
   python3 -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt
   ```
3. Ejecutar:
   ```
   python resumidor.py
   ```
   Para salir: `Control + C`

---

## English version

**Resumidor con LCEL** is a terminal chat that remembers the conversation and, when asked to summarise a text, reads it from the `textos/` folder and summarises it in 3 bullet points. It runs locally with Ollama and llama3.1, no paid API. This is project 4 of my AI Engineering master (thePower), module 5: LangChain.

**Pieces**

- LCEL chain: `prompt | modelo | parser | forzar_3_vinetas` (my own function makes sure the output is exactly 3 bullet points)
- Tool `leer_texto`: opens `textos/<name>.txt` and returns its content
- Memory: one `InMemoryChatMessageHistory` per `session_id`; every message, answer and tool call is stored and the model reads the whole history each turn

**Decisions**

- llama3.1 called the tool on every message (even "my name is Juanmi"), so the code decides when to use it: if the message contains "resume", the model with tools is used; otherwise, the plain model
- No `RunnableWithMessageHistory`: the tool call and its `ToolMessage` must also go into the history, so I fill the history myself

**Limitations**

- Only the 3-bullet summary is stored in memory, not the full text, so llama3.1 may make up details that are not in the summary
- Memory lives in RAM and is lost when the program stops

**Run**

```
ollama pull llama3.1
pip install -r requirements.txt
python resumidor.py
```
