# API for getting data from Elasticsearch
# import required packages
from flask import Flask
from flask import request
from flask_cors import CORS
import json
import requests
import urllib

app = Flask(__name__)
CORS(app) #enable cors

@app.route("/")
def hello():
    return "Hello World!"
    
# main route
@app.route("/search", methods=['GET', 'POST'])
def search():
    payload = request.data
    api_url = 'http://localhost:9200/my-tweets/_search'
    headers = {'Content-Type': 'application/json','User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36'}
    response = requests.post(api_url,data=payload, headers=headers)
    if response.status_code == 200:
        return response.content.decode('utf-8')
    else:
        return 'None'


if __name__ == '__main__':
    app.run(debug=True)