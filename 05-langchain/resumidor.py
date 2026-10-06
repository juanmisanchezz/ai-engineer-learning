"""Resumidor: recibe un texto largo y lo resume en 3 viñetas."""

from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama import ChatOllama
from langchain_core.tools import tool
from langchain_core.messages import HumanMessage, ToolMessage
from langchain_core.chat_history import InMemoryChatMessageHistory


# 1) PROMPT: la instrucción se escribe una vez; {texto} es el hueco que rellenamos al invocar
prompt = ChatPromptTemplate.from_messages([
    ("system", "Eres un resumidor profesional. Devuelve SOLO el resumen distribuido en 3 viñetas, sin comentarios."),
    ("human", "{texto}"),
])

# 2) MODELO: el ChatModel local. Cambiar de proveedor = cambiar solo esta línea
modelo = ChatOllama(model="llama3.1", temperature=0)

# 3) PARSER: el modelo devuelve un AIMessage; el parser se queda con el texto limpio
parser = StrOutputParser()

# FUNCION: devuélve sólo 3 viñetas forzadas en caso de error
def forzar_3_vinetas(texto):

    # Partir la frase por los "\n" --> Split
    frases = texto.split ("\n")
    
    # Me quedo con las frases que empiecen con * --> Creo variable y for --- in --- y dentro un if con un append
    buenas = []
    for frase in frases:
        if frase.startswith("*"):
            buenas.append(frase)
    # De esas frases me quedo con las 3 primeras --> lista [:3]
    seleccionadas = buenas[:3]

    # Vuelvo a juntarlas con "\n" y devolverlas --> "\n".join(variable)

    return "\n".join(seleccionadas)

# LCEL: el | une las tres piezas en una tubería. La cadena también es un Runnable
cadena = prompt | modelo | parser | forzar_3_vinetas

# TOOL: lee un texto de la carpeta textos/ y lo devuelve entero
@tool
def leer_texto(nombre: str) -> str:
    """Lee el archivo textos/<nombre>.txt y devuelve su contenido completo."""
    # 1. Montar la ruta del archivo con el nombre
    ruta = f"textos/{nombre}.txt"

    # 2. Abrir el archivo y leer su texto
    texto = open(ruta, encoding= "utf-8").read()

    # 3. Devolver el texto
    return texto

# MODELO CON TOOLS: el mismo modelo, pero sabiendo que puede pedir leer_texto
modelo_con_tools = modelo.bind_tools([leer_texto])

historiales = {}

def obtener_historial(session_id: str) -> InMemoryChatMessageHistory:
    if session_id not in historiales:
        historiales[session_id] = InMemoryChatMessageHistory()
    return historiales[session_id]

if __name__ == "__main__":
    historial = obtener_historial("alumno-1")
    while True:
        mensaje = input("Escribe tu mensaje: ")
        historial.add_user_message(mensaje)                             

        if "resume" in mensaje.lower():
            respuesta = modelo_con_tools.invoke(historial.messages)
            historial.add_message(respuesta)                    
            for llamada in respuesta.tool_calls:
                texto = leer_texto.invoke(llamada["args"])
                resumen = cadena.invoke({"texto": texto})
                historial.add_message(ToolMessage(content=resumen, tool_call_id=llamada["id"]))
                historial.add_ai_message(resumen)
                print(resumen)                                  
        else:
            respuesta = modelo.invoke(historial.messages)
            historial.add_message(respuesta)
            print(respuesta.content)
