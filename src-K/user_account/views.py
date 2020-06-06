from django.contrib.auth.models import User
from django.shortcuts import render

# Create your views here.
from django.urls import reverse
from django.views.generic import CreateView

from user_account.forms import UserAccountRegistrationForms


class CreateUserAccountView(CreateView):
    model = User
    template_name = 'registration.html'
    form_class = UserAccountRegistrationForms

    def get_success_url(self):
        return reverse('success')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=None, **kwargs)
        context['title'] = 'Register new user'
        return context


def success_func(request):
    return render(request=request,
                  template_name='success.html')
