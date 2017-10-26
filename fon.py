import speech_recognition as sr
import time

def callback(recognizer, audio):
    print(1)
    try:
        s = recognizer.recognize_google(audio, language="ru-RU")
        print(s)
        print(len(s.split(" ")))
    except sr.UnknownValueError:
        print("Робот не расслышал фразу")
    except sr.RequestError as e:
        print("Ошибка сервиса; {0}".format(e))


r = sr.Recognizer()
r.listen_in_background(sr.Microphone(), callback)

for i in range(50):
    print(i)
    time.sleep(0.1)