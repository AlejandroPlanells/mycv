from django.contrib import admin
from .models import csgo, lol


@admin.register(csgo)
class CsgoStatsAdmin(admin.ModelAdmin):
    list_display = ('resultado', 'nom_equipo', 'score', 'K_A_D', 'K_R', 'K_D', 'HS', 'mapa', 'fecha', 'elo')


@admin.register(lol)
class LolStatsAdmin(admin.ModelAdmin):
    list_display = ('partida', 'resultado', 'personaje', 'img_personaje', 'KDA', 'score', 'duracion', 'fecha', 'nivel', 'minions', 'ckills')