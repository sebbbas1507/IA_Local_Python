import ollama

# Historial con mensaje de sistema
mensajes = [
    {
        'role': 'system',
        'content': (
            'Eres una IA de asistencia computacional como cortana. '
            'Responde de forma clara, educativa y corta.'
            'Habla como un robot.'
        )
    }
]

print("=== IA LOCAL ===")
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

    respuesta = ollama.chat(
        model='llama3.2',
        messages=mensajes
    )

    contenido = respuesta['message']['content']

    print(f"\nIA: {contenido}\n")

    mensajes.append({
        'role': 'assistant',
        'content': contenido
    })