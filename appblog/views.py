from django.shortcuts import render, redirect
from .models import Categorie, Article,Auteur
from .forms import ArticleForm,AuteurForm,CategoriesForm

# Create your views here.
#  view frontoffice
def index(request):
    categories = Categorie.objects.all()
    article_liste = Article.objects.all().order_by('-date_creation')
    article_en_avant = Article.objects.filter(en_avant=True).first()
    print(categories)

    context = {
        'categories':categories,
        "articles" : article_liste,
        "article_en_avant" : article_en_avant
        }

    return render(request, "blog/frontoffice/index.html", context)


def article_detail(request, article_id):
    categories = Categorie.objects.all()
    categories = Categorie.objects.all()
    article = Article.objects.get(id=article_id)
    


    context = {
        
        "categories" : categories,
        'article':article 
    }

    return render(request, "blog/frontoffice/article_detail.html", context)


def article_by_categorie(request, categorie_id):
    categories = Categorie.objects.all()
    categorie = Categorie.objects.get(id=categorie_id)
    article_en_avant = Article.objects.filter(en_avant=True).first()

    articles = Article.objects.filter(categorie=categorie)
    context = {
        "categories":categories,
        "articles": articles,
        "article_en_avant" : article_en_avant

    }

    return render(request, "blog/frontoffice/article_by_categorie.html", context)

    # views backoffices

def dashboard(request):
    nbre_articles = Article.objects.all().count()
    nbre_auteurs = Auteur.objects.all().count()
    context = {
        "nbre_article":nbre_articles,
        "nbre_auteurs":nbre_auteurs
    }

    return render(request, "blog/backoffice/dashboard.html", context)


def article_liste(request):
    articles = Article.objects.all()
    context = {
        'articles' : articles
    }
    return render(request, "blog/backoffice/article_liste.html", context)

def article_create(request):
    form = ArticleForm()
    
    if request.method == "POST":
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            print("Article ajouté avec success")
            return redirect('article_liste')

    context = {
        'form' : form
    }


    return render(request, "blog/backoffice/article_create.html", context)


def article_update(request, article_id):
    article = Article.objects.get(id= article_id)

    form = ArticleForm(instance=article)
    
    if request.method == "POST":
        form = ArticleForm(instance=article, data = request.POST, files= request.FILES)
        if form.is_valid():
            form.save()
            print("Article modifié avec success")
            return redirect('article_liste')

    context = {
        'form' : form
    }


    return render(request, "blog/backoffice/article_update.html", context)

def article_delete(request, article_id):
    article = Article.objects.get(id= article_id)
    article.delete()
    return redirect('article_liste')

def categorie(request):
    categories = Categorie.objects.all()
    context = {
        'categories' : categories
    }
    return render(request, "blog/backoffice/categorie.html", context)


def categorie_update(request, categorie_id):
    categorie = Categorie.objects.get(id= categorie_id)

    form = ArticleForm(instance=categorie)
    
    if request.method == "POST":
        form = CategoriesForm(instance=categorie, data = request.POST, files= request.FILES)
        if form.is_valid():
            form.save()
            print("Article modifié avec success")
            return redirect('categorie')

    context = {
        'form' : form
    }

    return render(request, "blog/backoffice/categorie_update.html", context)

def categorie_delete(request, categorie_id):
    categorie = Categorie.objects.get(id= categorie_id)
    categorie.delete()
    return redirect('categorie')    


def auteur_liste(request):
    auteurs = Auteur.objects.all()
    context = {
        'auteurs' : auteurs
    }
    return render(request, "blog/backoffice/auteur_liste.html", context)

def auteur_create(request):
    form = AuteurForm()
    
    if request.method == "POST":
        form = AuteurForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            print("auteur ajouté avec success")
            return redirect('auteur_liste')

    context = {
        'form' : form
    }


    return render(request, "blog/backoffice/auteur_create.html", context)


def auteur_update(request, auteur_id):
    auteur = Auteur.objects.get(id= auteur_id)

    form = AuteurForm(instance=auteur)
    
    if request.method == "POST":
        form = AuteurForm(instance=auteur, data = request.POST, files= request.FILES)
        if form.is_valid():
            form.save()
            print("auteur modifié avec success")
            return redirect('auteur_liste')

    context = {
        'form' : form
    }


    return render(request, "blog/backoffice/auteur_update.html", context)


def auteur_delete(request, auteur_id): 

    auteur = Auteur.objects.get(id= auteur_id)
    auteur.delete()
    return redirect('auteur_liste')
