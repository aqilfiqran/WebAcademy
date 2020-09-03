
from django.urls import path
from .views import (
    indexView,
    aboutView,
    ArticleList,
    ArticleDetail,
    KelasView,
    ArticleDelete,
    ArticleUpdate,
    ArticleCreate
)

app_name = "user"
urlpatterns = [
    path('', indexView, name='index'),  # localhost:8000/
    path('about', aboutView, name='about'),  # localhost:8000/about
    path('kelas', KelasView.as_view(),
         name='kelas'),  # localhost:8000/kelas
    path('artikel', ArticleList.as_view(), name='article'),
    path('artikel/create', ArticleCreate.as_view(), name='articleCreate'),
    path('artikel/<int:pk>', ArticleDetail.as_view(), name='articleDetail'),
    path('artikel/delete/<int:pk>', ArticleDelete, name='articleDelete'),
    path('artikel/update/<int:pk>', ArticleUpdate.as_view(), name='articleUpdate'),

]
