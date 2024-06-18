from django.shortcuts import render
from datetime import datetime
from .models import Article


# Create your views here.

def accueil(request):
    articles = Article.objects.all().order_by('-publication_date')  # Récupère tous les articles depuis la base de données
    context = {
        'articles': articles,
        'current_year': datetime.now().year,
    }
    return render(request, 'accueil.html', context)
    return render(request, 'accueil.html', {'posts': posts})  # Passe detaile des articles au template

def article_detail(request, id):
    articles = Article.objects.all()
    return render(request, 'article_detail.html', {'articles': articles})

