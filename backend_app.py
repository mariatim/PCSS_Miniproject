from flask import Flask, request
import random
import json

from product import products
from order import orders, Order

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return "Server is running!"

@app.route('/get/product/', methods=['GET'])
def get_product():
    parameter = int(request.args["id"])
    return products[parameter].toJson()

@app.route('/get/allproducts/', methods=['GET'])
def get_all_products():
    response = json.dumps([p.toJson() for p in products])
    return "getAllCallback(" + response + ")"

@app.route('/put/order/', methods=['GET', 'PUT', 'POST'])
def put_order():
    print(request.is_json)
    print(type(request))
    print(request.form)
    parameter = request.args["products"]
    orders.append(Order(len(orders), parameter))
    return parameter

@app.after_request
def after_request(response):
  response.headers.add('Access-Control-Allow-Origin', '*')
  response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
  response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
  response.headers.add('Access-Control-Allow-Credentials', 'true')
  response.headers.add('Access-Control-Allow-Redirect', 'true')
  return response

app.run(debug=True)
