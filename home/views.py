from django.shortcuts import render


def reception(request):
    return render(request, 'home/reception.html')


def index(request):
    return render(request, 'home/index.html')
