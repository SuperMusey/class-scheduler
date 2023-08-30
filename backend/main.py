from flask import Flask
from app.routes.api import api  # Import the 'api' instance
from app.routes.api import ClassData  # Import the 'ClassData' route
from flask_cors import CORS
from app.services.scrapers.StudentLink import StudentLinkScraper

app = Flask(__name__)
CORS(app)
api.init_app(app)  # Initialize the 'api' instance with the Flask app

@app.route('/')
def hello():
    return "hello"

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)
