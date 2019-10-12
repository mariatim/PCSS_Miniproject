from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return "Server is running!"

@app.route('/get/product/<int:id>', methods=['GET'])
def get_product(id):
    id = request.args.get('id', id)
    return "Information about product with id {}!".format(id)

@app.route('/put/order/<int:id>', methods=['GET', 'PUT', 'POST'])
def put_order(id):
    return "Putting order with id {}".format(id)

app.run(debug=True)
