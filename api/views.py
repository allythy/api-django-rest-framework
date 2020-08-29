from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import DjangoModelPermissionsOrAnonReadOnly
from api.models import Article
from api.serializers import ArticleSerializer


class ArticleViewSet(ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
