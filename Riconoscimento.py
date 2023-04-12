import speech_recognition as reconocimiento_voz 

reconocimiento = reconocimiento_voz.Recognizer() # ho creato l'instanza della classe speech recognition e poi utilizzo il metodo recogizer()
microfono = reconocimiento_voz.Microphone()

with microfono as source:
    audio = reconocimiento.listen(source)

text = reconocimiento.recognize_google(audio, language='es')  
print(f'HAS DICHO: {text}')  
