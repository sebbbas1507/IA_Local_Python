import ollama
import pyttsx3
import speech_recognition as sr

# =====================================
# MOTOR DE VOZ
# =====================================

voz = pyttsx3.init()

voz.setProperty('rate', 180)

# =====================================
# RECONOCEDOR
# =====================================

reconocedor = sr.Recognizer()

# =====================================
# MEMORIA
# =====================================

mensajes = [
    {
        'role': 'system',
        'content': (
            'Eres una IA amigable experta en Python.'
        )
    }
]

# =====================================
# HABLAR
# =====================================

def hablar(texto):

    voz.say(texto)

    voz.runAndWait()

# =====================================
# ESCUCHAR
# =====================================

def escuchar():

    with sr.Microphone() as source:

        print("\n🎤 Escuchando...\n")

        recognizer_ajuste = reconocedor.adjust_for_ambient_noise(
            source,
            duration=1
        )

        audio = reconocedor.listen(source)

    try:

        texto = reconocedor.recognize_google(
            audio,
            language="es-ES"
        )

        print(f"Tú: {texto}\n")

        return texto

    except:

        print("No entendí.\n")

        return ""

# =====================================
# CHAT PRINCIPAL
# =====================================

print("=== IA POR VOZ ===")
print("Di 'salir' para terminar.\n")

while True:

    texto_usuario = escuchar()

    if texto_usuario == "":
        continue

    if "salir" in texto_usuario.lower():

        hablar("Hasta luego")

        break

    mensajes.append({
        'role': 'user',
        'content': texto_usuario
    })

    stream = ollama.chat(
        model='llama3.2',
        messages=mensajes,
        stream=True
    )

    respuesta_completa = ""

    print("IA: ", end="")

    for chunk in stream:

        contenido = chunk['message']['content']

        print(contenido, end="", flush=True)

        respuesta_completa += contenido

    print("\n")

    mensajes.append({
        'role': 'assistant',
        'content': respuesta_completa
    })

    hablar(respuesta_completa)