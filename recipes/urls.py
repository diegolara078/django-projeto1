from django.urls import path

from recipes.views import  home  # imprtar as funcões da views

urlpatterns = [
    path('', home),
   # path('contato/', contado),
   # path('sobre/', sobre),
]
