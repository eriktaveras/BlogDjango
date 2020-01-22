from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField(default='')

class lucha(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField(default='')


def __str__(self):
        return self.title