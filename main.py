import ollama
import json
import os           #Interactia con el sistema operativo

#Memoria persistente en un archivo JSON
ARCHIVO_MEMORIA = "memoria.json"

# =========================
# CARGAR MEMORIA
# =========================

if os.path.exists(ARCHIVO_MEMORIA):     #Verifica si el archivo de memoria existe

    with open(ARCHIVO_MEMORIA, "r", encoding="utf-8") as archivo:
        mensajes = json.load(archivo) #Convierte json a python

else:

    mensajes = [
        {
            'role': 'system',
            'content': (
                'Eres una IA experta en Python. '
                'Responde claro y corto.'
            )
        }
    ]

print("=== IA LOCAL CON MEMORIA ===")
print("Escribe 'salir' para terminar.\n")

# =========================
# CHAT PRINCIPAL
# =========================

while True:

    texto = input("Tú: ")

    if texto.lower() == "salir":
        print("Memoria guardada.")
        break

    mensajes.append({
        'role': 'user',
        'content': texto
    })

    stream = ollama.chat(
        model='llama3.2',
        messages=mensajes,
        stream=True
    )

    print("\nIA: ", end="")

    respuesta_completa = ""

    for chunk in stream:                        #Cada chunk es una parte de la respuesta que va llegando(tocken)

        contenido = chunk['message']['content']

        print(contenido, end="", flush=True)    #Imprime sin salto de línea y fuerza la actualización de la pantalla

        respuesta_completa += contenido

    print("\n")

    mensajes.append({
        'role': 'assistant',
        'content': respuesta_completa
    })

    # =========================
    # GUARDAR MEMORIA
    # =========================

    with open(ARCHIVO_MEMORIA, "w", encoding="utf-8") as archivo:

        json.dump(      #Convierte python a json
            mensajes,
            archivo,
            ensure_ascii=False, #Permite caracteres no ASCII (como acentos), caracteres en espanol
            indent=4    #Hace el json legible con sangría
        )