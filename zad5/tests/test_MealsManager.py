import unittest
from assertpy import assert_that
from src.MealsManager import MealsManager
import requests


class TestStatement(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        # Load all data from api to MealsManager
        cls.mm2 = MealsManager()
        # Get all categories from api
        all_categories = requests.get(
            'https://www.themealdb.com/api/json/v1/1/categories.php')
        # For every category in response, add it to MealsManager
        for category in all_categories.json()["categories"]:
            category_id = category.get("idCategory")
            category_name = category.get("strCategory")
            category_thumbnail = category.get("strCategoryThumb")
            category_description = category.get("strCategoryDescription")
            cls.mm2.create_category(category_id, category_name,
                                    category_thumbnail, category_description)
        # For every category in MealsManager, get all meals from api that have such category
        for category in cls.mm2.get_categories():
            all_meals_in_category = requests.get(
                f'https://www.themealdb.com/api/json/v1/1/filter.php?c={category.name}')
            # For all meals in category, get their details
            for meal in all_meals_in_category.json()["meals"]:
                meal_id = meal.get("idMeal")
                meal_details = requests.get(
                    f'https://www.themealdb.com/api/json/v1/1/lookup.php?i={meal_id}')
                meal_object = meal_details.json()["meals"][0]
                meal_name = meal_object.get("strMeal")
                meal_thumbnail = meal_object.get("strMealThumb")
                meal_instructions = meal_object.get("strInstructions")
                meal_tags = meal_object.get("strTags")
                if meal_tags != None:
                    meal_tags = set(meal_tags.split(","))
                else:
                    meal_tags = set()
                meal_ingredients = set(ingredient for ingredient in [meal_object.get(
                    f'strIngredient{i}') for i in range(1, 21)] if ingredient != "")
                cls.mm2.create_meal(meal_id, meal_name, category, meal_instructions,
                                    meal_thumbnail, meal_tags, meal_ingredients)

    def setUp(self) -> None:
        self.mm = MealsManager()

    def test_empty_categories(self) -> None:
        assert_that(self.mm.get_categories()).is_equal_to(set())

    def test_create_and_get_category(self) -> None:
        self.mm.create_category("1", "test_cat", "link", "testingcategory")
        assert_that(str(self.mm.get_category('1'))).is_equal_to(
            'Category: test_cat\nthumbnail: link\ndescription: testingcategory')

    def test_create_and_get_multiple_categories(self) -> None:
        self.mm.create_category("1", "test_cat", "link", "testingcategory")
        self.mm.create_category("2", "test_cat2", "link2", "testingcategory2")
        assert_that(str(self.mm.get_categories())).contains(
            'Category: test_cat2, id: 2', 'Category: test_cat, id: 1')

    def test_get_categories(self) -> None:
        self.mm.create_category("1", "test_cat", "link", "testingcategory")
        assert_that(str(self.mm.get_categories())).is_equal_to(
            "{Category: test_cat, id: 1}")

    def test_delete_category(self) -> None:
        self.mm.create_category("1", "test_cat", "link", "testingcategory")
        self.mm.delete_category(self.mm.get_category('1'))
        assert_that(self.mm.get_categories()).is_equal_to(set())

    def test_create_and_get_meal(self) -> None:
        self.mm.create_category("1", "test_cat", "link", "testingcategory")
        cat = self.mm.get_category('1')
        self.mm.create_meal('1', 'zupa', cat, 'ugotuj wode', 'link',
                            set(['wodne']), set(['woda']))
        assert_that(str(self.mm.get_meal('1'))).is_equal_to(
            'Meal: zupa\ncategory: test_cat\ninstructions: ugotuj wode\nthumbnail: link\ntags: {\'wodne\'}\ningredients: {\'woda\'}')

    def test_create_and_get_meals(self) -> None:
        self.mm.create_category("1", "test_cat", "link", "testingcategory")
        cat = self.mm.get_category('1')
        self.mm.create_meal('1', 'zupa', cat, 'ugotuj wode', 'link',
                            set(['wodne']), set(['woda']))
        self.mm.create_meal('2', 'zupa2', cat, 'ugotuj wode', 'link',
                            set(['wodne']), set(['woda']))
        assert_that(str(self.mm.get_meals())).contains(
            'Meal: zupa, id: 1', 'Meal: zupa2, id: 2')

    def test_delete_meal(self) -> None:
        self.mm.create_category("1", "test_cat", "link", "testingcategory")
        cat = self.mm.get_category('1')
        self.mm.create_meal('1', 'zupa', cat, 'ugotuj wode', 'link',
                            set(['wodne']), set(['woda']))
        self.mm.delete_meal(self.mm.get_meal('1'))
        assert_that(self.mm.get_meals()).is_equal_to(set())

    def test_delete_category_with_meal(self) -> None:
        self.mm.create_category("1", "test_cat", "link", "testingcategory")
        self.mm.create_meal('1', 'zupa', self.mm.get_category('1'), 'ugotuj wode', 'link',
                            set(['wodne']), set(['woda']))
        self.mm.delete_category(self.mm.get_category('1'))
        assert_that(self.mm.get_meals()).is_equal_to(set())

    def test_get_meals_by_tag(self) -> None:
        self.mm.create_category("1", "test_cat", "link", "testingcategory")
        cat = self.mm.get_category('1')
        self.mm.create_meal('1', 'zupa', cat, 'ugotuj wode', 'link',
                            set(['wodne']), set(['woda']))
        self.mm.create_meal('2', 'zupa2', cat, 'ugotuj wode', 'link',
                            set(['wodne']), set(['woda']))
        self.mm.create_meal('3', 'zupa3', cat, 'ugotuj olej', 'link',
                            set(['olejowe']), set(['olej']))
        assert_that(str(self.mm.get_meals_by_tag('wodne'))).contains(
            'Meal: zupa, id: 1', 'Meal: zupa2, id: 2')

    def test_get_meals_by_category(self) -> None:
        self.mm.create_category("1", "test_cat", "link", "testingcategory")
        self.mm.create_category("2", "test_cat2", "link", "testingcategory2")
        cat1 = self.mm.get_category('1')
        cat2 = self.mm.get_category('2')
        self.mm.create_meal('1', 'zupa', cat1, 'ugotuj wode', 'link',
                            set(['wodne']), set(['woda']))
        self.mm.create_meal('2', 'zupa2', cat1, 'ugotuj wode', 'link',
                            set(['wodne']), set(['woda']))
        self.mm.create_meal('3', 'zupa3', cat2, 'ugotuj olej', 'link',
                            set(['olejowe']), set(['olej']))
        assert_that(str(self.mm.get_meals_by_category(cat2))
                    ).is_equal_to('{Meal: zupa3, id: 3}')

    def test_get_meals_with_ingredient(self) -> None:
        self.mm.create_category("1", "test_cat", "link", "testingcategory")
        self.mm.create_category("2", "test_cat2", "link", "testingcategory2")
        cat1 = self.mm.get_category('1')
        cat2 = self.mm.get_category('2')
        self.mm.create_meal('1', 'zupa', cat1, 'ugotuj wode', 'link',
                            set(['wodne']), set(['woda']))
        self.mm.create_meal('2', 'zupa2', cat1, 'ugotuj wode', 'link',
                            set(['wodne']), set(['woda']))
        self.mm.create_meal('3', 'zupa3', cat2, 'ugotuj olej', 'link',
                            set(['olejowe']), set(['olej']))
        assert_that(str(self.mm.get_meals_with_ingredient('olej'))
                    ).is_equal_to('{Meal: zupa3, id: 3}')

    def test_get_categories_with_thumbnail(self) -> None:
        self.mm.create_category("1", "test_cat", "link", "testingcategory")
        self.mm.create_category(
            "2", "test_cat2", "some_other_link", "testingcategory2")
        assert_that(str(self.mm.get_categories_with_thumbnail())
                    ).contains('\'1\', \'link\'', '\'2\', \'some_other_link\'')

    def test_api_categories_is_not_empty(self) -> None:
        assert_that(self.mm2.get_categories()).is_not_empty()

    def test_api_count_categories_by_tag(self) -> None:
        assert_that(self.mm2.count_meals_by_tag('Pasta')).is_equal_to(10)

    def test_api_get_meal_by_id(self) -> None:
        assert_that(self.mm2.get_meal('52771').name).is_equal_to(
            "Spicy Arrabiata Penne")

    def test_api_get_category_by_id(self) -> None:
        assert_that(self.mm2.get_category('1').name).is_equal_to('Beef')

    def test_api_get_categories(self) -> None:
        assert_that(str(self.mm2.get_categories())).contains(
            'Beef', 'Seafood', 'Breakfast')

    def test_api_get_meals_by_category(self) -> None:
        cat = self.mm2.get_category('2')
        assert_that(str(self.mm2.get_meals_by_category(cat))).contains(
            'Kung Pao Chicken', 'Teriyaki Chicken Casserole')

    def test_api_get_meals_with_ingredient(self) -> None:
        assert_that(str(self.mm2.get_meals_with_ingredient('Ginger'))
                    ).contains('Nutty Chicken Curry', 'Eccles Cakes')

    def test_create_category_invalid_types(self) -> None:
        assert_that(self.mm.create_category).raises(
            TypeError).when_called_with(1, {}, [], 3.14)

    def test_delete_category_invalid_types(self) -> None:
        assert_that(self.mm.delete_category).raises(
            TypeError).when_called_with({1: "2"})

    def test_get_category_invalid_types(self) -> None:
        assert_that(self.mm.get_category).raises(
            TypeError).when_called_with(1337)

    def test_create_meal_invalid_types(self) -> None:
        assert_that(self.mm.create_meal).raises(
            TypeError).when_called_with(1, {}, [], 3.14, 5, 6, 7)

    def test_delete_meal_invalid_types(self) -> None:
        assert_that(self.mm.delete_meal).raises(
            TypeError).when_called_with(None)

    def test_get_meal_invalid_types(self) -> None:
        assert_that(self.mm.get_meal).raises(
            TypeError).when_called_with(False)

    def test_get_meals_by_tag_invalid_types(self) -> None:
        assert_that(self.mm.get_meals_by_tag).raises(
            TypeError).when_called_with(0)

    def test_get_meals_by_category_invalid_types(self) -> None:
        assert_that(self.mm.get_meals_by_category).raises(
            TypeError).when_called_with(None)

    def test_get_meals_with_ingredient_invalid_types(self) -> None:
        assert_that(self.mm.get_meals_with_ingredient).raises(
            TypeError).when_called_with(["test", "invalid"])

    def test_count_meals_by_tag_invalid_types(self) -> None:
        assert_that(self.mm.count_meals_by_tag).raises(
            TypeError).when_called_with(123123123)

    def tearDown(self) -> None:
        self.mm = None
