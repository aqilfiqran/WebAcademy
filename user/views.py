from django.shortcuts import render

# Create your views here.


def indexView(request):
    return render(request, 'index.html')


def aboutView(request):
    return render(request, 'about.html')
