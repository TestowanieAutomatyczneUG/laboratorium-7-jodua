from src.Category import Category


class Meal:
    def __init__(self, id: str, name: str, category: Category, instructions: str, thumbnail: str, tags: set[str], ingredients: set[str]) -> None:
        self._id = id
        self._name = name
        self._category = category
        self._instructions = instructions
        self._thumbnail = thumbnail
        self._tags = tags
        self._ingredients = ingredients

    @property
    def id(self) -> str:
        return self._id

    @property
    def name(self) -> str:
        return self._name

    @property
    def category(self) -> Category:
        return self._category

    @property
    def tags(self) -> set[str]:
        return self._tags

    @property
    def ingredients(self) -> set[str]:
        return self._ingredients

    def __str__(self) -> str:
        return f'Meal: {self._name}\ncategory: {self._category.name}\ninstructions: {self._instructions}\nthumbnail: {self._thumbnail}\ntags: {self._tags}\ningredients: {self._ingredients}'

    def __repr__(self) -> str:
        return f'Meal: {self._name}, id: {self._id}'
