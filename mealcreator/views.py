from django.views.generic import ListView
from mealcreator.models import Meal


class MealListView(ListView):
    template_name = "templates/mealcreator/meal_list.html"
    model = Meal
    context_object_name = "meals"

    def get_queryset(self):
        return Meal.objects.all().order_by("meal_date")