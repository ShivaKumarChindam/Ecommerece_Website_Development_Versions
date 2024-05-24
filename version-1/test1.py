from flask import Flask, render_template,request
import mysql.connector

app = Flask(__name__)
@app.route('/')
def a():
	return render_template("temp1.html")
@app.route('/',methods=['POST','GET'])
def abc():
	id=request.form.get("id")
	print(f"Received input from HTML: {id}")
	return "Data received successfully!"
@app.route('/',methods=['POST','GET'])
def cd():
	return render_template("productpage2.html")
app.run(debug='True')