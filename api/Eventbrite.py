from flask import Flask, Blueprint, jsonify
from flask_restful import Api, Resource
import requests
import os

# Environment variables simulation (Replace these lines with actual environment variable setting in production)
os.environ['EVENTBRITE_PUBLIC_TOKEN'] = 'Z6GK7TDVPBMZJVRCZ2RL'
# For demonstration purposes only - Ensure to use secure storage for your tokens in real applications

eventbrite_api = Blueprint('eventbrite_api', __name__, url_prefix='/api/eventbrite')
api = Api(eventbrite_api)

class EventbriteEvents(Resource):
    def get(self, genre):
        api_key = os.environ.get('EVENTBRITE_PUBLIC_TOKEN')
        url = f"https://www.eventbriteapi.com/v3/events/search/?q={genre}&token={api_key}"
        headers = {"Authorization": f"Bearer {api_key}"}
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return jsonify(response.json())
        else:
            return jsonify({"error": "Failed to fetch events from Eventbrite"})

# Adjust the route to include a genre parameter
api.add_resource(EventbriteEvents, '/events/<string:genre>')

if __name__ == "__main__":
    app = Flask(__name__)
    app.register_blueprint(eventbrite_api)
    # Ensure your server is running in a secure environment before enabling public access
    app.run(debug=True, port=8086)
