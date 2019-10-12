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

app.run(debug=True, port=5000)
