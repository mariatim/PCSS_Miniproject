from flask import Flask, request
import random
import json

from product import Product

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return "Server is running!"

def populate_dummy_data():
    products = [Product(0, 'HyperFest', 1190, 'If you like rock music, this festival is for you!'),
                Product(1, 'SuperFest', 1695, 'If you like boardgames, this festival is for you!'),
                Product(2, 'MegaFest', 2100, 'If you like woodcarving, this festival is for you!'),
                Product(3, 'GigaFest', 1099, 'If you like rock climbing, this festival is for you!'),
                Product(4, 'GrandFest', 3000, 'If you like electronic music, this festival is for you!'),
                Product(5, 'MegaloFest', 990, 'If you like aliens, this festival is for you!')]
    return products

@app.route('/get/product/', methods=['GET'])
def get_product():
    products = populate_dummy_data()
    id = request.json['id']
    randomPos = random.randint(0, 5)
    products[randomPos].setId(id)
    return products[randomPos].toJson()

@app.route('/get/allproducts/', methods=['GET'])
def get_all_products():
    products = populate_dummy_data()
    response = json.dumps([p.toJson() for p in products])
    return "getAllCallback(" + response + ")"

@app.route('/put/order/', methods=['GET', 'PUT', 'POST'])
def put_order():
    id = request.json['id']
    return "Putting order with id {}".format(id)

@app.after_request
def after_request(response):
  response.headers.add('Access-Control-Allow-Origin', '*')
  response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
  response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
  response.headers.add('Access-Control-Allow-Credentials', 'true')
  return response

app.run(debug=True)