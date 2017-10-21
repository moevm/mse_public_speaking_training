import speech_recognition as sr

def callback(recognizer, audio):
    try:
        s = recognizer.recognize_google(audio, language="ru-RU")
        print(s)
        print(len(s.split(" ")))
    except sr.UnknownValueError:
        print("Робот не расслышал фразу")
    except sr.RequestError as e:
        print("Ошибка сервиса; {0}".format(e))


r = sr.Recognizer()

with sr.Microphone() as source:
    audio = r.listen(source)

callback(r, audio)