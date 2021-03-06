# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models


class Article(models.Model):

    title = models.CharField(max_length=100)
    slug = models.SlugField()
    body = models.TextField()
    date = models.DateField(auto_now_add=True)
    thumb = models.ImageField(default='default.png', blank=True)

    def __str__(self):
        return self.title

    def snippet(self):
        return self.body[:50] + '...'

# TODO: Add in author later