from django.shortcuts import render, redirect
from django.http import HttpResponse


def home_files(request, filename):
    return render(request, filename, {}, content_type="text/plain")

def homepage(request):
    return render(request, 'books/homepage.html', {})
