from django.contrib import admin
from .models import Livre, LivreAdmin


# Register your models here.
admin.site.register(Livre, LivreAdmin)
