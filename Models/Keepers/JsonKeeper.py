import json

from Models.Keepers.Keeper import Keeper


class JsonKeeper(Keeper):
    def __init__(self, path: str):
        self.path = path

    def load(self):
        try:
            file = open(self.path, 'r')
            value = json.load(file)
            file.close()
            return value
        except ValueError:
            return []

    def save(self, obj) -> None:
        try:
            with open(self.path, "w") as file:
                json.dump(obj, file)
            return True
        except ValueError:
            return False
