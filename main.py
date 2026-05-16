import ollama
import json
import os
from datetime import datetime # Para funciones de fecha y hora

ARCHIVO_MEMORIA = "memoria.json"

# =========================================
# FUNCIONES DE MEMORIA
# =========================================

def guardar_memoria():

    with open(ARCHIVO_MEMORIA, "w", encoding="utf-8") as archivo:

        json.dump(          # Guardar la memoria en un archivo JSON
            mensajes,       # Lista de mensajes a guardar
            archivo,        # Guardar la memoria en un archivo JSON
            ensure_ascii=False, # Para que los caracteres especiales se guarden correctamente
            indent=4    # Para que el JSON se vea bonito y legible
        )

def cargar_memoria():

    if os.path.exists(ARCHIVO_MEMORIA):     # Si el archivo de memoria existe, lo cargamos

        with open(ARCHIVO_MEMORIA, "r", encoding="utf-8") as archivo:
            return json.load(archivo)   # Devolver la memoria cargada desde el archivo JSON

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

    return ahora.strftime("%H:%M:%S")   # Devolver la hora actual en formato de horas, minutos y segundos

def obtener_fecha():

    hoy = datetime.now()

    return hoy.strftime("%d/%m/%Y")    # Devolver la fecha actual en formato de día, mes y año

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

        break       # Salir del bucle principal para cerrar el programa

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

        continue        # Volver al inicio del bucle principal para esperar el siguiente mensaje del usuario

    # =========================================
    # TOOL CALLING SIMPLE
    # =========================================

    texto_minuscula = texto.lower()

    if "hora" in texto_minuscula:   # Si el mensaje del usuario contiene la palabra "hora" (sin importar mayúsculas o minúsculas)

        hora = obtener_hora()       # Obtener la hora actual utilizando la función definida anteriormente

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