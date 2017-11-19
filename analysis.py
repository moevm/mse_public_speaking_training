#считаем, что у нас есть распарсенная презентация и массив из аудиофайлов для каждого слайда

import speech_recognition as sr
import ProcessingSound2 as sound
import pylab

# список слов на каждом слайде из аудиофайлов
# передаем массив аудиофайлов
def massWord(mass):
    r = sr.Recognizer()
    listWord = []
    for el in mass:
        s = sound.callback(r, el)
        if ((s.equals("error1")) or (s.equals("error2"))):
            s = ""
        listWord.append(s)
    return listWord

# количество слов на слайде
# передается список полученный из massWord
def wordsOnSlide(listWord):
    countWord = []
    for el in listWord:
        if (el == ""):
            countWord.append(0)
        else:
            countWord.append(len(el.split(" ")))
    return countWord

#graphWordsOnSlide(["l", "", "f f f f", "a a a a a a a", "r r r r", "2 f w e", "a s d f g"])

# график скорости (простой, то есть просто время аудиозаписи на количество сказанных слов)
# передается список секунд, в которые заканчивался показ данного слайда
# и список полученный из graphWordOnSlide
def simpleSpeed(time, countWord):
    speed = []
    for i in range(len(time)):
        if i == 0:
            t = time[0]
        else:
            t = time[i] - time[i - 1]
        speed.append(countWord[i] / t)
    for i in range(len(speed)):
        if i == 0:
            pylab.plot([0.0, time[0]], [speed[i], speed[i]], 'g')
        else:
            pylab.plot([time[i - 1], time[i - 1]], [speed[i - 1], speed[i]], 'g')
            pylab.plot([time[i - 1], time[i]], [speed[i], speed[i]], 'g')
    pylab.title("График скорости")
    pylab.ylabel("Скорость (количество слов в секунду)")
    pylab.xlabel("Секунды")
    pylab.show()


time = [20, 50, 67, 89, 105]
countWord = [30, 55, 34, 17, 44]
#simpleSpeed(time, countWord)

# график скорости доклада
# на первом графике показывается расход времени на слайд и среднее время на слайд
# на втором графике показывается расход слов на слайд и среднее количество слов на слайд
# передается список секунд, в которые заканчивался показ данного слайда
# и список полученный из graphWordOnSlide
def SpeedReport(time, countWord):
    numSlide = range(1, len(time) + 1)
    timeSlide = []
    for i in range(len(time)):
        if i == 0:
            timeSlide.append(time[0])
        else:
            timeSlide.append(time[i] - time[i - 1])
    averageTime = 0
    for el in timeSlide:
        averageTime += el
    averageTime /= len(time)
    pylab.plot(numSlide, timeSlide, 'g')
    pylab.plot([0, len(time)], [averageTime, averageTime], 'r--')
    pylab.axis([1, len(time), 0, max(time) + 10])
    pylab.title("Расход времени на слайд")
    pylab.ylabel("Количество секунд")
    pylab.xlabel("Номер слайда")
    pylab.show()

    averageCount = 0
    for el in countWord:
        averageCount += el
    averageCount /= len(countWord)
    pylab.plot(numSlide, countWord, 'g')
    pylab.plot([0, len(countWord)], [averageCount, averageCount], 'r--')
    pylab.axis([1, len(countWord), 0, max(countWord) + 5])
    pylab.title("Расход слов на слайд")
    pylab.ylabel("Количество слов")
    pylab.xlabel("Номер слайда")
    pylab.show()

#SpeedReport(time, countWord)

# сопоставление распознанных слов и текста со слайдов
# подсчитываем процент сказанных слов из текста со слайда
# выявление неосвященных тем - это те слайды, у которых процент меньше 60
# передается текст со слайдов и список полученный из massWord
def comparisionOfTheme(dict, listWord):
    percent = []
    for i in range(len(listWord)):
        mapSlideText = {}
        slideText = dict[i].split(" ")
        for el in slideText:
            count = mapSlideText.get(el)
            if count == None:
                mapSlideText[el] = 1
            else:
                mapSlideText[el] = count + 1
        mapSpeechText = {}
        speechText = listWord[i].split(" ")
        for el in speechText:
            count = mapSpeechText.get(el)
            if count == None:
                mapSpeechText[el] = 1
            else:
                mapSpeechText[el] = count + 1

        count = 0
        for el in mapSlideText.keys():
            countSlide = mapSlideText.get(el)
            countSpeech = mapSpeechText.get(el)
            if  countSpeech != None:
                if (countSlide < countSpeech):
                    count += countSlide
                else:
                    count += countSpeech
        percent.append(count * 100.0 / len(slideText))
    print(percent)


#dict = ['ald asf efhs skhe', 'oh ash ewds oih sx', 'ohuogwe qwe oi sda hoh', 'ohuwed owis wqe f qw', 'a a a a a a', 'ohe oue qw sf qw']
#listWord = ['ald ald a a aasf efhs skhe', 'axe qwead ewds erash ewds oih sx', 'ohuogwe qwefsd oiwes sda hoh', 'ohuwedwqe  wq qwe qwe owis wqe f qw', 'a a a', 'ohe oue qw sf qw']

#comparisionOfTheme(dict, listWord)




