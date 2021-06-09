from django.urls import path
from . import views

urlpatterns = [
    path('', views.taskist(), name='tasks'),
]
