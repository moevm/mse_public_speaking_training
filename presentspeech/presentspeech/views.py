from django.contrib.auth import authenticate
from django.contrib.auth.views import login
from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import FormView

from presentparser.models import Presentation
from .forms import DashboardForm, RegisterForm


class RegistrationView(FormView):
    template_name = 'registration.html'
    form_class = RegisterForm
    success_url = '/'

    def form_valid(self, form):
        form.save()
        username = form.cleaned_data.get('username')
        raw_password = form.cleaned_data.get('password1')
        user = authenticate(username=username, password=raw_password)
        login(self.request, user)
        return super(RegistrationView, self).form_valid(form)


class DashboardView(FormView):
    template_name = 'dashboard.html'
    form_class = DashboardForm

    def form_valid(self, form):
        timer = form.cleaned_data.get('timer')
        presentation = Presentation(file=self.request.FILES['presentation'])
        print(type(self.request.FILES['presentation']))
        presentation.save()
        print(presentation.id)
        redirect_to = '%s?timer=%i' % (reverse('presentation', kwargs={'presentation_id': presentation.id}), timer)
        return redirect(redirect_to)

    def get(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            context = self.get_context_data()
            return self.render_to_response(context)
        else:
            return redirect('login/')
