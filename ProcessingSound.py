import wave
import numpy as np
import math
import pylab

# количество байт уходящих на кодирование одного сэмпла
types = {
    1: np.int8,
    2: np.int16,
    4: np.int32
}

def entropy(list):
    sum = 0.0
    for el in list:
        if el != 0:
            sum += el * math.log(abs(el), 2)
    return sum

wav = wave.open("1.wav", mode="r")

#кортеж основных параметров: число каналов, число байт на сэмпл, число фреймов в секунду, общее число фреймов, тип сжатия, имя типа сжатия
(nchannels, sampwidth, framerate, nframes, comptype, compname) = wav.getparams()
content = wav.readframes(nframes) #считываем фреймы

print(nchannels)

#получаем массив сэмплов, для одного потока это массив фреймов
samples = np.fromstring(content, dtype=types[sampwidth])
maxEl = max(abs(samples))

samples = [el/maxEl for el in samples]

#разбиваем на промежутки по 10мс с нахлестом в 50% (1с = 1000мс) и считаем энтропию
ent=[]
n = framerate // 100
if n % 2 != 0:
    n = n - 1

for i in range(0, nframes, int(n/2)):
    ent.append(entropy(samples[i:i+n]))

threshold = (max(ent) - min(ent))/2

pylab.plot(range(0, len(ent)), ent)
pylab.plot([0, len(ent)], [threshold, threshold])
pylab.show()



count = 0
word = False

for el in ent:
    if el > threshold:
       if word == False:
           word = True
           count += 1
    if el < threshold:
        if word:
            word = False

print(count)