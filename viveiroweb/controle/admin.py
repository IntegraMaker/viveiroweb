from django.contrib import admin
from django.db import models #upload de imagens
from .models import Planta, Reserva, AcaoEnsino

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
    list_editable = ("aceito",)  # permite editar o campo diretamente da lista
    search_fields = ('nome', 'data', 'motivo')
    list_filter = ('data',)
    ordering = ('data',)

@admin.register(AcaoEnsino)
class AcaoEnsinoAdmin(admin.ModelAdmin):
    list_display = ('id', 'tipo', 'nome', 'descricao', 'aceito')
    list_editable = ("aceito",) 
    search_fields = ('tipo', 'nome')
    ordering = ('tipo',)