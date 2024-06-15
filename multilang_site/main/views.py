from django.shortcuts import render
from .models import Article

# Create your views here.

def accueil(request):
    return render(request, 'accueil.html')

def article_list(request):
    articles = Article.objects.all()
    return render(request, 'article_list.html', {'articles': articles})