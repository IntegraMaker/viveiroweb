from django.db import models
# Create your models here.
class Planta(models.Model):
    id = models.AutoField(primary_key=True)
    imagem = models.ImageField(upload_to='media/', null=True, blank=True) 
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
    
class Reserva(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=250)
    telefone = models.CharField(max_length=20, default='(00) 00000-0000') #colocar uma validação melhor depois
    data = models.DateField() #cada reserva só pode ter uma data diferente da outras
    motivo = models.CharField(max_length= 250)
    descricao = models.CharField(max_length= 250, null=True, blank=True)
    aceito = models.BooleanField(default=False) #comeca como falso, o admin aprova depois
    email = models.EmailField() 
   

    def __str__(self):
        return f"{self.nome} - {self.data}"

class AcaoEnsino(models.Model): #vai precisar de quem pediu a ação?
    id = models.AutoField(primary_key=True) #data? motivo? etc...
    tipo = models.CharField(max_length=250)
    nome= models.CharField(max_length=250, unique=True) #unico
    autores = models.CharField(max_length=250,default='Autor Desconhecido') #vários autores separados por vírgula
    descricao = models.CharField(max_length=250, null=True, blank=True)
    aceito = models.BooleanField(default=False) #comeca como falso, o admin aprova depois
    

    def __str__(self):
        return self.tipo