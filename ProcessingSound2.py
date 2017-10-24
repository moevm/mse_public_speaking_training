import speech_recognition as sr

def callback(recognizer, audio):
    try:
        s = recognizer.recognize_google(audio, language="ru-RU")
        print(s)
    except sr.UnknownValueError:
        s = 'error1'
    except sr.RequestError as e:
        s = 'error1'
    return s


r = sr.Recognizer()

with sr.Microphone() as source:
    audio = r.listen(source)

callback(r, audio)