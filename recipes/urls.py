from django.urls import path, include
from calculator.views import recipe_view

urlpatterns = [
    path('<str:recipe>/', recipe_view, name='recipe'),

]


