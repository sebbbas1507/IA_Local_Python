import ollama
import json
import os

ARCHIVO_MEMORIA = "memoria.json"

# =====================================
# FUNCIONES
# =====================================

def guardar_memoria():

    with open(ARCHIVO_MEMORIA, "w", encoding="utf-8") as archivo:

        json.dump(
            mensajes,
            archivo,
            ensure_ascii=False,
            indent=4
        )

def cargar_memoria():

    if os.path.exists(ARCHIVO_MEMORIA):

        with open(ARCHIVO_MEMORIA, "r", encoding="utf-8") as archivo:
            return json.load(archivo)

    return [
        {
            'role': 'system',
            'content': (
                'Eres una IA experta en Python. '
                'Responde claro y corto.'
            )
        }
    ]

# =====================================
# CARGAR MEMORIA
# =====================================

mensajes = cargar_memoria()

print("=== IA LOCAL AVANZADA ===")
print("Comandos:")
print("/salir")
print("/reset")
print("/guardar")
print("/historial\n")

# =====================================
# CHAT PRINCIPAL
# =====================================

while True:

    texto = input("Tú: ")

    # =====================================
    # COMANDO: SALIR
    # =====================================

    if texto == "/salir":

        guardar_memoria()

        print("Memoria guardada.")
        print("Cerrando programa...")

        break

    # =====================================
    # COMANDO: RESET
    # =====================================

    if texto == "/reset":

        mensajes = [
            {
                'role': 'system',
                'content': (
                    'Eres una IA experta en Python. '
                    'Responde claro y corto.'
                )
            }
        ]

        guardar_memoria()

        print("Memoria reiniciada.\n")

        continue

    # =====================================
    # COMANDO: GUARDAR
    # =====================================

    if texto == "/guardar":

        guardar_memoria()

        print("Memoria guardada.\n")

        continue

    # =====================================
    # COMANDO: HISTORIAL
    # =====================================

    if texto == "/historial":

        print(f"\nMensajes guardados: {len(mensajes)}\n")

        continue

    # =====================================
    # MENSAJE NORMAL
    # =====================================

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

    for chunk in stream:

        contenido = chunk['message']['content']

        print(contenido, end="", flush=True)

        respuesta_completa += contenido

    print("\n")

    mensajes.append({
        'role': 'assistant',
        'content': respuesta_completa
    })

    guardar_memoria()