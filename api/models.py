from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.conf import settings

class UserManager(BaseUserManager):#email認証にかえる
    def create_user(self, email, password=None, **extra_friends):
        if not email:
            raise ValueError('email is must')
        user = self.model(email=self.normalize_email(email), **extra_friends)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self,email,password):
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=50, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'

    def __str__(self):
        return self.email

class Diary(models.Model):
    foodName = models.CharField(max_length=50)
    userDiary = models.ForeignKey(
        settings.AUTH_USER_MODEL, related_name='userDiary',
        on_delete=models.CASCADE
    )
    date = models.DateTimeField(auto_now_add=False)
    userDiary = models.ForeignKey(
        'Recipe', related_name='recipeDiary',
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.foodName

class Recipe(models.Model):
    foodName = models.CharField(max_length=50)
    vegetables  = models.ManyToManyField(Vegetable)
    main = modelsmodels.ForeignKey(
        'RecipeMain', related_name='recipeMain',
        on_delete=models.CASCADE
    )
    recipeKind = modelsmodels.ForeignKey(
        'RecipeKind', related_name='recipeKind',
        on_delete=models.CASCADE
    )
    memo = models.CharField(max_length=500)
    ajitsuke = models.CharField(max_length=50)
    cookingTime = models.IntegerField
    onomatopoeia = models.CharField(max_length=20)

    def __str__(self):
        return self.foodName

class Vegetable(models.Model):
    vegeName = models.CharField(max_length=50)
    kind = modelsmodels.ForeignKey(
        'VegetableKind', related_name='vegetableKind',
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.foodName

class VegetableKind(models.Model):
    kindName = models.CharField(max_length=50)

    def __str__(self):
        return self.kindName
    
class RecipeKind(models.Model):
    recipeName = models.CharField(max_length=50)

    def __str__(self):
        return self.recipeName

class Season(models.Model):
    seasonName = models.CharField(max_length=50)

    def __str__(self):
        return self.seasonName

class MainDish(models.Model):
    mainDishName = models.CharField(max_length=50)

    def __str__(self):
        return self.seasonName


