from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext as _
from . import models

class UserAdmin(BaseUserAdmin):
    ordering = ['id']
    list_display = ['email']
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal Info'), {'fields': ()}),
        (
            _('Permissions'),
            {
                'fields': (
                    'is_active',
                    'is_staff',
                    'is_superuser',
                )
            }
        ),
        (_('Important dates'), {'fields': ('last_login',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2')
        }),
    )
admin.site.register(models.User, UserAdmin)
admin.site.register(models.Diary)
admin.site.register(models.Recipe)
admin.site.register(models.RecipeKind)
admin.site.register(models.Vegetable)
admin.site.register(models.VegetableKind)
admin.site.register(models.Season)
admin.site.register(models.MainDish)