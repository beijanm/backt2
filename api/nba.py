 
from flask import Blueprint, jsonify
from flask_restful import Api, Resource
import requests

from model.nbas import getNbaAPIData

nba_api = Blueprint('nba_api', __name__, url_prefix='/api/nba')
api = Api(nba_api)

class NbaAPI(Resource):
    def get(self):
        # Example: Fetch all NBA players data
        nba_data = getNbaAPIData()
        return jsonify(nba_data)

# Adjust the route accordingly
api.add_resource(NbaAPI, '/players')

if __name__ == "__main__":
    from flask import Flask
    app = Flask(__name__)
    app.register_blueprint(nba_api)
    app.run(debug=True, port=8086)
