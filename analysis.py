#считаем, что у нас есть распарсенная презентация, список из аудиофайлов для каждого слайда и список секунд, в которые заканчивает показ слайда

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

# график скорости (простой, то есть просто время аудиозаписи на количество сказанных слов)
# передается список секунд, в которые заканчивался показ данного слайда
# и список полученный из wordsOnSlide
def simpleSpeed(time, countWord):
    speed = []
    max = 0
    for i in range(len(time)):
        if i == 0:
            t = time[0]
        else:
            t = time[i] - time[i - 1]
        speed.append(countWord[i] / t)
    for i in range(len(speed)):
        if (max < speed[i]):
            max = speed[i]
        if i == 0:
            pylab.plot([0.0, time[0]], [speed[i], speed[i]], 'g')
            pylab.plot([time[0], time[0]], [-1.0, 10.0], 'r--')
            pylab.text( 1.0, speed[i] + 0.02, str(i + 1) + ' слайд')
        else:
            pylab.plot([time[i - 1], time[i - 1]], [speed[i - 1], speed[i]], 'g')
            pylab.plot([time[i - 1], time[i]], [speed[i], speed[i]], 'g')
            pylab.plot([time[i], time[i]], [-1.0, 10.0], 'r--')
            pylab.text(time[i - 1] + 1, speed[i] + 0.02, str(i + 1) + ' слайд')
    pylab.title("График скорости")
    pylab.ylabel("Скорость (количество слов в секунду)")
    pylab.xlabel("Секунды")
    pylab.ylim([0, max + 1])
    pylab.show()

# график скорости доклада
# на первом графике показывается расход времени на слайд и среднее время на слайд
# на втором графике показывается расход слов на слайд и среднее количество слов на слайд
# передается список секунд, в которые заканчивался показ данного слайда
# и список полученный из wordsOnSlide
def SpeedReport(time, countWord):
    numSlide = range(1, len(time) + 1)
    timeSlide = []
    for i in range(len(time)):
        if i == 0:
            timeSlide.append(time[0])
        else:
            timeSlide.append(time[i] - time[i - 1])
    averageTime = time[len(time) - 1] / len(time)
    pylab.plot(numSlide, timeSlide, 'g')
    pylab.plot([0, len(time)], [averageTime, averageTime], 'r--')
    pylab.axis([1, len(time), 0, max(timeSlide) + 10])
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


#dict = ['презентация', 'слайд номер один', 'слайд номер два', 'слайд слайд слайд', 'на слайде четыре', 'конец презентации']
#listWord = ['тестовая презентация', 'первый слайд', 'слайд номер два слайд номер два', 'слайд', 'слайд', 'конец']

#comparisionOfTheme(dict, listWord)

time = [20, 50, 67, 89, 105]
countWord = [30, 55, 34, 17, 44]
simpleSpeed(time, countWord)


