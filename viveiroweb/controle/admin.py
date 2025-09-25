from django.contrib import admin
from django.db import models #upload de imagens
from .models import Planta, Reserva, acao_ensino

# Register your models here.
@admin.register(Planta)
class PlantaAdmin(admin.ModelAdmin):
    list_display = ('imagem', 'id', 'nome', 'nomeclatura', 'familia', 'nutricao', 'regiao', 'nativa', 'manejo')
    search_fields = ('nome', 'nomeclatura', 'familia','regiao')
    list_filter = ('nativa',)
    ordering = ('nome',)

@admin.register(Reserva)
class ReservaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'data', 'motivo', 'descricao', 'aceito', 'email', 'telefone')
    search_fields = ('nome', 'data', 'motivo')
    list_filter = ('data',)
    ordering = ('data',)

@admin.register(acao_ensino)
class acao_ensinoAdmin(admin.ModelAdmin):
    list_display = ('id', 'tipo')
    search_fields = ('tipo',)
    ordering = ('tipo',)