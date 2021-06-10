from django.db import models

# Create your models here.


from django.db import models
# Create your models here.
class Stats(models.Model):

    resultado = models.CharField(max_length=200)
    nom_equipo = models.CharField(max_length=200)
    score = models.CharField(max_length=200)
    K_A_D = models.CharField(max_length=200)
    K_R = models.CharField(max_length=200)
    K_D = models.CharField(max_length=200)
    HS = models.CharField(max_length=200)
    mapa = models.CharField(max_length=200)
    fecha = models.CharField(max_length=200)
    elo = models.CharField(max_length=200)

