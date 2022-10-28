"""CS 108 - Lab 9.0

This module implements a simple food item class with nutritional information.

@author: OWEN KOH (ojk2)
@date: Fall, 2022

Note: All the code before the "#Your code goes here... " was not done by me.
"""


class FoodItem:

    def __init__(self, name, fat, carbohydrates, protein):
        """Constructs a FoodItem instance with the given attributes"""
        self.name = name
        self.fat = fat
        self.carbohydrates = carbohydrates
        self.protein = protein

    def __str__(self):
        """Returns a printable representation of this food item"""
        return (
            self.name
            + "\n\tFat: {:.2f} g".format(self.fat)
            + "\n\tCarbohydrates: {:.2f} g".format(self.carbohydrates)
            + "\n\tProtein: {:.2f} g".format(self.protein)
        )

    def get_calories(self, num_servings):
        """Returns the number of calories for the given number of servings of
        this food item
        """
        return num_servings * (
            (self.fat * 9) + (self.carbohydrates * 4) + (self.protein * 4)
        )


# Your code goes here...
fooditem1 = FoodItem('M&Ms', 10.0, 34.00, 2.00)
print(f"{fooditem1}\nCalories per serving: {fooditem1.get_calories(1)}")
print()
fooditem2 = FoodItem('Water', 0.00, 0.00, 0.00)
print(f"{fooditem2}\nCalories per 10 servings: {fooditem2.get_calories(10)}")
