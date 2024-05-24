from flask import Flask,render_template
import mysql.connector

app = Flask(__name__)

# MySQL database configuration
DB_USERNAME = "root"
DB_PASSWORD = "root"
DB_HOST = "localhost"
# DB_PORT = "your_port"
DB_NAME = "registration"

# MySQL database configuration
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'root',
    'database': 'registration',
}


# Function to read items from a text file with multiple fields
def read_items_from_file(filename):
    with open(filename, 'r') as file:
        lines = file.read().splitlines()

    items = []
    for line in lines:
        # Assuming fields are separated by commas
        fields = line.split(',')
        items.append(tuple(fields))

    return items

# Connect to the created database
db_connection = mysql.connector.connect(
    host=DB_HOST,
    user=DB_USERNAME,
    password=DB_PASSWORD,
    database=DB_NAME
)

# Create a table if it doesn't exist
cursor = db_connection.cursor()
cursor.execute("""
    CREATE TABLE IF NOT EXISTS products3 (
        id VARCHAR(20) PRIMARY KEY,
        image_url VARCHAR(255),
        product_name VARCHAR(255),
        actual_price DECIMAL(10, 2),
        discounted_price DECIMAL(10, 2),
        discount_percentage DECIMAL(5, 2)
    )
""")

cursor.close()

# Flask route to insert items into the table
@app.route('/')
def insert_items():
    # Read items from the text file
    items = read_items_from_file('input_items.txt')

    # Insert items into the table
    cursor = db_connection.cursor()
    for item in items:
        cursor.execute("INSERT INTO products3 (id, image_url, product_name, actual_price,discounted_price,discount_percentage) VALUES (%s, %s, %s, %s, %s, %s)", item)
    db_connection.commit()
    cursor.close()

    return render_template('sucess.html')

# New route to retrieve and display product details
@app.route('/products')
def display_products():
    connection = mysql.connector.connect(**db_config)
    cursor = connection.cursor(dictionary=True)

    select_query = """
    SELECT id, image_url, product_name, actual_price, discounted_price, discount_percentage
    FROM products3;
    """

    cursor.execute(select_query)
    products = cursor.fetchall()

    cursor.close()
    connection.close()

    return render_template('products.html', products=products)


if __name__ == '__main__':
    app.run(debug=True)
