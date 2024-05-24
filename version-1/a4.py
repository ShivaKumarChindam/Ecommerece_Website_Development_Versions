from flask import Flask, render_template,request
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
	return render_template("temp3.html")

@app.route('/',methods=['POST','GET'])
def display_product():
    try:
        selected_option = request.form.get('option')
        print(f"selected_option : {selected_option}")
        id=selected_option
        # id=request.form.get("id")
        print(f"Received input from HTML: {id}")
        # Connect to the database
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor()
        # Replace 'your_table' with the actual table name and 'your_product_id' with the specific product ID
        query = "SELECT * FROM products WHERE id = (%s)"
        cursor.execute(query,(id,))

        # Fetch one row of result
        product = cursor.fetchone()

        # Close the cursor
        cursor.close()

        # Check if the product exists
        if product:
            # Pass the product details to the HTML template
            return render_template('productpage2.html', product=product)
        else:
            print("Product not found")
            return "Product not found"

    except Exception as e:
        return str(e)
@app.route('/')
def b():
	return render_template("productpage2.html")

if __name__ == '__main__':
    app.run(debug=True)
