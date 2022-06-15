from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('addlivre/', views.formulaire, name='formulaire'),
    path('roman/', views.roman, name='roman'),
    path('bd/', views.bande_dessine, name='bds'),
    path('search/', views.recherche, name='recherche'),
    path('carousel/', views.jolie_carousel, name="carousel")
]
