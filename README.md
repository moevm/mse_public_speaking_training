# mse_public_speaking_training

Env:
pip install Python-pptx
pip install SpeechRecognition
pip install time
pip install django


������ �������:
1) ����������� ���������� python-pptx
2) ��� ��������� ������ ������� ���������� ������� slides(), � ���������� �������� ������ �������.
3) ����� ������ ������� ����� - ����� ��� ��������)
������ ������� � ��� ����, �������� �� ���� � � ��� ������� ������ ��������� ���:
	text_slide = " "
	for shape in slide.shapes:
		if not shape.has_text_frame:
			continue
		text_slide += shape.text_frame + "\n"
� ��������� text_slide � ������� ������ � �������

������ ������ ��������� �����:
1) ������������ ���������� speech_recognition
2) ���������� ������ ����, ������� ������������ �� ���������� ���� ������������ 
3) ���������� ���� ������������ �� ��������� � ������� recognize_google_api
� ���������� �������� ���������� ���� String � ������������ �������

