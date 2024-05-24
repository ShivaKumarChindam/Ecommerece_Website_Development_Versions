from flask import Flask
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
    password=DB_PASSWORD,
    database=DB_NAME
)

# Flask route to insert items into the table
@app.route('/insert_items')
def insert_items():
    # Read items from the text file
    items = read_items_from_file('input_items.txt')

    # Insert items into the table
    cursor = db_connection.cursor()
    for item in items:
        cursor.execute("INSERT INTO products (image_url, product_name,actual_price,discounted_price,discount_percentage) VALUES (%s, %s, %s, %s, %s)", item)
    db_connection.commit()
    cursor.close()

    return 'Items inserted into the table successfully!'

if __name__ == '__main__':
    app.run(debug=True)
