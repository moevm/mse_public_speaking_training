from django.db import models
from django import forms
class Presentation(models.Model):
    product=models.FileField(upload_to=None, max_length=100)
    #product = models.TextField(max_length=150)



