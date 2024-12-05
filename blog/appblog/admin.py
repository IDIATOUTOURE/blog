from django.contrib import admin
from .models import Categorie, Tags, Auteur, Article

# Register your models here.
admin.site.register(Categorie)
admin.site.register(Tags)
admin.site.register(Auteur)
admin.site.register(Article)
