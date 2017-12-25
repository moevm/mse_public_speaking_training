import threading

from django.core.files.base import ContentFile
from django.http import HttpResponse
from django.shortcuts import redirect, get_object_or_404
from django.utils.html import escape
from django.views.generic import TemplateView
import speech_recognition as sr

from .models import Presentation, Voice


def get_slide(request, presentation_id, slide):
    if not request.user.is_authenticated:
        return redirect('login/')

    presentation = get_object_or_404(Presentation, pk=presentation_id)
    slide = presentation.slide_set.get(num_page=slide)

    response = HttpResponse(slide.image.file)
    response['Content-Type'] = 'image/png'

    return response


def recognize_voice(voice):
    r = sr.Recognizer()
    with sr.AudioFile(voice.as_wav.file) as source:
        audio = r.record(source)
    try:
        voice.as_text = r.recognize_google(audio, language='ru-RU')
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
    else:
        print(voice.as_text)
        voice.save()


def upload_voice(request, presentation_id, slide):
    if request.method == 'POST':
        presentation = get_object_or_404(Presentation, pk=presentation_id)
        # slide = presentation.slide_set.get(num_page=slide)
        voice = Voice.objects.create(presentation=presentation)
        voice.as_wav.save('recorded_voice.wav', ContentFile(request.body))
        t = threading.Thread(target=recognize_voice, args=(voice,), kwargs={})
        t.setDaemon = True
        t.start()

        return HttpResponse(escape(repr(request)))


class PresentationView(TemplateView):
    template_name = 'presentation.html'

    def get(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            context = self.get_context_data()
            return self.render_to_response(context)
        else:
            return redirect('/')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.GET.get('timer'):
            context['timer'] = self.request.GET['timer']
        presentation_id = self.kwargs['presentation_id']
        context['presentation_id'] = presentation_id
        context['max_slides'] = Presentation.objects.get(pk=presentation_id).slide_set.all().count()
        return context
