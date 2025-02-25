from . import views
from django.urls import path


app_name = "mealcreator"
urlpatterns = [
    path("", views.MealListView.as_view(), name="meal_list"),
]