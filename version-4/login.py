from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)

# MySQL database configuration
DB_USERNAME = "root"
DB_PASSWORD = "root"
DB_HOST = "localhost"
DB_NAME = "ecom"


# MySQL connection
db_connection = mysql.connector.connect(
    host=DB_HOST,
    user=DB_USERNAME,
    password=DB_PASSWORD,
    database=DB_NAME
)


@app.route("/",methods=['POST','GET'])
def abc():
	if request.method == 'POST':
		email = request.form['email']
		password = request.form['password']
		username= request.form['username']
		cursor = db_connection.cursor()
		cursor.execute("INSERT INTO customers (email, password, username) VALUES (%s, %s,%s)", (email, password, username))
		db_connection.commit()
		cursor.close()
	return render_template("t1.html")


if __name__ == '__main__':
    app.run(debug=True)