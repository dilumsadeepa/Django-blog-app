from django.db import models
from django.utils import timezone


class Blog(models.Model):
    title = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    image = models.CharField(max_length=255)
    info = models.TextField()
    description = models.TextField()
    author = models.CharField(max_length=255)


class Post(models.Model):
    blog_id = models.CharField(max_length=255)
    published = models.CharField(max_length=255)


class Content(models.Model):
    title = models.CharField(max_length=255, default="blogisnotcomplete")
    image = models.CharField(max_length=255, default="noimage")
    info = models.TextField(default="NOinfo")
    description = models.TextField(default="none")
    author = models.CharField(max_length=255, default="some_editor")
