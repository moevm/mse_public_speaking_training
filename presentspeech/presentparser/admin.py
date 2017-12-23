from django.contrib import admin
from .models import Presentation, Slide, Voice

# Register your models here.
admin.site.register(Presentation)
admin.site.register(Slide)
admin.site.register(Voice)
