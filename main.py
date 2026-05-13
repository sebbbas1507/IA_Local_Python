import ollama

mensajes = [
    {
        'role': 'system',
        'content': (
            'Eres una IA experta en Python. '
            'Explica de forma clara.'
        )
    }
]

print("=== IA LOCAL STREAMING ===")
print("Escribe 'salir' para terminar.\n")

while True:

    texto = input("Tú: ")

    if texto.lower() == "salir":
        print("Cerrando chat...")
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

    for chunk in stream:

        contenido = chunk['message']['content']

        print(contenido, end="", flush=True)

        respuesta_completa += contenido

    print("\n")

    mensajes.append({
        'role': 'assistant',
        'content': respuesta_completa
    })