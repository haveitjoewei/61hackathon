import sqlite3
import time
from euclid import findcloseststop
from flask import Flask, request, g, render_template, redirect, send_file

app = Flask(__name__)


@app.route("/")
def hello():
	return render_template('index2.html', loc=False)

@app.route("/contact")
def hi():
    return render_template('index3.html')   

@app.route("/api/cheep", methods=["POST"])
def receive_cheep():
    print(request.form)
    location = [float(i) for i in request.form['name'].split(",")] #TODO
    closest_stop = findcloseststop(location[0], location[1])
    return render_template('index2.html', loc=closest_stop)
    
if __name__ == "__main__":
	app.debug = True
	app.run(host = '0.0.0.0', debug = True, port = 5000)