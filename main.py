import ollama
import json
import os
from datetime import datetime

ARCHIVO_MEMORIA = "memoria.json"

# =========================================
# FUNCIONES DE MEMORIA
# =========================================

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

# =========================================
# HERRAMIENTAS
# =========================================

def obtener_hora():

    ahora = datetime.now()

    return ahora.strftime("%H:%M:%S")

def obtener_fecha():

    hoy = datetime.now()

    return hoy.strftime("%d/%m/%Y")

# =========================================
# CARGAR MEMORIA
# =========================================

mensajes = cargar_memoria()

print("=== IA LOCAL CON HERRAMIENTAS ===")
print("Comandos:")
print("/salir")
print("/reset\n")

# =========================================
# CHAT PRINCIPAL
# =========================================

while True:

    texto = input("Tú: ")

    # =========================================
    # COMANDO: SALIR
    # =========================================

    if texto == "/salir":

        guardar_memoria()

        print("Memoria guardada.")
        print("Cerrando programa...")

        break

    # =========================================
    # COMANDO: RESET
    # =========================================

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

    # =========================================
    # TOOL CALLING SIMPLE
    # =========================================

    texto_minuscula = texto.lower()

    if "hora" in texto_minuscula:

        hora = obtener_hora()

        print(f"\n🕒 Hora actual: {hora}\n")

        continue

    if "fecha" in texto_minuscula:

        fecha = obtener_fecha()

        print(f"\n📅 Fecha actual: {fecha}\n")

        continue

    # =========================================
    # IA NORMAL
    # =========================================

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