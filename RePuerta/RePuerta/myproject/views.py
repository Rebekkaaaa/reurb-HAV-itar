# from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.forms import *


def homepage(request):
    return render(request, 'home.html')


# def about(request):
#     return render(request, 'about.html')


def repare(request):
    return render(request, 'repare.html')


def replace(request):
    return render(request, 'replace.html')
