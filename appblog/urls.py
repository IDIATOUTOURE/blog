from django.urls import path
from .views import *

urlpatterns =[
    path('', index, name='index'),
    path('article_detail/<int:article_id>/', article_detail, name='article_detail'),
    path('article-by-categorie/<int:categorie_id>/', article_by_categorie, name="article_by_categorie"),

   
    # urls the backoffice
    path('dashboard/', dashboard, name='dashboard'),
    path('dashboard/article/liste/', article_liste, name='article_liste'),
    path('dashboard/article/add/', article_create, name='article_create'),
    path('dashboard/article/update/<int:article_id>/', article_update, name='article_update'),
    path('dashboard/article/delete/<int:article_id>/', article_delete, name='article_delete'),
    path('categories/article/cat',categorie, name='categorie'),
    path('dashboard/categorie/update/<int:categorie_id>/', categorie_update, name='categorie_update'),
    path('dashboard/categorie/delete/<int:categorie_id>/', categorie_delete, name='categorie_delete'),
    path('auteur/',auteur_liste, name='auteur_liste'),
    path('dashboard/auteur/add/', auteur_create, name='auteur_create'),

    path('dashboard/auteur/update/<int:auteur_id>/', auteur_update, name='auteur_update'),
    path('dashboard/auteur/delete/<int:auteur_id>/', auteur_delete, name='auteur_delete'),

]
