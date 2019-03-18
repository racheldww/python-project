from flask import Flask, render_template, request
import requests

app = Flask("MyApp")

@app.route("/")
def hello():
	return render_template("index.html")

@app.route("/dragon")
def hello():
	return render_template("dragon.py")

app.run(debug=True)
