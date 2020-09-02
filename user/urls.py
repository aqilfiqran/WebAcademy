
from django.urls import path
from .views import indexView, aboutView
from django.views.generic import TemplateView

app_name = "user"
urlpatterns = [
    path('', indexView, name='index'),  # localhost:8000/
    path('about', aboutView, name='about'),  # localhost:8000/about
    path('kelas', TemplateView.as_view(template_name="kelas.html"),
         name='kelas'),  # localhost:8000/kelas
]
