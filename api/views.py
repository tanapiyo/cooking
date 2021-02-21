from rest_framework import generics
from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from . import serializers
from .models import Diary, Recipe

from rest_framework_serializer_extensions.views import SerializerExtensionsAPIViewMixin

class CreateUserView(generics.CreateAPIView):
    serializer_class = serializers.UserSerializer
    permission_classes = (AllowAny,)#誰でもアクセスできるように

class DiaryViewSet(viewsets.ModelViewSet):
    queryset = Diary.objects.all()
    serializer_class = serializers.DiarySerializer

    def perform_create(self, serializer):#userProfileをreadonlyにしているので、それの割り当て
        serializer.save(userDiary=self.request.user)

class RecipeViewSet(SerializerExtensionsAPIViewMixin, viewsets.ModelViewSet):
    queryset = Recipe.objects.all()
    serializer_class = serializers.RecipeSerializer

    def perform_create(self, serializer):
        serializer.save(userRecipe=self.request.user)

# class RecipeViewSet(viewsets.ModelViewSet):
#     queryset = Recipe.objects.all()
#     serializer_class = serializers.RecipeSerializer
#
#     def perform_create(self, serializer):
#         serializer.save(userRecipe=self.request.user)


