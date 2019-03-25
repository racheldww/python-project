# import the Flask class from the flask module
from flask import Flask, render_template, redirect, url_for, request
import requests

# create the application object
app = Flask("MyApp")
endgame = ""
# use decorators to link the function to a url
@app.route("/")
def startgame():
	return render_template("index.html") # render a template

@app.route("/start")
def playagain():
	return render_template("index.html") 

@app.route("/1-nochallenge")
def nochallenge():
	global endgame
	endgame = "Does honour mean nothing to you?"
	return render_template("1-nochallenge.html")

@app.route("/1-yeschallenge")
def yeschallenge():
	return render_template("1-yeschallenge.html")

@app.route("/2-left")
def left():
	global endgame
	endgame = "Oh no, you drop through the crack and get injured!"
	return render_template("2-left.html")

@app.route("/2-right")
def right():
	global endgame
	endgame = "Turns out you have terrible night vision. You got injured."
	return render_template("2-right.html")

@app.route("/3-torch")
def torch():
	global endgame
	endgame = "The bats overwhelmed you!"
	return render_template("3-torch.html")

@app.route("/4-founddragon")
def founddragon():
	global endgame
	endgame = "You are obviously not strong enough to defeat the dragon!"
	return render_template("4-founddragon.html")

@app.route("/5-foundprincess")
def foundprincess():
	return render_template("5-foundprincess.html")

@app.route("/6-goafterdragon")
def goafterdragon():
	global endgame
	endgame = "You are obviously not strong enough to defeat the dragon!"
	return render_template("6-goafterdragon.html")

@app.route("/6-saveprincess")
def saveprincess():
	global endgame
	endgame = "You are obviously not strong enough to defeat the dragon!"
	return render_template("6-saveprincess.html")

@app.route("/7-frienddragon")
def frienddragon():
	return render_template("7-frienddragon.html")

@app.route("/7-winner")
def winner():
	return render_template("7-winner.html")

@app.route("/<gameover>")
def gameover(gameover):
	global endgame
	return render_template("gameover.html",gameover = endgame)

app.run(debug=True)
