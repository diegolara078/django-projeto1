from django.contrib import admin

# Register your models here.
from .models import Category, Recipe


# Criar uma classe herdando de admin.ModelAdmin
class CategoryAdmin(admin.ModelAdmin):
    ...


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    ...

    # Model e a Classe criada acima
admin.site.register(Category, CategoryAdmin)
