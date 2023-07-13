# from django.http import Http404, HttpResponse
# from utils.recipes.factory import make_recipe
import os

# Importar model .models, pq esta dentro da mesmo diretorio
from django.core.paginator import Paginator
from django.shortcuts import get_list_or_404, render

from recipes.models import Recipe

PER_PAGE = int(os.environ.get('PER_PAGE', 2))


# def home(request):

#     keywords = Posts.objects.filter(
#         is_published=True,
#     ).order_by('-id')
#     paginator = Paginator(keywords, PER_PAGE)  # Show 25 contacts per page.
#     page_number = request.GET.get("page")
#     page_obj = paginator.get_page(page_number)

#     return render(request, "blog/pages/home.html", {"page_obj": page_obj})


def home(request):
    keywords = Recipe.objects.all().order_by('-id')
    paginator = Paginator(keywords, PER_PAGE)  # Show 25 contacts per page.
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(request, 'recipes/pages/home.html', {"page_obj": page_obj})


# def category(request, category_id):
#     recipes = Recipe.objects.filter(
#         category__id=category_id
#     ).order_by('-id')

#     if not recipes:
#         return HttpResponse(content='Not found', status=404)
#         # raise Http404('Not found 🥲')

#     return render(request, 'recipes/pages/category.html', context={
#         'recipes': recipes,
#         'title': f'{recipes.first().category.name} - Category | '  # aula 62
#     })

def category(request, category_id):
    recipes = get_list_or_404(
        Recipe.objects.filter(
            category__id=category_id,
            is_published=True,
        ).order_by('-id')
    )

    return render(request, 'recipes/pages/category.html', context={
        'recipes': recipes,
        'title': f'{recipes[0].category.name} - Category | '
    })


def recipe(request, id):
    recipe = Recipe.objects.filter(
        pk=id,
        is_published=True,
    ).order_by('-id').first()

    return render(request, 'recipes/pages/recipe-view.html', context={
        'recipe': recipe,
        'is_detail_page': True,
    })
