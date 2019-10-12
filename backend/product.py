import json
from json import JSONEncoder


class Product():

    def __init__(self, _id, _name, _price, _description):
        self.id = _id
        self.name = _name
        self.price = _price
        self.description = _description__dict__

    def setId(self, _id):
        self.id = _id

    def getId(self):
        return self.id

    def setName(self, _name):
        self.name = _name

    def getName(self):
        return self.name

    def setPrice(self, _price):
        self.price = _price

    def getPrice(self):
        return self.price

    def setDescription(self, _description):
        self.id = _description

    def getDescription(self):
        return self.description

    def toJson(self):
        print(json.dumps(self.__dict__))
        return json.dumps(self.__dict__)
