
from django.urls import path
from .views import indexView, aboutView

urlpatterns = [
    path('', indexView, name='index'),  # localhost:8000/
    path('about', aboutView, name='about'),  # localhost:8000/
]
