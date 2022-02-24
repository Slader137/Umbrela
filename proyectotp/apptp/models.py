from django.db import models

# Create your models here.
class Persona(models.Model):

    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=60)
    sexo = models.CharField(max_length=10)
    nacimiento = models.CharField(max_length=50)
    foto = models.ImageField(
        upload_to = 'foto/%Y/%m/%d',
        blank = True,
        verbose_name = ('Foto de la persona')
    )
    dni = models.CharField(max_length=50, unique = True, default="2")
    telefono = models.CharField(max_length=50, unique = True, default="2")
    

class Meta:
    verbose_name = ('Persona')
    verbose_name_plural = ('Persona')
    
    

def __str__(self):
    return self.nombre


    
