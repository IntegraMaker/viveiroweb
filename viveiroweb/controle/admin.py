from django.contrib import admin
from .models import Planta

# Register your models here.
@admin.register(Planta)
class PlantaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'nomeclatura', 'familia', 'nutricao', 'regiao', 'nativa', 'manejo')
    search_fields = ('nome', 'nomeclatura', 'familia','regiao')
    list_filter = ('nativa',)
    ordering = ('nome',)