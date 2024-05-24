from flask import Flask,render_template
import mysql.connector

app = Flask(__name__)

# MySQL database configuration
DB_USERNAME = "root"
DB_PASSWORD = "root"
DB_HOST = "localhost"
DB_NAME = "registration"

# Function to read items from a text file with multiple fields
def read_items_from_file(filename):
    with open(filename, 'r') as file:
        lines = file.read().splitlines()
        print(lines)
    items = []
    for line in lines:
        # Assuming fields are separated by commas
        fields = line.split(',')
        items.append(tuple(fields))

    return items

# MySQL connection
db_connection = mysql.connector.connect(
    host=DB_HOST,
    user=DB_USERNAME,
    password=DB_PASSWORD
)

# Create a database if it doesn't exist
cursor = db_connection.cursor()
cursor.execute(f"CREATE DATABASE IF NOT EXISTS {DB_NAME}")
cursor.close()
db_connection.close()
print("created database")

# Connect to the created database
db_connection = mysql.connector.connect(
    host=DB_HOST,
    user=DB_USERNAME,
    password=DB_PASSWORD,
    database=DB_NAME
)

print("connected to the database")

# Create products table if it doesn't exist
cursor = db_connection.cursor()
cursor.execute("""
    CREATE TABLE IF NOT EXISTS products (
        id VARCHAR(25) PRIMARY KEY,
        image_url VARCHAR(255) NOT NULL,
        product_name VARCHAR(255) NOT NULL,
        actual_price DECIMAL(10, 2) NOT NULL,
        discounted_price DECIMAL(10, 2) NOT NULL,
        discount_percentage DECIMAL(10, 2) NOT NULL
    )
""")
cursor.close()
print("created products table")

# Create reg table if it doesn't exist
cursor = db_connection.cursor()
cursor.execute("""
    CREATE TABLE IF NOT EXISTS reg (
        email VARCHAR(25) NOT NULL,
        pswd VARCHAR(25) NOT NULL,
        uname VARCHAR(50) NOT NULL
    )
""")
cursor.close()
print("created reg table")

# Flask route to insert items into the table
@app.route('/')
def insert_items():
    # Read items from the text file
    items = read_items_from_file('input_items.txt')

    # Insert items into the table
    cursor = db_connection.cursor()
    for item in items:
        cursor.execute("INSERT INTO products (id, image_url, product_name, actual_price, discounted_price, discount_percentage) VALUES (%s, %s, %s, %s, %s,%s)", item)
    db_connection.commit()
    cursor.close()
    print("items added sucessfully")

    return render_template('sucess.html')

if __name__ == '__main__':
    app.run(debug=True)
