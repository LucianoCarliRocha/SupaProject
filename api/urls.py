from django.urls import path

from . import views
from django.http import HttpResponse

def livros (request):
    return HttpResponse("livros")

urlpatterns = [
     path('livros/', views.getLivros),
     path('livros/<int:id>', views.LivroById),
]