from django.shortcuts import render

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    # можете добавить свои рецепты ;)
}

def recipe_view(request, recipe):
    template_name = 'calculator/index.html'
    template_404 = 'calculator/404.html'
    servings = int(request.GET.get('servings', 1))

    recipe_data = DATA.get(recipe, None)
    if recipe_data:
        for key, value in recipe_data.items():
            recipe_data[key] = value * servings

        context = {
            'recipe': recipe_data
        }
        return render(request, template_name, context)
    else:
        return render(request, template_404)