import requests


class Species:

    def __init__(self, name: str = "", description: str = "", imageURL: str = "") -> None:
        self.name = name
        self.description = description
        self.imageURL = imageURL

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name) -> None:
        if isinstance(name, str):
            self.__name = name.replace("_", " ").strip()
        else:
            raise TypeError("Name must be of type str.")

    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description) -> None:
        if isinstance(description, str):
            self.__description = description.strip()
        else:
            raise TypeError("Description must be of type str.")

    @property
    def imageURL(self) -> str:
        return self.__imageURL

    @imageURL.setter
    def imageURL(self, imageURL) -> None:
        req = requests.get(imageURL)
        if req.status_code < 400:
            self.__imageURL = imageURL
        else:
            raise InvalidURLError(f"Could not connect to: {imageURL}")


class InvalidURLError(Exception):
    pass
