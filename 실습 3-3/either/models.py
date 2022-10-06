from django.db import models


class Article(models.Model):
    title = models.CharField(max_length = 200)
    red = models.CharField(max_length = 100)
    blue = models.CharField(max_length = 100)

class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    pick = models.BooleanField(default=True)
    content = models.CharField(max_length = 100)