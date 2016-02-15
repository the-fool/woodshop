from django.db import models

class User(models.Model):
    pass

class Gem(models.Model):
    text = models.TextField(default='')
    author = models.ForeignKey(User, default=None)
