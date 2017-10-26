# mse_public_speaking_training

Env:
pip install Python-pptx
pip install SpeechRecognition
pip install time
pip install django


Работа парсера:
1) Подключение библиотеки python-pptx
2) Для получения списка слайдов используем функцию slides(), в результате получаем список слайдов.
3) Затем делаем словарь слайд - текст или наоборот)
Список слайдов у нас есть, проходим по нему и в для каждого слайда выполняем код:
	text_slide = " "
	for shape in slide.shapes:
		if not shape.has_text_frame:
			continue
		text_slide += shape.text_frame + "\n"
И добавляем text_slide в словарь вместе с текстом

Работа модуля обработки звука:
1) Подключается библиотека speech_recognition
2) Начинается запись речи, которая продолжается до отстановки речи пользователя 
3) Записанная речь отправляется на обработку с помощью recognize_google_api
В результате получаем переменную типа String с распознанным текстом

