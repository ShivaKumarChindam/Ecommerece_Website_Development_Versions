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

@app.route('/')
def a():
    return render_template("temp2.html")


@app.route('/display/<id>', methods=['POST', 'GET'])
def display_product(id):
    try:
        if request.method == 'POST':
            selected_option = request.form.get('option')
            print(f"selected_option: {selected_option}")

            # Connect to the database
            connection = mysql.connector.connect(**db_config)
            print("connected to db")
            cursor = connection.cursor(dictionary=True)
            print("created cursor")

            # Replace 'products' with your actual table name
            query = "SELECT * FROM products3 WHERE id = %s"
            print("query written")
            cursor.execute(query, (selected_option,))
            print("cursor executed")

            # Fetch one row of result
            product = cursor.fetchone()
            print("product fetched")

            # Close the cursor and connection
            cursor.close()
            connection.close()
            print("cursor and connection closed")

            # Check if the product exists
            if product:
                # Pass the product details to the HTML template
                print("we got the product")
                print(product)
                return render_template('productpage2.html', product=product)
            else:
                print("Product not found")
                return "Product not found"

        return "Invalid request"

    except Exception as e:
        return str(e)

if __name__ == '__main__':
    app.run(debug=True)
