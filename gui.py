import tkinter as tk                 # Importar la biblioteca Tkinter para crear la interfaz gráfica
from tkinter import scrolledtext     # Importar el widget ScrolledText para mostrar el chat con barra de desplazamiento
import threading                     # Importar la biblioteca threading para ejecutar la generación de respuestas en un hilo separado# Importar otras bibliotecas necesarias
import ollama

# ======================================
# MEMORIA
# ======================================

mensajes = [
    {
        'role': 'system',
        'content': (
            'Eres una IA experta en Python. '
            'Responde claro y corto.'
        )
    }
]

# ======================================
# FUNCIÓN IA
# ======================================

def generar_respuesta(texto_usuario):

    mensajes.append({
        'role': 'user',
        'content': texto_usuario
    })

    stream = ollama.chat(
        model='llama3.2',
        messages=mensajes,
        stream=True
    )

    chat.insert(tk.END, "IA: ")                       # Insertar "IA: " al inicio de la respuesta    

    respuesta_completa = ""

    for chunk in stream:                               # Recorrer cada fragmento de la respuesta generada por la IA

        contenido = chunk['message']['content']        # Obtener el contenido del fragmento actual

        respuesta_completa += contenido

        chat.insert(tk.END, contenido)                 # Insertar el fragmento actual en el widget de chat

        chat.see(tk.END)                               # Desplazar el widget de chat hacia abajo para mostrar la última parte de la respuesta

        chat.update_idletasks()                        # Fuerza actualizar la interfaz gráfica inmediatamente para mostrar el nuevo contenido insertado  

    chat.insert(tk.END, "\n\n")

    mensajes.append({
        'role': 'assistant',
        'content': respuesta_completa
    })

# ======================================
# ENVIAR MENSAJE
# ======================================

def enviar_mensaje():                                 # Función que se ejecuta cuando el usuario envía un mensaje

    texto_usuario = entrada.get()                     # Obtener el texto ingresado por el usuario en la entrada de texto

    if texto_usuario == "":
        return                                        # Si el usuario no ha ingresado ningún texto, no hacer nada y salir de la función   

    # Mostrar usuario
    chat.insert(tk.END, f"Tú: {texto_usuario}\n\n")   # Insertar el mensaje del usuario en el widget de chat

    # Limpiar entrada
    entrada.delete(0, tk.END)                         # Borrar el contenido de la entrada de texto para que el usuario pueda escribir un nuevo mensaje

    # Crear thread
    hilo = threading.Thread(        # Crear un nuevo hilo para ejecutar la función de generación de respuesta sin bloquear la interfaz gráfica
        target=generar_respuesta,   # Especificar la función que se ejecutará en el hilo
        args=(texto_usuario,)       # Pasar el texto del usuario como argumento a la función de generación de respuesta
    )

    hilo.start()                                     # Iniciar el hilo para que comience a generar la respuesta de la IA

# ======================================
# VENTANA
# ======================================

ventana = tk.Tk()                                    # Crear la ventana principal de la aplicación utilizando Tkinter

ventana.title("IA Local Avanzada")

ventana.geometry("700x500")

# ======================================
# CHAT
# ======================================

chat = scrolledtext.ScrolledText(       
    ventana,
    wrap=tk.WORD,
    font=("Arial", 12)
)                                                   # Crear un widget de texto con barra de desplazamiento para mostrar el chat entre el usuario y la IA

chat.pack(
    padx=10,
    pady=10,
    fill=tk.BOTH,
    expand=True
)                                                   # Empaquetar el widget de chat en la ventana principal con relleno y para que se expanda y llene el espacio disponible  

# ======================================
# FRAME INFERIOR
# ======================================

frame_inferior = tk.Frame(ventana)                  # Crear un frame (marco) para contener la entrada de texto y el botón de enviar en la parte inferior de la ventana

frame_inferior.pack(
    fill=tk.X,
    padx=10,
    pady=10
)

# ======================================
# ENTRADA
# ======================================

entrada = tk.Entry(
    frame_inferior,
    font=("Arial", 12)
)

entrada.pack(
    side=tk.LEFT,       # Empaquetar la entrada de texto en el lado izquierdo del frame inferior
    fill=tk.X,
    expand=True,
    padx=(0, 10)
)

# ======================================
# BOTÓN
# ======================================

boton = tk.Button(
    frame_inferior,
    text="Enviar",
    command=enviar_mensaje
)

boton.pack(side=tk.RIGHT)                                   # Empaquetar el botón en el lado derecho del frame inferior

# ======================================
# ENTER PARA ENVIAR
# ======================================

entrada.bind("<Return>", lambda event: enviar_mensaje())    # Vincular la tecla Enter para que al presionarla se ejecute la función de enviar mensaje

# ======================================
# EJECUTAR
# ======================================

ventana.mainloop()                                          # Iniciar el bucle principal de la ventana para que la aplicación se ejecute y responda a las interacciones del usuario 