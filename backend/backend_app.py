from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return "Server is running!"

@app.route('/get/product/', methods=['GET'])
def get_product():
    id = request.json['id']
    return "Information about product with id {}!".format(id)

@app.route('/put/order/', methods=['GET', 'PUT', 'POST'])
def put_order():
    id = request.json['id']
    return "Putting order with id {}".format(id)

@app.after_request
def after_request(response):
  response.headers.add('Access-Control-Allow-Origin', 'http://localhost:8000')
  response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
  response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
  response.headers.add('Access-Control-Allow-Credentials', 'true')
  return response

app.run(debug=True)
