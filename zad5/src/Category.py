class Category:
    def __init__(self, id: str, name: str, thumbnail: str, description: str) -> None:
        self._id = id
        self._name = name
        self._thumbnail = thumbnail
        self._description = description

    @property
    def id(self) -> str:
        return self._id

    @property
    def name(self) -> str:
        return self._name

    @property
    def thumbnail(self) -> str:
        return self._thumbnail

    def __str__(self) -> str:
        return f'Category: {self._name}\nthumbnail: {self._thumbnail}\ndescription: {self._description}'

    def __repr__(self) -> str:
        return f'Category: {self._name}, id: {self._id}'
