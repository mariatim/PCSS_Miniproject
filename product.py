import json
from json import JSONEncoder


class Product():
    def __init__(self, _id, _name, _price, _description, _tickets):
        self.id = _id
        self.name = _name
        self.price = _price
        self.description = _description
        self.tickets = _tickets

    def toJson(self):
        return json.dumps(self.__dict__)

# "Database"
products = [Product(0, 'HyperFest', 1190, 'If you like rock music, this festival is for you!', 100),
            Product(1, 'SuperFest', 1695, 'If you like boardgames, this festival is for you!', 0),
            Product(2, 'MegaFest', 2100, 'If you like woodcarving, this festival is for you!', 300),
            Product(3, 'GigaFest', 1099, 'If you like rock climbing, this festival is for you!', 5),
            Product(4, 'GrandFest', 3000, 'If you like electronic music, this festival is for you!', 14),
            Product(5, 'MegaloFest', 990, 'If you like aliens, this festival is for you!', 7)]
