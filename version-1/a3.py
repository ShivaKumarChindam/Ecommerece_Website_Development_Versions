from flask import Flask, render_template, request, redirect, url_for
import os
import mysql.connector

app = Flask(__name__)

# Define the upload folder and allowed extensions for images
UPLOAD_FOLDER = 'static/uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# MySQL database configuration
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'root',
    'database': 'registration',
}

# Function to check if the file has an allowed extension
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# Create a table if it doesn't exist
def create_table():
    connection = mysql.connector.connect(**db_config)
    cursor = connection.cursor()

    create_table_query = """
    CREATE TABLE IF NOT EXISTS products (
        id INT AUTO_INCREMENT PRIMARY KEY,
        image_url VARCHAR(255),
        product_name VARCHAR(255),
        actual_price DECIMAL(10, 2),
        discounted_price DECIMAL(10, 2),
        discount_percentage DECIMAL(5, 2)
    );
    """

    cursor.execute(create_table_query)
    connection.commit()

    cursor.close()
    connection.close()

# Route to display a form to add a product
@app.route('/')
def index():
    return render_template('index.html')

# Route to handle the form submission and insert into the database
@app.route('/add_product', methods=['POST'])
def add_product():
    image_file = request.files['image_file']
    product_name = request.form['product_name']
    actual_price = float(request.form['actual_price'])
    discounted_price = float(request.form['discounted_price'])
    discount_percentage = float(request.form['discount_percentage'])

    # Check if the file is allowed
    if image_file and allowed_file(image_file.filename):
        filename = os.path.join(app.config['UPLOAD_FOLDER'], image_file.filename)
        image_file.save(filename)
        image_url = url_for('static', filename=f'uploads/{image_file.filename}')

        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor()

        insert_query = """
        INSERT INTO products (image_url, product_name, actual_price, discounted_price, discount_percentage)
        VALUES (%s, %s, %s, %s, %s);
        """

        cursor.execute(insert_query, (image_url, product_name, actual_price, discounted_price, discount_percentage))
        connection.commit()

        cursor.close()
        connection.close()

        return "Product added successfully!"

    return "Invalid file format. Allowed formats: png, jpg, jpeg, gif"

#product page testing
@app.route('/productpage')
def dis_products():
    connection = mysql.connector.connect(**db_config)
    cursor = connection.cursor(dictionary=True)

    select_query = """
    SELECT id, image_url, product_name, actual_price, discounted_price, discount_percentage
    FROM products;
    """

    cursor.execute(select_query)
    products = cursor.fetchall()

    cursor.close()
    connection.close()

    return render_template('productpage.html', products=products)

#testing ends

# New route to retrieve and display product details
@app.route('/products')
def display_products():
    connection = mysql.connector.connect(**db_config)
    cursor = connection.cursor(dictionary=True)

    select_query = """
    SELECT id, image_url, product_name, actual_price, discounted_price, discount_percentage
    FROM products;
    """

    cursor.execute(select_query)
    products = cursor.fetchall()

    cursor.close()
    connection.close()

    return render_template('products.html', products=products)

if __name__ == '__main__':
    create_table()
    app.run(debug=True)
