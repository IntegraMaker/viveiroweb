from django.db import models

# Create your models here.
class Planta(models.Model):
    id = models.AutoField(primary_key=True) 
    nome= models.CharField(max_length=250, unique=True) #unico
    nomeclatura = models.CharField(max_length=250, unique=True) #unico
    familia = models.CharField(max_length=250)
    nutricao = models.CharField(max_length=250)
    regiao = models.CharField(max_length=250)
    nativa = models.BooleanField(default=False) #não sabemos qual o critério para definir se é nativa ou não
    manejo = models.CharField(max_length=250) #depois pode ser um link de um video
    # pragas e doenças podem entrar depois

    def __str__(self):
        return self.nome
    
