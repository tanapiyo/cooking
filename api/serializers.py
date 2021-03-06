from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import Diary, Recipe, Vegetable, MainDish

from rest_framework_serializer_extensions.serializers import SerializerExtensionsMixin

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = get_user_model()
        fields = ('id','email','password')
        extra_kwargs= {'password': {'write_only': True}}

    def create(self, validated_data):
        user = get_user_model().objects.create_user(**validated_data)
        return user

class DiarySerializer(serializers.ModelSerializer):
    class Meta:
        model=Diary
        fields = ('foodName', 'userDiary', 'date', 'memo')
        extra_kwargs = {'userDiary': {'read_only': True}}

class VegetableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vegetable
        fields = ('vegeName', 'kind')
        extra_kwargs = {'kind': {'read_only': True}}

class MainDishSerializer(serializers.ModelSerializer):
    class Meta:
        model = MainDish
        fields = ('mainDishName',)#1つでも,ないとエラーになる

class RecipeSerializer(SerializerExtensionsMixin, serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = ('foodName', 'main', 'recipeKind', 'memo','ajitsuke', 'cookingTime',
                  'onomatopoeia', 'userRecipe')
        expandable_fields = dict(
            vegetables=dict(
                serializer=VegetableSerializer,
                many=True
            ),
            main=MainDishSerializer,
        )
        extra_kwargs = {'userRecipe': {'read_only': True}}

# class RecipeSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Recipe
#         fields = ('foodName', 'vegetables', 'main', 'recipeKind', 'memo','ajitsuke', 'cookingTime',
#                   'onomatopoeia', 'userRecipe')
#         extra_kwargs = {'userRecipe': {'read_only': True}}



