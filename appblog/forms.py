from django import forms

from .models import Article, Categorie, Auteur

class ArticleForm(forms.ModelForm):

    class Meta:
        model = Article
        fields = "__all__"

class CategoriesForm(forms.ModelForm):

    class Meta:
        model = Categorie    
        fields = "__all__"    

class AuteurForm(forms.ModelForm):

    class Meta:
        model = Auteur
        fields = "__all__"