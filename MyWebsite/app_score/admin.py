from django.contrib import admin
from .models import Stats


@admin.register(Stats)
class StatsAdmin(admin.ModelAdmin):
    list_display = ('resultado', 'nom_equipo', 'score', 'K_A_D', 'K_R', 'K_D', 'HS', 'mapa', 'fecha', 'elo')
