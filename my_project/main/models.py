from django.db import models

# Create your models here.


#Les articles et leur propriétés stokés dans la bdd
class Article(models.Model) : 
    title = models.CharField(max_length = 255)
    content = models.CharField(max_length = 255)
    publication_date = models.DateField()

#Le message pour la partie IA
class Message(models.Model):
        user_message = models.TextField()
        bot_message = models.TextField()    
        timestamp = models.DateTimeField(auto_now_add=True)