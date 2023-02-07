from django.shortcuts import render

from utils.recipes.factory import make_recipe


def home(request):
    return render(request, 'recipes/pages/home.html', context={
        #  for _ in range(10) vai gerar 10 Receitas do importe faker
        'recipes': [make_recipe() for _ in range(9)],
    })

# Passar paremetros, nesse caso a baixo passamos um int no arquivo urls.py
# Isso serve para minimizar ataques e possiveis erros
# https://docs.djangoproject.com/pt-br/3.2/topics/http/urls/


def recipe(request, id):
    return render(request, 'recipes/pages/recipe-view.html', context={
        'recipe': make_recipe(),
    })
# def contado(request):
#     return render(request, 'recipes/contato.html')


# def sobre(request):
#     return render(request, 'recipes/sobre.html')
