"""core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include
from .views import ArticleViewSet
from rest_framework.routers import DefaultRouter
# from .views import GenericAPIView
# from .views import ArticleAPIView, ArticleDetails, GenericAPIView
# from .views import article_list, article_detail

# urlpatterns = [
#     path('article/', article_list),
#     path('detail/<int:pk>/', article_detail),
# ]

# urlpatterns = [
# path('article/', ArticleAPIView.as_view()),
# path('detail/<int:pk>/', ArticleDetails.as_view()),
# path('generic/article/<int:pk>/', GenericAPIView.as_view()),
# ]

router = DefaultRouter()
router.register('article', ArticleViewSet, basename='article')

urlpatterns = [
    path('viewset/', include(router.urls)),
    path('viewset/<int:pk>/', include(router.urls)),
]