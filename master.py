# import the Flask class from the flask module
from flask import Flask, render_template, redirect, url_for, request
import requests

# create the application object
app = Flask("MyApp")

# use decorators to link the function to a url
@app.route("/")
def hello():
	return render_template("index.html") # render a template

app.run(debug=True)
