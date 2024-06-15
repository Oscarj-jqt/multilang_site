from django.db import models

# Create your models here.


class Article(models.Model) : 
    title = models.CharField(max_length = 50)
    content = models.CharField(max_length = 255)
    publication_date = models.DateField()