from django.urls import path
from projetos.views import index, page

urlpatterns = [
    path('', index, name='index'),
    path('page', page, name='page'),
    path('index', index, name='index'),
]
