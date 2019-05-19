from django.db import models

# Create your models here.

class Cadastro (models.Model):

    nome = models.CharField(max_length=120)
    email = models.EmailField()
    CPF = models.IntegerField()
    login = models.CharField(max_length=50)
    senha = models.CharField(max_length=50)

def __str__(self):
        return self.nome