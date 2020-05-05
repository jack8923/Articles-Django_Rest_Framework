from abc import ABC

from rest_framework import serializers
from .models import Article, ArticleType, Author
from django.db import transaction
from .helpers.article_helper import ArticleHelper
from .helpers.author_helper import AuthorHelper
from .helpers.article_type_helper import ArticleTypeHelper
from django.db.utils import IntegrityError
from utility.behaviours import DynamicFieldsMixin



# class ArticleSerializer(serializers.Serializer):
#     title = serializers.CharField(max_length=100)
#     author = serializers.CharField(max_length=100)
#     email = serializers.EmailField(max_length=100)
#
#     def create(self, validated_data):
#         """
#         Create and return a new `Article` instance, given the validated data.
#         """
#         return Article.objects.create(validated_data)
#
#     def update(self, instance, validated_data):
#         """
#         Update and return an existing `Article` instance, given the validated data.
#         """
#         instance.title = validated_data.get('title', instance.title)
#         instance.author = validated_data.get('author', instance.author)
#         instance.email = validated_data.get('email', instance.email)
#         instance.save()
#         return instance

class ArticleSerializer(DynamicFieldsMixin,serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ('id', 'title', 'author', 'article_type')

    def create(self, validated_data):
        try:
            with transaction.atomic():
                article = Article.objects.create(title=validated_data.get('title'), author=validated_data.get('author'),
                                                 article_type=validated_data.get('article_type'))
        except IntegrityError:
            print('Integrity Error')

        return article

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.author = validated_data.get('author', instance.author)
        instance.article_type = validated_data.get('article_type', instance.article_type)

        initial_value = self.initial_data
        ArticleHelper.create_or_update(instance, initial_value)

        instance.save()
        return instance

    def validate(self, data):
        # print('validate mein ghus gaya')
        # ArticleHelper.cneck_title_unique(data)
        validated_data = super().validate(data)
        return validated_data


class ArticleTypeSerializer(DynamicFieldsMixin,serializers.ModelSerializer):
    # articles = ArticleSerializer(many=True)

    class Meta:
        model = ArticleType
        fields = ('id', 'name')

    def create(self, validated_data):
        # articles = validated_data.get('articles',None)
        try:
            with transaction.atomic():
                article_type = ArticleType.objects.create(name=validated_data.get('name'))
        except IntegrityError:
            print('Integrity Error')

        return article_type

    def update(self, instance, validated_data):
        print('update mein')
        instance.name = validated_data.get('name', instance.name)

        # initial_values = self.initial_data.get('articles')

        # article_type_helper.update_or_create(instance,initial_values)

        instance.save()
        return instance

    def validate(self, data):
        # duplicate entries
        print('validate')
        ArticleTypeHelper.check_unique(data.get('name'))
        validated_data = super().validate(data)
        return validated_data


class AuthorSerializer(DynamicFieldsMixin,serializers.ModelSerializer):
    # articles = ArticleSerializer(many=True)

    class Meta:
        model = Author
        fields = ('id', 'name', 'email')

    def create(self, validated_data):
        try:
            with transaction.atomic():
                author = Author.objects.create(name=validated_data.get('name'), email=validated_data.get('email'))
        except IntegrityError:
            print('Integrity Error')

        return author

    def update(self, instance, validated_data):
        print('update')
        instance.name = validated_data.get('name', instance.name)
        instance.email = validated_data.get('email', instance.email)
        instance.save()
        return instance

    def validate(self, data):
        #     Duplicate entries
        #     same name with two emails
        # AuthorHelper.check_unique(data.get.all())
        print('validate')
        validated_data = super().validate(data)
        return validated_data

