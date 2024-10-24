from django.db import models
from django.forms import IntegerField

# Create your models here.

class Livro (models.Model):
    nome = models.CharField(max_length=100)
    autor = models.CharField(max_length=100)
    editora = models.CharField(max_length=100)
    anoPublicacao = IntegerField()
