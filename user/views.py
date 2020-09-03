from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, TemplateView
from .models import Article
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


class ArticleList(ListView):
    template_name = 'user/list.html'
    model = Article
    ordering = ['-updated_at']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'WebAcademy | List'
        return context


class ArticleDetail(DetailView):
    template_name = 'user/detail.html'
    model = Article

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'WebAcademy | Detail'
        return context


class KelasView(TemplateView):
    template_name = 'kelas.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'WebAcademy | Kelas'
        return context


def ArticleDelete(request, *args, **kwargs):
    Article.objects.filter(id=kwargs['pk']).delete()
    return redirect('user:article')
