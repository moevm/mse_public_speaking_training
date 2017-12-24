# mse_public_speaking_training

Env:
pip install Python-pptx
pip install SpeechRecognition
pip install time
pip install django

Веб страница:
1) Открывается страница, на которой выбирается презентация для выступления и указывается временной порог, в который необходимо уложиться.
![Image alt](https://github.com/moevm/mse_public_speaking_training/blob/master/images/web1.jpg)
2) После нажатию на кнопку "Начать" открывается страница с первым слайдом презентации и кнопками для управления.
![Image alt](https://github.com/moevm/mse_public_speaking_training/blob/master/images/web2.jpg)
3) Для того, чтобы начать тренировку, необходимо нажать на кнопку "Старт". После этого начнется обратный отсчет времени.
![Image alt](https://github.com/moevm/mse_public_speaking_training/blob/master/images/web3.jpg)
4) Если пользователь не уложился в заданный временной порог, то тренировка не останавливается, а продолжается. Причем таймер идет с отрицательным значением
![Image alt](https://github.com/moevm/mse_public_speaking_training/blob/master/images/web4.jpg)
5) Для того, чтобы закончить тренировку, необходимо нажать на кнопку "Стоп". После этого выведется окошко с результатами.
![Image alt](https://github.com/moevm/mse_public_speaking_training/blob/master/images/web5.jpg)

Работа парсера:
1) Подключение библиотеки python-pptx
2) Для получения списка слайдов используем функцию slides(), в результате получаем список слайдов.
3) Затем делаем словарь слайд - текст или наоборот)
Список слайдов у нас есть, проходим по нему и в для каждого слайда выполняем код:
	```python
	text_slide = " "
	for shape in slide.shapes:
		if not shape.has_text_frame:
			continue
		text_slide += shape.text_frame + "\n"
	```
И добавляем text_slide в словарь вместе с текстом
![Image alt](https://github.com/moevm/mse_public_speaking_training/blob/master/images/parser.png)

Работа модуля обработки звука:
1) Подключается библиотека speech_recognition
2) Начинается запись речи, которая продолжается до отстановки речи пользователя 
3) Записанная речь отправляется на обработку с помощью recognize_google_api
В результате получаем переменную типа String с распознанным текстом
![Image alt](https://github.com/moevm/mse_public_speaking_training/blob/master/images/sound.png)

Работа модуля анализа полученных данных:
* def massWord(mass):
	1. На вход получаем список записанных аудиофайлов
	2. Каждый элемент список отправляется на обработку функции из модуля обработки звука.
	3. На выходе получаем список из сказанного текста на каждом слайде

* def wordsOnSlide(listWord):
	1. На вход получаем список полученный из функции massWord
	2. Подсчитываем количество слов в каждом элементе этого списка
	3. На выходе список из количества слов, сказанного во время просмотра презентации

* def simpleSpeed(time, countWord):
	Реализован простой подсчет скорости, т.е. считаем, что в процессе показа одного слайда скорость постоянная
	1. На вход получаем список секунд, в которые заканчивается показ слайдов и список из wordsOnSlide
	2. Для получения списка скоростей говорящего на каждом слайде проходимся по списку time и считаем, сколько секунд затратили на данный слайд. В этом же цикле делим число сказанных слов на количество секунд и получаем скорость на данном слайде.
	3. Строим график скорость с помощью полученных данных.
![Image alt](https://github.com/moevm/mse_public_speaking_training/blob/master/images/speed.png)

* def SpeedReport(time, countWord):
	1. На вход получаем списк секунд, в которые заканчивается данный слайд и список из wordsOnSlide
	2. Подсчитываем количество секунд, которое тратится на каждый слайд.
	3. Находим среднее количество секунд, потраченное на один слайд
	4. Строим график, на котором показано среднее количество секунд (красный пунктир) и количество секунд, потраченное на каждый слайд
	![Image alt](https://github.com/moevm/mse_public_speaking_training/blob/master/images/time.png)
	5) Находим среднее количество слов, потраченное на один слайд
	6) Строим график, на котором показано среднее количество слов (красный пунктир) и количество слов, потраченное на каждый слайд
	![Image alt](https://github.com/moevm/mse_public_speaking_training/blob/master/images/word.png)

* def comparisionOfTheme(dict, listWord):
	1. На вход получаем список с текстом из слайдов и список поллученный из massWord
	![Image alt](https://github.com/moevm/mse_public_speaking_training/blob/master/images/data.PNG)
	2. Для каждого слайда:
		1. Составляем словарь, в котором ключом является слово, а значением количество таких слов в тексте на слайде
		2. Составляем словарь, в котором ключом является слово, а значением количество таких слов в сказанном тексте пользователем на данном слайде
		3. Производим сопоставление этих двух списков и подсчитываем количество слов, которое встречается в тексте на слайде и в сказанном пользователем тексте
		4. Подсчитываем процент сказанных слов со слайда
	![Image alt](https://github.com/moevm/mse_public_speaking_training/blob/master/images/result.png)
>>>>>>> 6ca9a07fd6fecc8c0db5868be85381af754f313c
