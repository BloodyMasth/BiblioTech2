from django.db import models
from django.contrib import admin


# Create your models here.
class Livre(models.Model):
    titre = models.CharField(max_length=255)
    tome = models.IntegerField()
    auteur = models.CharField(max_length=255)
    serie = models.CharField(max_length=255)
    genre = models.CharField(max_length=55)
    image_url = models.CharField(max_length=2085)


class LivreAdmin(admin.ModelAdmin):
    list_display = ("titre", "tome", "auteur")
    list_filter = ("auteur", "serie", "genre")

