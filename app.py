from flask import Flask,render_template,request
app = Flask(__name__)
from pymongo import MongoClient
from datetime import datetime
import calendar
cluster = MongoClient("mongodb+srv://smcs2026talontech:lUxhcscK1PDAhJxm@talontracker.k6uzv05.mongodb.net/?retryWrites=true&w=majority&appName=TalonTracker")
db = cluster["Tracker"]
locations = db["Locations"]
#chrome://net-internals/#sockets
def to_integer(dt_time):
    return f"{calendar.month_name[dt_time.month]} {dt_time.day} { dt_time.strftime('%-I:%M%p') }"

@app.route("/", methods= ["POST","GET"])
def index():
    c = locations.find_one({"current": True})
    rn = datetime.utcnow()
    if c == None:
        currentLocation = "UNAVAILABLE"
        t = to_integer(locations.find_one({"n":"notavail"})["c"])
    else:
        currentLocation = c["locN"]
        t = to_integer(c["time"])
    return render_template('index.html',current = currentLocation,time = t)

if __name__ == "__main__":
    app.run(debug=True)
    cluster.close()
