from flask import Flask
from dotenv import load_dotenv
from pegasus.database import dbconnection
from pegasus.database import schema


db = dbconnection.DbConnection()

app = Flask(__name__)
 
@app.route("/")
def home_view():
        return "<h1>Bicho feio</h1>"

if __name__ == "__main__":
  app.run()