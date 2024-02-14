from flask import Blueprint, jsonify  # jsonify creates an endpoint response object
from flask_restful import Api, Resource # used for REST API building
import requests  # used for testing 
import random
import http.client

from model.nbas import *

nba_api = Blueprint('nba_api', __name__,
                   url_prefix='/api/nba')

# API generator https://flask-restful.readthedocs.io/en/latest/api.html#id1
api = Api(nba_api)

class NbaAPI:
    # not implemented
    
    # getnba()
    class _Read(Resource):
        def get(self, nba):
            return jsonify(getNbaAPIData(nba))

    api.add_resource(_Read, '/players')

if __name__ == "__main__": 
    # server = "http://127.0.0.1:5000" # run local
    server = 'http://127.0.0.1:8086' # run from web
    url = server + "/api/nba"
    responses = []  # responses list
    