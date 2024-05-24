from flask import Flask,render_template
import mysql.connector

app = Flask(__name__)

# MySQL database configuration
DB_USERNAME = "root"
DB_PASSWORD = "root"
DB_HOST = "localhost"
# DB_PORT = "your_port"
DB_NAME = "registration"

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
    CREATE TABLE IF NOT EXISTS products (
        id VARCHAR(20) PRIMARY KEY,
        name VARCHAR(255) NOT NULL,
        url VARCHAR(255) NOT NULL,
        price DECIMAL(10, 2) NOT NULL
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
        cursor.execute("INSERT INTO products (id, name, url, price) VALUES (NULL, %s, %s, %s)", item)
    db_connection.commit()
    cursor.close()

    return render_template('sucess.html')

if __name__ == '__main__':
    app.run(debug=True)
