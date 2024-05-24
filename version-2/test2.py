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
    return render_template("index.html")


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
            query = "SELECT * FROM products WHERE id = %s"
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
                return render_template('product_page.html', product=product)
            else:
                print("Product not found")
                return "Product not found"

        return "Invalid request"

    except Exception as e:
        return str(e)


@app.route("/display/index.html")
def fun1():
   return(render_template("index.html"))
@app.route("/mobiles.html")
def fun2():
  return(render_template("mobiles.html"))
@app.route("/cart.html")
def fun4():
  return(render_template("cart.html"))
@app.route("/downloadtheapp.html")
def fun5():
  return(render_template("downloadtheapp.html"))
@app.route("/login.html")
def fun6():
  return(render_template("login.html"))
@app.route("/",methods=['POST','GET'])
def abc1():
	if request.method == 'POST':
		email=request.form.get("email")
		uname=request.form.get("uname")	
		pswd=request.form.get("pswd")
		con=mysql.connector.connect(host="localhost",user="root",password="root",database="registration")
		cur=con.cursor()
		query = "INSERT INTO reg (email, pswd, uname) VALUES (%s, %s, %s)"
		cur.execute(query, (email, pswd, uname))
		print("success")
		con.commit()
	return render_template("login.html")
@app.route("/2",methods=['POST','GET'])
def abc2():
	if request.method == 'POST':
		email=request.form.get("email")
		pswd=request.form.get("pswd")
		con=mysql.connector.connect(host="localhost",user="root",password="root",database="registration")
		cur=con.cursor()
		cur.execute("select * from reg")
		for x in cur:
			if(x[0]==email):
				if(x[1]==pswd):
					return render_template("index.html")
				else:
					print("Enter valid Password")
			else:
				print("Enter valid Username")

	return render_template("login.html")

@app.route("/refer.html")
def fun7():
  return(render_template("refer.html"))
@app.route("/wishlist.html")
def fun8():
  return(render_template("wishlist.html"))
@app.route("/grocery.html")
def fun9():
  return(render_template("grocery.html"))
@app.route("/fashion.html")
def fun10():
  return(render_template("fashion.html"))
@app.route("/electronics.html")
def fun11():
  return(render_template("electronics.html"))
@app.route("/home&furniture.html")
def fun12():
  return(render_template("home&furniture.html"))
@app.route("/beauty.html")
def fun13():
  return(render_template("beauty.html"))
@app.route("/toys.html")
def fun14():
  return(render_template("toys.html"))
@app.route("/books.html")
def fun15():
  return(render_template("books.html"))
@app.route("/walldecors.html")
def fun16():
  return(render_template("walldecors.html"))
@app.route("/medicine.html")
def fun17():
  return(render_template("medicine.html"))
@app.route("/redirected.html")
def fun18():
  return(render_template("redirected.html"))
@app.route("/display/errorpage.html")
def fun19():
  return(render_template("errorpage.html"))


if __name__ == '__main__':
    app.run(debug=True)
