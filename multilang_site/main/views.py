from django.shortcuts import render
import json
from django.http import HttpResponse
from .chat_gpt import get_chat_response
from django.conf import settings
from datetime import datetime
from django.shortcuts import render, get_object_or_404
from .models import Article
from .models import Message
import requests
#marquer le texte pour la localisation
from django.utils.translation import gettext as _

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


#Page de détail article
def article_detail(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    context = {
        'article': article,
        'current_year': datetime.now().year,
    }
    return render(request, 'article_detail.html', context)

#Vue du Chatbot
#Elle traitera les requêtes des utilisateurs et va renvoyer les réponses GPT
#La partie pour l'utilisateur
def chat_view(request):
    if request.method == "POST":
        user_message = request.POST.get('message')
        bot_message = get_ai_response(user_message)
        Message.objects.create(user_message=user_message, bot_message=bot_message)
    messages = Message.objects.all()
    return render(request, 'chatbot.html', {'messages': messages})

def get_ai_response(user_input: str) -> str:
    # Set up the API endpoint and headers
    endpoint = "https://api.openai.com/v1/chat/completions"
    headers = {
        "Authorization": "Bearer sk-proj-1CZXNIGuQWdrbnNtsOMaT3BlbkFJEyr4dWWRnmDHjzG8Xjf4",
        "Content-Type": "application/json",
    }

    # Data payload
    messages = get_existing_messages()
    messages.append({"role": "user", "content": f"{user_input}"})
    data = {
        "model": "gpt-3.5-turbo",
        "messages": messages,
        "temperature": 0.7
    }
    response = requests.post(endpoint, headers=headers, json=data)
    response_data = response.json()


    # Check if 'choices' key exists in response_data
    if 'choices' in response_data:
        ai_message = response_data['choices'][0]['message']['content']
    else:
        ai_message = "Une erreur est survenue."

    return ai_message

def get_existing_messages() -> list:
    """
    Get all messages from the database and format them for the API.
    """
    formatted_messages = []

    for message in Message.objects.values('user_message', 'bot_message'):
        formatted_messages.append({"role": "user", "content": message['user_message']})
        formatted_messages.append({"role": "assistant", "content": message['bot_message']})

    return formatted_messages
