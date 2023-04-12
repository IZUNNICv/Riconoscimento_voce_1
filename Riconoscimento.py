import speech_recognition as reconocimiento_voz 

reconocimiento = reconocimiento_voz.Recognizer() # ho creato l'instanza della classe speech recognition e poi utilizzo il metodo recogizer()
microfono = reconocimiento_voz.Microphone()

with microfono as source:
    audio = reconocimiento.listen(source)

text = reconocimiento.recognize_google(audio, language='es')  # Corregir 'lenguage' a 'language' y usar 'es' en minúsculas
print(f'HAS DICHO: {text}')  # Corregir 'HAI DETTO' a 'HAS DICHO' y agregar f antes de la cadena para formatear la variable 'text'