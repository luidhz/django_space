from django.urls import path
from galeria.views import index, imagem, buscar, filtrar_por_tag

urlpatterns = [
    path('', index, name='index'),
    path('imagem/<int:foto_id>', imagem, name='imagem'),
    path('buscar', buscar, name='buscar'),
    path('tag/<str:tag_nome>/', filtrar_por_tag, name='filtrar_por_tag'),
]