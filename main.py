import os
from flask import Flask
from dotenv import load_dotenv
from pymongo import MongoClient
from routes import pages

load_dotenv()

MONGODB_URI="mongodb://mongo:U6jPLKApN8UBaWs1LbYK@containers-us-west-61.railway.app:7708"
app = Flask(__name__)
app.config["MONGODB_URI"] = MONGODB_URI
app.config["SECRET_KEY"] = os.environ.get(
    "SECRET_KEY", "pf9Wkove4IKEAXvy-cQkeDPhv9Cb3Ag-wyJILbq_dFw"
)
app.db = MongoClient(app.config["MONGODB_URI"]).get_database("movie-watchlist")

app.register_blueprint(pages)


if __name__=="__main__":
    app.run(debug=True,host='0.0.0.0')