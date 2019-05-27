import requests as rqs
from flask import Flask, jsonify
from flask_api import status
import json

app = Flask('mock-json-service')

POSTS_URL = 'https://jsonplaceholder.typicode.com/posts'

@app.route('/')
def posts():
    res = rqs.get(POSTS_URL)
    if res.status_code != 200:
        return jsonify({ 'message': 'Unable to fetch posts.' }), status.HTTP_500_INTERNAL_SERVER_ERROR 
    posts = json.loads(res.content)    
    return jsonify({ 'count': len(posts), 'data': posts })