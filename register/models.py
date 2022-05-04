from django.db import models
from django.forms import ModelForm

class user(models.Model):
    username = models.CharField(max_length = 100, verbose_name = 'USUÁRIO')
    cpf = models.CharField(max_length = 14, verbose_name = 'CPF')
    enrollment = models.CharField(max_length = 14, verbose_name = 'MATRÍCULA')
    email = models.EmailField(max_length = 70, verbose_name = 'E-MAIL')
    phone = models.CharField(max_length = 15, verbose_name = 'TELEFONE')

    def __str__(self):
        return self.username

class vehicle(models.Model):
    brand = models.CharField(max_length = 100, verbose_name ='MARCA')
    model = models.CharField(max_length = 100, verbose_name = 'MODELO')
    plate = models.CharField(max_length = 100, verbose_name = 'PLACA')
    color = models.CharField(max_length = 100, verbose_name = 'COR')
    user = models.ForeignKey(user, on_delete = models.CASCADE, null = True, blank = True, verbose_name = 'PROPRIETÁRIO')



    
    
    





