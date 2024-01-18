from django.db import models
from django.contrib.auth.models import User
from uuid import uuid4
from django.utils import timezone

class Curso(models.Model):
    codigo = models.CharField(primary_key=True, max_length=6)
    nombre = models.CharField(max_length=50)
    creditos = models.PositiveSmallIntegerField()

    def __str__(self):
        texto = "{0} ({1})"
        return texto.format(self.nombre, self.creditos)
    
    
class Chat(models.Model):
    code = models.CharField(primary_key=True, max_length=6)
    quetion = models.CharField(max_length=500)
    answer = models.CharField(max_length=500) 
    address = models.CharField(max_length=500) 
    course = models.CharField(max_length=500) 
    year = models.CharField(max_length=500) 
    date = models.DateField()

    def __str__(self):
        texto = "{0} ({1})"
        return texto.format(self.code, self.quetion)    
    
    
class User(models.Model):
    code = models.CharField(primary_key=True, max_length=6)
    username = models.CharField(max_length=500)
    firtname = models.CharField(max_length=500)
    lastname = models.CharField(max_length=500) 
    email = models.CharField(max_length=500) 
    password = models.CharField(max_length=500) 

    def __str__(self):
        texto = "{0} ({1})"
        return texto.format(self.username, self.firtname)
    


# Create your models here.
class QuestionAnswer(models.Model):
    code = models.CharField(primary_key=True, max_length=26)
    question = models.CharField(max_length=1000)
    answer = models.TextField()
    course = models.CharField(max_length=1000)
    year_level = models.CharField(max_length=1000)
    user = models.CharField(max_length=1000)
    session = models.CharField(max_length=1000)
    feedback = models.CharField(max_length=1000)
    created = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.question
    
class Rating(models.Model):
    stars = models.IntegerField()
    comment = models.TextField()
    year_level = models.IntegerField()
