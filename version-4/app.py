from flask import Flask, render_template, request, session, redirect, url_for
import mysql.connector

app = Flask(__name__)
app.secret_key = 'cskmnt1'

# MySQL database configuration
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'root',
    'database': 'ecom',
}

@app.route('/')
def a():
    print("Opend login page")
    return render_template("login.html")

@app.route("/1",methods=['POST','GET'])
def abc1():
	if request.method == 'POST':
		email=request.form.get("email")
		username=request.form.get("username")	
		password=request.form.get("password")
		con=mysql.connector.connect(host="localhost",user="root",password="root",database="ecom")
		cur=con.cursor()
		query = "INSERT INTO customers (email, password, username) VALUES (%s, %s, %s)"
		cur.execute(query, (email, password, username))
		print("user created successfully")
		con.commit()
	return render_template("login.html")

@app.route("/2",methods=['POST','GET'])
def abc2():
	if request.method == 'POST':
		email=request.form.get("email")
		password=request.form.get("password")
		con=mysql.connector.connect(host="localhost",user="root",password="root",database="ecom")
		cur=con.cursor()
		cur.execute("select * from customers")
		for x in cur:
			if(x[0]==email):
				if(x[1]==password):
					session['email'] = email
					email=session['email']
					print("Email id matched with existing users")
					print("Email id:",email)
					if 'email' in session:
						email = session['email']
						try:
							connection = mysql.connector.connect(**db_config)
							cursor = connection.cursor(dictionary=True)
							query = "SELECT * FROM customers WHERE email = %s"
							cursor.execute(query, (email,))
							user = cursor.fetchone()
							cursor.close()
							connection.close()
							print(user)
							return render_template('index.html', user=user)
						except mysql.connector.Error as error:
							return f"Error: {error}"
				else:
					print("Enter valid Password")
			else:
				print("Email id does not matched")
		

	return render_template("login.html")




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
            query = "SELECT * FROM product_list WHERE id = %s"
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

@app.route("/logout")
def logout():
    session.pop('email', None)  # Resetting email to null
    print("LogOuted sucessfully")
    print("email id is null")
    return render_template("login.html")


@app.route("/display/index.html")
def fun1():
   print("Opend index page")
   return(render_template("index.html"))

@app.route("/index.html")
def fun01():
   print("Opend index page")
   return(render_template("index.html"))
	

@app.route("/mobiles.html")
def fun2():
  print("Opend mobiles page")
  print("Email id:", session['email'])
  return(render_template("mobiles.html"))

@app.route("/cart.html")
def fun4():
  print("Opend cart page")
  return(render_template("cart.html"))

@app.route("/downloadtheapp.html")
def fun5():
  print("Opend downloadtheapp page")
  return(render_template("downloadtheapp.html"))

@app.route("/login.html")
def fun6():
  print("Opend login page")
  return(render_template("login.html"))

@app.route("/refer.html")
def fun7():
  print("Opend refer page")
  return(render_template("refer.html"))

@app.route("/wishlist.html")
def fun8():
  print("Opend wishlist page")
  return(render_template("wishlist.html"))

@app.route("/grocery.html")
def fun9():
  print("Opend grocery page")
  return(render_template("grocery.html"))

@app.route("/fashion.html")
def fun10():
  print("Opend fashion page")
  return(render_template("fashion.html"))

@app.route("/electronics.html")
def fun11():
  print("Opend electronics page")
  return(render_template("electronics.html"))

@app.route("/home&furniture.html")
def fun12():
  print("Opend home&furniture page")
  return(render_template("home&furniture.html"))

@app.route("/beauty.html")
def fun13():
  print("Opend beauty page")
  return(render_template("beauty.html"))

@app.route("/toys.html")
def fun14():
  print("Opend toys page")
  return(render_template("toys.html"))

@app.route("/books.html")
def fun15():
  print("Opend books page")
  return(render_template("books.html"))

@app.route("/walldecors.html")
def fun16():
  print("Opend walldecors page")
  return(render_template("walldecors.html"))

@app.route("/medicine.html")
def fun17():
  print("Opend medicine page")
  return(render_template("medicine.html"))

@app.route("/redirected.html")
def fun18():
  print("Opend redirected page")
  return(render_template("redirected.html"))

@app.route("/display/errorpage.html")
def fun19():
  print("Opend errorpage page")
  return(render_template("errorpage.html"))

if __name__ == '__main__':
    app.run(debug=True)
