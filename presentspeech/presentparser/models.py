from django.db import models


class Presentation(models.Model):
    # text = models.TextField(verbose_name='Текст презентации', blank=True, null=True)
    file = models.FileField(verbose_name='Файл презентации', upload_to='uploads/presentations/', blank=False,
                            null=False)
    # text_from_voice = models.TextField(verbose_name='Произнесенный текст', blank=True, null=True)
    match_percentage = models.SmallIntegerField(verbose_name='Процент совпадения', blank=True, null=True)

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        super(Presentation, self).save()

    class Meta:
        verbose_name = 'Презентация'
        verbose_name_plural = 'Презентации'

    def __str__(self):
        return self.file.name


class Slide(models.Model):
    text = models.TextField(verbose_name='Текст слайда')
    image = models.ImageField(verbose_name='Слайд в виде изображения', upload_to='uploads/slides/')
    num_page = models.PositiveSmallIntegerField(verbose_name='Номер страницы')

    presentation = models.ForeignKey('Presentation', verbose_name='Презентация', on_delete=models.CASCADE, blank=True,
                                     null=True)

    class Meta:
        verbose_name = 'Слайд'
        verbose_name_plural = 'Слайды'


class Voice(models.Model):
    as_text = models.TextField(verbose_name='Голос во время презентации в виде текста')
    as_wav = models.FileField(verbose_name='Записанный голос', upload_to='uploads/voice/')
    presentation = models.ForeignKey('Presentation', verbose_name='Презентация', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Голос'
        verbose_name_plural = 'Голос'


from .signals import *
