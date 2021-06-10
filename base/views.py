from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Task
from django.urls import reverse_lazy

from django.contrib.auth.views import LoginView

from django.contrib.auth.mixins import LoginRequiredMixin

class CustomLoginView(LoginView):
    template_name = 'base/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_sucess_url(self):
        return reverse_lazy('login')



class TaskList(LoginRequiredMixin, ListView):
    model = Task
    context_object_name = 'tasks'


