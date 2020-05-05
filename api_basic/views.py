# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .models import Article, ArticleType, Author
from .serializers import ArticleSerializer, ArticleTypeSerializer, AuthorSerializer
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.decorators import APIView
from rest_framework.response import Response
from rest_framework import mixins
from rest_framework import generics
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework import permissions
from rest_framework import viewsets
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from utility.behaviours import CreateRetrieveUpdateListModelViewSet, RetrieveModelViewSet


# Create your views here.
class ArticleViewSet(CreateRetrieveUpdateListModelViewSet):
    serializer_class = ArticleSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    queryset = Article.objects.all().order_by("id")


class ArticleTypeViewSet(CreateRetrieveUpdateListModelViewSet):
    serializer_class = ArticleTypeSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    queryset = ArticleType.objects.all().order_by("id")


class AuthorViewSet(CreateRetrieveUpdateListModelViewSet):
    serializer_class = AuthorSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    queryset = Author.objects.all().order_by("id")


# ////////////////////////////////////////////////////////////////////////////////////////////////////////

# class ArticleModelViewSet(viewsets.ModelViewSet):
#     serializer_class = ArticleSerializer
#     queryset = Article.objects.all()
#
# class ArticleGenericViewSet(viewsets.GenericViewSet,mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView,
#                      mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin):
#     serializer_class = ArticleSerializer
#     queryset = Article.objects.all()
#
# class ArticleViewSet(viewsets.ViewSet):
#     def list(self, request):
#         article = Article.objects.all()
#         serializer = ArticleSerializer(article, many=True)
#         return Response(serializer.data)
#
#     def create(self, request):
#         serializer = ArticleSerializer(data=request.data)
#
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def retrieve(self, request, pk=None):
#         queryset = Article.objects.all()
#         article = get_object_or_404(queryset, pk=pk)
#         serializer = ArticleSerializer(article)
#         return Response(serializer.data)
#
#     def update(self, request, pk=None):
#         article = Article.objects.all(pk=pk)
#         serializer = ArticleSerializer(article, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#
# class GenericAPIView(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView,
#                      mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin):
#
#     queryset = Article.objects.all()
#     serializer_class = ArticleSerializer
#
#     lookup_field = 'id'
#     authentication_classes = [SessionAuthentication,BasicAuthentication,TokenAuthentication]
#     # authentication_classes = [TokenAuthentication]
#     permission_classes = [permissions.IsAuthenticated]
#
#     def get(self, request, id =None):
#
#         if id:
#             return self.retrieve(request)
#
#         else:
#             return self.list(request)
#
#     def post(self, request):
#         return self.create(request)
#
#     def put(self, request, id=None):
#         return self.update(request,id)
#
#     def delete(self, request, id):
#         return self.destroy(request,id)
#
# # class ArticleDetail(mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,generics.GenericAPIView):
# #
# #     queryset = Article.objects.all()
# #     serializer_class = ArticleSerializer
# #
# #     def get(self, request):
# #         return self.retrieve(request)
# #
# #     def put(self, request, *args, **kwargs):
# #         return self.update(request)
# #
# #     def delete(self, request, *args, **kwargs):
# #         return self.destroy(request)
#
# class ArticleList(APIView):
#     """
#     List all Articles, or create a new snippet.
#     """
#     def get(self, request, format=None):
#         article = Article.objects.all()
#         serializer = ArticleSerializer(article, many=True)
#         return Response(serializer.data)
#
#     def post(self, request, format=None):
#         serializer = ArticleSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
# class ArticleDetail(APIView):
#     """
#     Retrieve, update or delete a Article instance.
#     """
#     def get_object(self, pk):
#         try:
#             return Article.objects.get(pk=pk)
#         except Article.DoesNotExist:
#             raise status.HTTP_400_BAD_REQUEST
#
#     def get(self, request, pk, format=None):
#         article = self.get_object(pk)
#         serializer = ArticleSerializer(article)
#         return Response(serializer.data)
#
#     def put(self, request, pk, format=None):
#         article = self.get_object(pk)
#         serializer = ArticleSerializer(article, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def delete(self, request, pk, format=None):
#         article = self.get_object(pk)
#         article.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
#
# @api_view(['GET', 'POST'])
# def article_list(request):
#     """
#     List all code Articles, or create a new snippet.
#     """
#     if request.method == 'GET':
#         article = Article.objects.all()
#         serializer = ArticleSerializer(article, many=True)
#         return Response(serializer.data)
#
#     elif request.method == 'POST':
#         # data = JSONParser().parse(request)
#         serializer = ArticleSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#
# @api_view(['GET', 'PUT', 'DELETE'])
# def article_detail(request, pk):
#     """
#     Retrieve, update or delete a code Article.
#     """
#     try:
#         article = Article.objects.get(pk=pk)
#     except Article.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
#
#     if request.method == 'GET':
#         serializer = ArticleSerializer(article)
#         return Response(serializer.data)
#
#     elif request.method == 'PUT':
#         serializer = ArticleSerializer(article, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     elif request.method == 'DELETE':
#         article.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
