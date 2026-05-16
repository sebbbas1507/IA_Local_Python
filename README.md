# Instrucciones:

- Crea una carpeta de proyecto
- coloca el archivo **main.py** en la carpeta
- Abre una terminal en la carpeta de proyecto
- En la terminal escribe "python -m venv venv" para crear un contenedor de la aplicacion(entorno virtual).
- Se creara una  carpeta "venv" en la carpeta principal, los paquetes se guardaran solo en la carpeta del proyecto y no en el entorno global.
- Ejecuta el comando ".\venv\Scripts\activate" en la tarminal para activar el *entorno virtual*, en la ruta aparecera un (venv) al inicio.
- Ejecuta "pip install requests" en la terminal
- Descarga e instala ollama desde su web, verifica su instalacion "ollama --version"
- Ejecuta el comando "ollama run llama3.2" para descargar el modelo
- En la terminal de python con el entorno virtual activado ejecuta:
* python -m pip install ollama
* python -m pip install requests
* python -m pip install pyttsx3
* python -m pip install SpeechRecognition
* python -m pip install pyaudio
* python -m pip install pyinstaller

- Para correr el archivo (**voz.py**) es necesatio tener la version de python *3.11*, crea un entorno virtual con esta version.
- Corre el programa con "python main.py"
- Corre el programa con "python voz.py"



