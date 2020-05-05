# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


# Create your models here.
class ArticleType(models.Model):
    name = models.CharField(
        max_length=256,
        verbose_name="Article Type Name"
    )

    def __str__(self):
        return self.name

    class Meta:
        db_table = "article_type"
        verbose_name = "Article Type"


class Author(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name='Author'
    )

    email = models.EmailField(
        max_length=100,
        verbose_name='Email'
    )

    def __str__(self):
        return self.name

    class Meta:
        db_table = "author"
        verbose_name = "Author"
        verbose_name_plural = "Authors"


class Article(models.Model):
    article_type = models.ForeignKey(
        ArticleType,
        on_delete=models.CASCADE,
        related_name='articles'
    )

    author = models.ForeignKey(
        Author,
        on_delete=models.CASCADE,
        related_name='articles'
    )

    title = models.CharField(
        max_length=100,
        verbose_name='Article Title'
    )

    def __str__(self):
        return self.title

    class Meta:
        db_table = "articles"
        verbose_name = "Article"
        verbose_name_plural = "Articles"
        unique_together = ("title", "article_type")
