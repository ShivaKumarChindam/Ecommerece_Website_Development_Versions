from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)

# MySQL database configuration
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'root',
    'database': 'registration',
}

# New route to retrieve and display product details
@app.route('/')
def display_products():
    connection = mysql.connector.connect(**db_config)
    cursor = connection.cursor(dictionary=True)

    select_query = """
    SELECT id,image_url, product_name, actual_price, discounted_price, discount_percentage
    FROM products;
    """

    cursor.execute(select_query)
    products = cursor.fetchall()

    cursor.close()
    connection.close()

    return render_template('products.html', products=products)


if __name__ == '__main__':
    app.run(debug=True)