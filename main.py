import ollama

# Historial de conversación
mensajes = []

print("=== IA LOCAL ===")
print("Escribe 'salir' para terminar.\n")

while True:

    # Pedir mensaje al usuario
    texto = input("Tú: ")

    # Salir del programa
    if texto.lower() == "salir":
        print("Cerrando chat...")
        break

    # Agregar mensaje del usuario
    mensajes.append({
        'role': 'user',
        'content': texto
    })

    # Enviar conversación completa a la IA
    respuesta = ollama.chat(
        model='llama3.2',
        messages=mensajes
    )

    # Extraer respuesta
    contenido = respuesta['message']['content']

    # Mostrar respuesta
    print(f"\nIA: {contenido}\n")

    # Guardar respuesta en historial
    mensajes.append({
        'role': 'assistant',
        'content': contenido
    })

