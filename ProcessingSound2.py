import speech_recognition as sr

def callback(recognizer, audio):
    try:
        s = recognizer.recognize_google(audio, language="ru-RU")
    except sr.UnknownValueError:
        s = 'error1'
    except sr.RequestError as e:
        s = 'error2'
    return s


r = sr.Recognizer()

with sr.Microphone() as source:
    audio = r.listen(source)

s = callback(r, audio)

my_file = open("some.txt", "w")
my_file.write(s)
my_file.close()