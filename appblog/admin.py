from django.contrib import admin
from appblog.models import Auteur,Categorie,Tags,Article

# Register your models here.
admin.site.register(Auteur)
admin.site.register(Categorie)
admin.site.register(Tags)
admin.site.register(Article)
