import sqlite3
import time
from euclid import findcloseststop
from flask import Flask, request, g, render_template, redirect

app = Flask(__name__)
DATABASE = 'cheeps.db'

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

def db_read_cheeps():
    cur = get_db().cursor()
    cur.execute("SELECT * FROM cheeps")
    return cur.fetchall()

def db_add_cheep(name, cheep):
    cur = get_db().cursor()
    t = str(time.time())
    cheep_info = (name, t, cheep)
    cur.execute("INSERT INTO cheeps VALUES (?, ?, ?)", cheep_info)
    get_db().commit()

@app.route("/")
def hello():
	cheeps = db_read_cheeps()
	print(cheeps)
	return render_template('index.html', loc=False)

@app.route("/api/cheep", methods=["POST"])
def receive_cheep():
    print(request.form)
    db_add_cheep(request.form['name'], request.form['cheep'])
    location = [float(i) for i in request.form['name'].split(",")] #TODO
    closest_stop = findcloseststop(location[0], location[1])
    return render_template('index.html', loc=closest_stop)

if __name__ == "__main__":
	app.debug = True
	app.run()
