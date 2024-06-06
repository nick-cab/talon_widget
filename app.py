from flask import Flask,render_template,request
app = Flask(__name__)
from pymongo import MongoClient
from datetime import datetime
from time import sleep
cluster = MongoClient("mongodb+srv://smcs2026talontech:lUxhcscK1PDAhJxm@talontracker.k6uzv05.mongodb.net/?retryWrites=true&w=majority&appName=TalonTracker")
db = cluster["Tracker"]
locations = db["Locations"]
#chrome://net-internals/#sockets

@app.route("/", methods= ["POST","GET"])
def index():
    c = locations.find_one({"current": True})
    if c == None:
        currentLocation = "UNAVAILABLE"
    else:
        currentLocation = c["locN"]
    return render_template('index.html',current = currentLocation)

if __name__ == "__main__":
    app.run(debug=True)
    cluster.close()
