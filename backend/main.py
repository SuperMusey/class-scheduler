from flask import Flask
from flask_restx import Resource, Api

app = Flask(__name__)

@app.route('/')
def hello():
    return "hello"

@app.route('/data')
def classData():
    return 'data'

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)