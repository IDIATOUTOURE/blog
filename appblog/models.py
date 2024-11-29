from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Categorie(models.Model):
    nom = models.CharField(max_length=150)
    def __str__(self):
        return self.nom

class Tags(models.Model):
    nom = models.CharField(max_length=150)
    code_couleur = models.CharField(max_length=70)  
    def __str__(self):
        return self.nom     

class Auteur(models.Model):
    utilisateur = models.OneToOneField(User,on_delete=models.CASCADE,null=True,blank=True)  
    nomComplet = models.CharField(max_length=150)
    email = models.EmailField(max_length=100)
    adresse = models.TextField()
    def __str__(self):
        return self.nomComplet


class Article(models.Model):
    titre = models.CharField(max_length=200)
    contenu = models.TextField()
    date_creation = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='img/',null =True,blank = True)
    auteur =models.ForeignKey(Auteur,on_delete=models.CASCADE)
    categorie = models.ForeignKey(Categorie,on_delete=models.CASCADE,default=1)
    tags = models.ManyToManyField(Tags, blank = True)
    en_avant = models.BooleanField(default=False)
    def __str__(self):
        return self.titre

class Commentaire(models.Model):
    article=models.ForeignKey(Article, on_delete=models.CASCADE)
    text = models.TextField()
    date_commentaire=models.DateTimeField(auto_now_add=True)
    date_acceptation=models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.article
