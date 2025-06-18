from django.contrib import admin
from .models import Planta, Reserva

# Register your models here.
@admin.register(Planta)
class PlantaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'nomeclatura', 'familia', 'nutricao', 'regiao', 'nativa', 'manejo')
    search_fields = ('nome', 'nomeclatura', 'familia','regiao')
    list_filter = ('nativa',)
    ordering = ('nome',)

@admin.register(Reserva)
class ReservaAdmin(admin.ModelAdmin):
    list_display = ('id', 'solicitante', 'data', 'motivo', 'obs', 'aceito', 'email')
    search_fields = ('solicitante', 'data', 'motivo')
    list_filter = ('data',)
    ordering = ('data',)