# import the Flask class from the flask module
from flask import Flask, render_template, redirect, url_for, request
import requests

# create the application object
app = Flask("MyApp")

# use decorators to link the function to a url
@app.route("/")
def startgame():
	return render_template("index.html") # render a template

@app.route("/index.html")
def playagain():
	return render_template("index.html") 

@app.route("/1-nochallenge.html")
def nochallenge():
	return render_template("1-nochallenge.html")

@app.route("/1-yeschallenge.html")
def yeschallenge():
	return render_template("1-yeschallenge.html")

@app.route("/2-left.html")
def left():
	return render_template("2-left.html")

@app.route("/2-right.html")
def right():
	return render_template("2-right.html")

@app.route("/3-torch.html")
def torch():
	return render_template("3-torch.html")

@app.route("/4-founddragon.html")
def founddragon():
	return render_template("4-founddragon.html")

@app.route("/5-foundprincess.html")
def foundprincess():
	return render_template("5-foundprincess.html")

@app.route("/6-goafterdragon.html")
def goafterdragon():
	return render_template("6-goafterdragon.html")

@app.route("/6-saveprincess.html")
def saveprincess():
	return render_template("6-saveprincess.html")

@app.route("/7-frienddragon.html")
def frienddragon():
	return render_template("7-frienddragon.html")

@app.route("/7-winner.html")
def winner():
	return render_template("7-winner.html")

@app.route("/gameover.html")
def gameover():
	return render_template("gameover.html")

app.run(debug=True)
