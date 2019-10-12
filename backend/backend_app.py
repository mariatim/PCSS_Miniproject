from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/get/product/<int:id>')
def get_product(id):
    id = request.args.get('id', id)
    return "Information about product with id {}!".format(id)

@app.route('/put/order/<int:id>')
def put_order(id):
    return "Putting order with id {}".format(id)

app.run(debug=True)
