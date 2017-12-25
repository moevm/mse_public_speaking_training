from django.urls import path

from .views import get_slide, upload_voice, PresentationView

urlpatterns = [
    path('<int:presentation_id>/', PresentationView.as_view(), name='presentation'),
    path('<int:presentation_id>/<int:slide>/', get_slide, name='slide'),
    path('<int:presentation_id>/<int:slide>/upload_voice/', upload_voice, name='upload_voice'),
]
