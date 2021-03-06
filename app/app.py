from flask import Flask, request, jsonify

import json

app = Flask(__name__)


@app.after_request
def add_headers(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Headers'] =  "Content-Type, Access-Control-Allow-Headers, Authorization, X-Requested-With"
    response.headers['Access-Control-Allow-Methods']=  "GET"
    return response


@app.route("/")
def hello():
    return "Hello World!"



if __name__ == "__main__":

    app.run(debug=True, host='0.0.0.0', port=8888)
