from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)

# MySQL database configuration
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'root',
    'database': 'ecom',
}

# New route to retrieve and display all product details
@app.route('/')
def display_products():
    connection = mysql.connector.connect(**db_config)
    cursor = connection.cursor(dictionary=True)

    select_query = """
    SELECT id,image_url, product_name, actual_price, discounted_price, discount_percentage
    FROM product_list;
    """

    cursor.execute(select_query)
    products = cursor.fetchall()

    cursor.close()
    connection.close()

    return render_template('products.html', products=products)

# new route to display all user details
@app.route('/uid')
def display_uid():
    connection = mysql.connector.connect(**db_config)
    cursor = connection.cursor(dictionary=True)

    select_query = """
    SELECT email,password,username
    FROM customers;
    """

    cursor.execute(select_query)
    products = cursor.fetchall()

    cursor.close()
    connection.close()

    return render_template('uid.html', products=products)

#new route to display wishlist products
@app.route('/wishlist')
def display_wishlist():
    connection = mysql.connector.connect(**db_config)
    cursor = connection.cursor(dictionary=True)

    select_query = """
    SELECT email,id,image_url, product_name, actual_price, discounted_price, discount_percentage
    FROM wishlist;
    """

    cursor.execute(select_query)
    products = cursor.fetchall()

    cursor.close()
    connection.close()

    return render_template('w1.html', products=products)

# Flask route to delete items from the table
@app.route('/delete')
def delete_wishlist_items():
    connection = mysql.connector.connect(**db_config)
    cursor = connection.cursor(dictionary=True)
    email='shiva@gmail.com'
    id='be1'
    # Insert items into the table
    cursor.execute("DELETE FROM wishlist WHERE email = %s AND id = %s", email,id)
    db_connection.commit()
    cursor.close()
    print("items added sucessfully")

    return render_template('sucess.html')




if __name__ == '__main__':
    app.run(debug=True)