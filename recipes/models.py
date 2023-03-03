from django.contrib.auth.models import User
from django.db import models

# 1° Criar as tabelas e a relação entre elas, caso tenha imagens "py manage.py makemigrations"
# 2° Comando para migrar e criar as tabelas "py manage.py migrate"
# 3° Criar o arquivo no diretorio o 0001_initial.py "py manage.py makemigrations", nunca apague de forma manual
# 4° Criar na base de dados "py manage.py migrate"

# Para acessar a area adimn com interface:
# Criar um usuario  "py manage.py creatsuperusser"
# Ir no arquivo admin.py


class Category(models.Model):
    name = models.CharField(max_length=65)

    # Para aparecer um nome no painel admin do django
    def __str__(self):
        return self.name
# tabela


class Recipe(models.Model):
    # Colunas
    title = models.CharField(max_length=65)
    description = models.CharField(max_length=165)
    slug = models.SlugField()
    preparation_time = models.IntegerField()
    preparation_time_unit = models.CharField(max_length=65)
    servings = models.IntegerField()
    servings_unit = models.CharField(max_length=65)
    preparation_steps = models.TextField()
    preparation_steps_is_html = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=False)
    cover = models.ImageField(
        upload_to='recipes/covers/%Y/%m/%d/', blank=True, default='')
    # cover = models.ImageField(upload_to='recipes/covers/%Y/%m/%d/')
    # relação entre as 2 tabelas
    category = models.ForeignKey(
        # on_delete -> Quando eu apagar a categoria, vai setar null para evitar erros
        Category, on_delete=models.SET_NULL, null=True, blank=True,
        default=None,
    )
    # relação do import acima
    author = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True
    )

    def __str__(self):
        return self.title


# EDITED
# title description slug
# preparation_time preparation_time_unit
# servings servings_unit
# preparation_step
# preparation_step_is_html
# created_at updated_at
# is_published
# cover
# category (Relação)
# Author (Relação)
