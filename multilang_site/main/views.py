import requests
from django.shortcuts import render
from django.http import JsonResponse
from django.conf import settings
from datetime import datetime
from .models import Article
#marquer le texte pour la localisation
from django.utils.translation import gettext as _
from django.utils import timezone

# Create your views here.

#Page d'accueil
def accueil(request):
    articles = Article.objects.all().order_by('-publication_date')  # Récupère tous les articles depuis la base de données
    context = {
        'articles': articles,
        'redirect_to': request.path,  # URL actuelle pour redirection après changement de langue
        'current_year': datetime.now().year,
    }
    return render(request, 'accueil.html', context)
    # return render(request, 'accueil.html', {'posts': posts})  # Passe detaile des articles au template

def article_detail(request, id):
    articles = Article.objects.all()
    return render(request, 'article_detail.html', {'articles': articles})


#Vue du Chatbot
#Elle traitera les requêtes des utilisateurs et va renvoyer les réponses GPT

def chatbot_view(request):
    if request.method == 'POST':
        user_input = request.POST.get('user_input')
        response_text = get_gpt_response(user_input)
        return JsonResponse({'response': response_text})

    return render(request, 'chatbot.html')

def get_gpt_response(prompt):
    api_key = settings.OPENAI_API_KEY
    url = 'https://api.openai.com/v1/completions'
    headers = {
        'Authorization': f'Bearer {api_key}',
        'Content-Type': 'application/json'
    }
    data = {
        'model': 'text-davinci-003',  # Assurez-vous d'utiliser le bon modèle
        'prompt': prompt,
        'max_tokens': 150
    }

    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 200:
        return response.json()['choices'][0]['text'].strip()
    else:
        return "Sorry, I couldn't process your request."