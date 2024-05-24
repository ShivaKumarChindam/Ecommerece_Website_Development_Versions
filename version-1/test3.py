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
	return render_template("temp5.html")


@app.route('/',methods=['POST','GET'])
def display_product():
    try:
        #selected_option = request.form.get('option')
        #print(f"selected_option : {selected_option}")
        #id=selected_option
        data = request.get_json()
        selected_value = data['value']
        print(f'Selected Value: {selected_value}')
        id=selected_value
        # id=request.form.get("id")
        print(f"Received input from HTML: {id}")
        # Connect to the database
        connection = mysql.connector.connect(**db_config)
        print("connected to db")
        cursor = connection.cursor()
        print("created cursur")
        # Replace 'your_table' with the actual table name and 'your_product_id' with the specific product ID
        query = "SELECT * FROM products WHERE id = (%s)"
        print("query writed")
        cursor.execute(query,(id,))
        print("curser executed")

        # Fetch one row of result
        product = cursor.fetchone()
        print("product featched")

        # Close the cursor
        cursor.close()
        print("cursor closed")

        # Check if the product exists
        if product:
            # Pass the product details to the HTML template
            print("we got the product")
            print(product)
            return render_template('single.html', product=product)
        else:
            print("Product not found")
            return "Product not found"

    except Exception as e:
        return str(e)
@app.route('/')
def b():
	return render_template("single.html")

if __name__ == '__main__':
    app.run(debug=True)
