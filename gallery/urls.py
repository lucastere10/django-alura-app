from django.urls import path, include
from gallery.views import index, imagem


urlpatterns = [
    path('', index, name = 'index'),
    path('imagem/', imagem, name = 'imagem')
]