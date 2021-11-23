from src.Category import Category
from src.Meal import Meal


class MealsManager:
    def __init__(self) -> None:
        self._meals = {}
        self._categories = {}

    def create_category(self, id: str, name: str, thumbnail: str, description: str) -> Category:
        if type(id) == str and type(name) == str and type(thumbnail) == str and type(description) == str:
            category = Category(id, name, thumbnail, description)
            self._categories[id] = category
            return category
        else:
            raise TypeError("All arguments must be strings")

    def delete_category(self, category: Category) -> Category:
        if type(category) == Category:
            meals_to_delete = []
            for meal in self._meals.values():
                if meal.category.id == category.id:
                    meals_to_delete.append(meal.id)
            for meal_id in meals_to_delete:
                del self._meals[meal_id]
            del self._categories[category.id]
            return category
        else:
            raise TypeError("Category must be a Category object")

    def get_category(self, id: str) -> Category:
        if type(id) == str:
            return self._categories.get(id)
        else:
            raise TypeError("Id must be a string")

    def get_categories(self) -> set[Category]:
        return set(self._categories.values())

    def create_meal(self, id: str, name: str, category: Category, instructions: str, thumbnail: str, tags: set[str], ingredients: set[str]) -> Meal:
        if type(id) == str and type(name) == str and type(instructions) == str and type(thumbnail) == str and type(tags) == set and type(ingredients) == set:
            if type(category) == Category:
                meal = Meal(id, name, category, instructions,
                            thumbnail, tags, ingredients)
                self._meals[id] = meal
                return meal
            else:
                raise TypeError("Category must be a Category object")
        else:
            raise TypeError("Invalid argument types")

    def delete_meal(self, meal: Meal) -> Meal:
        if type(meal) == Meal:
            del self._meals[meal.id]
            return meal
        else:
            raise TypeError("Meal must be a Meal object")

    def get_meal(self, id: str) -> Meal:
        if type(id) == str:
            return self._meals.get(id)
        else:
            raise TypeError("Id must be a string")

    def get_meals(self) -> set[Meal]:
        return set(self._meals.values())

    def get_meals_by_tag(self, tag: str) -> set[Meal]:
        if type(tag) == str:
            meals = set()
            for meal in self._meals.values():
                if tag in meal.tags:
                    meals.add(meal)
            return set(meals)
        else:
            raise TypeError("Tag must be a string")

    def get_meals_by_category(self, category: Category) -> set[Meal]:
        if type(category) == Category:
            meals = set()
            for meal in self._meals.values():
                if meal.category.id == category.id:
                    meals.add(meal)
            return meals
        else:
            raise TypeError("Category must be a category object")

    def get_meals_with_ingredient(self, ingredient: str) -> set[Meal]:
        if type(ingredient) == str:
            meals = set()
            for meal in self._meals.values():
                if ingredient in meal.ingredients:
                    meals.add(meal)
            return meals
        else:
            raise TypeError("Ingredient must be a string")

    def get_categories_with_thumbnail(self) -> set[(str, str)]:
        return set((cat.id, cat.thumbnail) for cat in self._categories.values())

    def count_meals_by_tag(self, tag) -> int:
        if type(tag) == str:
            return sum(1 for meal in self._meals.values() if tag in meal.tags)
        else:
            raise TypeError("Tag must be a string")
