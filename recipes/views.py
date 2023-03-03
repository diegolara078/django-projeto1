# from django.http import Http404, HttpResponse
# from utils.recipes.factory import make_recipe
from django.shortcuts import get_list_or_404, render

# Importar model .models, pq esta dentro da mesmo diretorio
from recipes.models import Recipe

# from utils.recipes.factory import make_recipe


# Para teste importado do factory#
# def home(request):
#   return render(request, 'recipes/pages/home.html', context={
#       'recipes': [make_recipe() for _ in range(9)],
#   })

# def recipe(request, id):
#   return render(request, 'recipes/pages/recipe-view.html', context={
#      'recipe': make_recipe(),
#     'is_detail_page': True,
#  })


def home(request):
    recipes = Recipe.objects.all().order_by('-id')
    return render(request, 'recipes/pages/home.html', context={
        'recipes': recipes,
    })


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
