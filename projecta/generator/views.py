from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def Home(request):
    return render(request, 'generator/Home.html')


def About(request):
    return render(request, 'generator/About.html')
