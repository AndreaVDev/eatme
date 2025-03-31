from django.db import models

class Dish(models.Model):
    ingredient_name = models.CharField(max_length=100, null=False, blank=False, unique=True)

    def __str__(self):
        return self.ingredient_name

class Meal(models.Model):
    LUNCH = "LU"
    DINNER = "DI"
    MEAL_TYPE_CHOICES = {
        LUNCH: "Lunch",
        DINNER: "Dinner",
    }
    type = models.CharField(max_length=2, choices=MEAL_TYPE_CHOICES.items(), default=LUNCH, null=False, blank=False)
    meal_date = models.DateField()
    meal_dish_lunch = models.ForeignKey('Dish', related_name="meal_dish_lunch", on_delete=models.CASCADE)
    meal_dish_dinner = models.ForeignKey('Dish', related_name="meal_dish_dinner", on_delete=models.CASCADE)

    def __str__(self):
        return self.type + " " + self.meal_dish_lunch.ingredient_name


