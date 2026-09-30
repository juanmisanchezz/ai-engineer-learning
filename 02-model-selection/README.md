# Proyecto 1: Selección de modelo

Proyecto del Módulo 2 del máster de AI Engineering (thePower). El informe completo está en [proyecto1-seleccion-modelo.pdf](proyecto1-seleccion-modelo.pdf).

*English version below.*

## Caso

Una tienda online de té matcha quiere un asistente en su web para resolver dudas antes de comprar, calcular pedidos, recomendar productos y responder sobre envíos. Solo texto, respuesta en menos de 2 segundos y presupuesto muy limitado.

## Qué hice

1. Análisis previo: qué entra y qué sale, nivel de razonamiento, ventana de contexto y descarte de modelos que no encajan (de imágenes o demasiado caros)
2. Elegí 3 modelos de tamaños distintos: Mistral Small 3, GPT-4o-mini y Llama 3.2 3B
3. Los probé en el chat de OpenRouter con el mismo system prompt, temperatura 0,2 y sin herramientas: 4 preguntas del enunciado y 4 mías (descuento, trampa, idioma y un mensaje largo con ruido)

## Resultados

| Modelo | Aciertos | Tiempo medio | Coste estimado (10.000 consultas/mes) |
|---|---|---|---|
| Mistral Small 3 | 6/8 | ~1,9 s | ~0,22 $ |
| GPT-4o-mini | 7/8 | ~1,9 s | ~0,78 $ |
| Llama 3.2 3B | 3/8 | ~1,5 s | ~0,59 $ |

Precios de OpenRouter a 30/09/2026.

## Decisión

Me quedo con GPT-4o-mini. Acertó los cálculos y fue el más fiel a los datos. Llama falló el descuento e inventó información, y Mistral fue más lento y suponía cosas. Como los tres cuestan menos de 1 $ al mes, pesa más no equivocarse con el cliente que ahorrar unos céntimos.

## Lo que aprendí

- El modelo más pequeño (3B) falla justo donde lo esperaba: en los cálculos.
- Un system prompt puede tener instrucciones que chocan. Al pedir una frase fija en español, los modelos dejaron de responder en inglés.
- La velocidad cambia bastante de una pregunta a otra, así que hay que mirar la media.

---

# Project 1: Model selection

Project for Module 2 of my AI Engineering master's (thePower). The full report (in Spanish) is in [proyecto1-seleccion-modelo.pdf](proyecto1-seleccion-modelo.pdf).

## The case

An online matcha tea shop wants a chat assistant on its website to answer pre-sale questions, calculate orders, recommend products and explain shipping. Text only, answers in under 2 seconds and a very small budget.

## What I did

1. Previous analysis: input and output, reasoning level, context window, and which models to rule out (image models or too expensive).
2. I picked 3 models of different sizes: Mistral Small 3, GPT-4o-mini and Llama 3.2 3B.
3. I tested them in the OpenRouter chat with the same system prompt, temperature 0.2 and no tools: 4 questions from the brief and 4 of my own (discount, trap, language and a long noisy message).

## Results

| Model | Correct | Average time | Estimated cost (10,000 queries/month) |
|---|---|---|---|
| Mistral Small 3 | 6/8 | ~1.9 s | ~$0.22 |
| GPT-4o-mini | 7/8 | ~1.9 s | ~$0.78 |
| Llama 3.2 3B | 3/8 | ~1.5 s | ~$0.59 |

OpenRouter prices on 30/09/2026.

## Decision

I chose GPT-4o-mini. It got the calculations right and stuck to the shop's data. Llama got the discount wrong and made things up, and Mistral was slower and assumed things. All three cost less than $1 a month, so not making mistakes with customers matters more than saving a few cents.

## What I learned

- The smallest model (3B) failed where I expected: calculations.
- A system prompt can have instructions that clash. Asking for a fixed sentence in Spanish stopped the models from answering in English.
- Speed changes a lot between questions, so the average is what matters.
