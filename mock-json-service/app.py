import requests as rqs
from flask import Flask, jsonify
from flask_api import status
import json
import os

app = Flask('mock-json-service')

RETURN_404 = False

if 'RESOURCE' in os.environ:
    RESOURCE_NAME = os.environ['RESOURCE']
    if RESOURCE_NAME == 'posts':
        RESOURCE_URL = 'https://jsonplaceholder.typicode.com/posts'
    elif RESOURCE_NAME == 'albums':
        RESOURCE_URL = 'https://jsonplaceholder.typicode.com/albums'
    else:
        RETURN_404 = True
else:
    RETURN_404 = True

@app.route('/')
def resources():
    if RETURN_404:
        return jsonify({ 'message': 'Resource not found.'}), status.HTTP_404_NOT_FOUND
    res = rqs.get(RESOURCE_URL)
    if res.status_code != 200:
        return jsonify({ 'message': 'Unable to fetch resources.' }), status.HTTP_500_INTERNAL_SERVER_ERROR 
    resources = json.loads(res.content)    
    return jsonify({ 'name': RESOURCE_NAME, 'count': len(resources), 'data': resources })