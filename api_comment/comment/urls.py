from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CommentViewSet, PostViewSet


router = DefaultRouter()
router.register('comment', CommentViewSet, basename='comment')
router.register('post', PostViewSet, basename='post')

urlpatterns = [
    path("", include(router.urls))
]