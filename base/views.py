# from django.shortcuts import render
from django.http import HttpResponse


def taskist():
    return HttpResponse('To Do List')
