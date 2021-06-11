from django.db import models

# Create your models here.


from django.db import models
# Create your models here.


class csgo(models.Model):
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


class lol(models.Model):
    partida = models.CharField(max_length=200)
    resultado = models.CharField(max_length=200)
    personaje = models.CharField(max_length=200)
    img_personaje = models.CharField(max_length=200)
    KDA = models.CharField(max_length=200)
    score = models.CharField(max_length=200)
    duracion = models.CharField(max_length=200)
    fecha = models.CharField(max_length=200)
    nivel = models.CharField(max_length=200)
    minions = models.CharField(max_length=200)
    ckills = models.CharField(max_length=200)

