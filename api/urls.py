from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

app_name = 'user'

router = DefaultRouter()
router.register('diary',views.DiaryViewSet)
router.register('recipe', views.RecipeViewSet)

urlpatterns = [
    path('register/', views.CreateUserView.as_view(), name='register'),
    path('',include(router.urls))
]