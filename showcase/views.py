from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'showcase/home/index.html')

def war(request):
    return render(request, 'showcase/war/index.html')

def calc(request):
    return render(request, 'showcase/calc/index.html')
