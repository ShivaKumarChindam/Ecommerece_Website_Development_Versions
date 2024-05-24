from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Sample product data
products = [
    {"id": 1, "name": "Product 1", "price": 50.00},
    {"id": 2, "name": "Product 2", "price": 40.00},
    {"id": 3, "name": "Product 3", "price": 30.00}
]

cart_items = []

@app.route('/')
def index():
    return render_template('addtocart.html', products=products)

@app.route('/add_to_cart', methods=['POST'])
def add_to_cart():
    product_id = int(request.form['product_id'])
    product = next((p for p in products if p['id'] == product_id), None)

    if product:
        cart_items.append(product)
        return jsonify({"success": True, "message": "Product added to cart."})
    else:
        return jsonify({"success": False, "message": "Product not found."})

@app.route('/remove_from_cart', methods=['POST'])
def remove_from_cart():
    product_id = int(request.form['product_id'])
    cart_items[:] = [item for item in cart_items if item['id'] != product_id]
    return jsonify({"success": True, "message": "Product removed from cart."})

if __name__ == '__main__':
    app.run(debug=True)
