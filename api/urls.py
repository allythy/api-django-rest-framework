from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api.views import ArticleViewSet


router = DefaultRouter()
router.register('articles', ArticleViewSet)

urlpatterns = router.urls