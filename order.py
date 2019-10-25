class Order():
    def __init__(self, _id, _products):
        self.id = _id
        self.products = _products
    
    def showOrder(self, _id):
        return self.products

orders = []
