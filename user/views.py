from django.shortcuts import render

# Create your views here.


def indexView(request):
    context = {
        'title': 'WebAcademy | index',

    }
    return render(request, 'index.html', context)


def aboutView(request):
    context = {
        'title': 'WebAcademy | about'
    }
    return render(request, 'about.html', context)
