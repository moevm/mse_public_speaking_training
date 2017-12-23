import io

import pdftotext
from django.core.files.base import ContentFile
from django.core.files.images import ImageFile
from django.db.models.signals import post_save
from django.dispatch import receiver
from wand.color import Color
from wand.exceptions import BlobError
from wand.image import Image

from .models import Presentation, Slide


def cut_in_background(presentation):
    with open(presentation.file.path, "rb") as f:
        pdf_as_text = pdftotext.PDF(f)

    try:
        with Image(filename=presentation.file.path) as img:
            for num, page in enumerate(img.sequence):
                with Image(width=page.width, height=page.height, background=Color("white")) as bg:
                    bg.format = 'png'
                    bg.composite(page, 0, 0)
                    slide_as_image = io.BytesIO()
                    bg.save(file=slide_as_image)
                    django_image = ContentFile(slide_as_image.getvalue())

                    text = pdf_as_text[num]

                    slide = Slide.objects.create(num_page=num, text=text,
                                                 presentation=presentation, image=ImageFile(django_image))
                    slide.image.save('slide.png', django_image)
                    slide.save()

                    # slide.presentation.add(self)
                    # bg.save(file=slide.image)
                    # slide.save()
    except BlobError:
        print('Something was wrong')


@receiver(post_save, sender=Presentation)
def cut_presentation_on_slides(sender, instance, **kwargs):
    print('cutting presentation')
    with open(instance.file.path, "rb") as f:
        pdf_as_text = pdftotext.PDF(f)

    try:
        with Image(filename=instance.file.path) as img:
            for num, page in enumerate(img.sequence):
                with Image(width=page.width, height=page.height, background=Color("white")) as bg:
                    bg.format = 'png'
                    bg.composite(page, 0, 0)
                    slide_as_image = io.BytesIO()
                    bg.save(file=slide_as_image)
                    django_image = ContentFile(slide_as_image.getvalue())

                    text = pdf_as_text[num]

                    slide = Slide.objects.create(num_page=num, text=text,
                                                 presentation=instance, image=ImageFile(django_image))
                    slide.image.save('slide.png', django_image)
                    slide.save()

                    # slide.presentation.add(self)
                    # bg.save(file=slide.image)
                    # slide.save()
    except BlobError:
        print('Something was wrong')


# @receiver(post_save, sender=Voice)
def recognize_audio(sender, instance, **kwargs):
    r = sr.Recognizer()
    with sr.AudioFile(open(instance.as_ogg.file)) as source:
        audio = r.record(source)
    try:
        instance.as_text = r.recognize_google(audio)
    except instance.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except instance.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
    instance.save()

# post_save.connect(cut_presentation_on_slides, sender=Presentation)
