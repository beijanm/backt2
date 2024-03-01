import json
from flask import Blueprint, request, jsonify, current_app, Response
from flask_restful import Api, Resource
from datetime import datetime
# Assuming you have a similar authentication middleware for token verification
from auth_middleware import token_required 
import json
from flask import Flask
from flask_cors import CORS

from model.ballers import db, Baller, Stat

from flask import Blueprint, request, jsonify
from flask_restful import Api, Resource
from datetime import datetime
from model.ballers import Baller  # Ensure this import matches your project structure

baller_api = Blueprint('baller_api', __name__, url_prefix='/api/ballers')
api = Api(baller_api)

class BallerCRUD(Resource):
    def post(self):
        body = request.get_json()

        name = body.get('name')
        if name is None or len(name) < 2:
            return {'message': 'Name is missing, or is less than 2 characters'}, 400

        team = body.get('team')
        if team is None or len(team) < 2:
            return {'message': 'Team is missing, or is less than 2 characters'}, 400

        points_per_game = body.get('points_per_game')
        if points_per_game is None:
            return {'message': 'Points per game is missing'}, 400

        player = Baller(name=name, team=team, points_per_game=points_per_game)
        try:
            player.create()
            return jsonify(player.read()), 201
        except Exception as e:
            return {'message': str(e)}, 400

    def get(self):
        ballers = Baller.query.all()
        return jsonify([baller.read() for baller in ballers])
    
    def delete(self):
        body = request.get_json(force=True)  # Use force=True to ignore the mimetype
        name = body.get('name')
        
        if not name:
            return {'message': 'Name is required.'}, 400

        # Assuming name is a combination of first and last name
        ballers = Baller.query.filter_by(name=name).all()
        
        if ballers:
            try:
                for baller in ballers:
                    db.session.delete(baller)
                db.session.commit()
                return {'message': f'Baller(s) with name {name} deleted.'}, 200
            except Exception as e:
                db.session.rollback()
                return {'message': str(e)}, 500
        else:
            return {'message': f'Baller with name {name} not found.'}, 404
        
class PlayerStats(Resource):
    def get(self, player_id):
        stats = Stat.query.filter_by(player_id=player_id).all()
        if stats:
            return jsonify([stat.read() for stat in stats])
        else:
            return {'message': 'No stats available for this player'}, 404

    def post(self, player_id):
        body = request.get_json()
        # Ensure all required fields are present
        if not all(key in body for key in ('points_per_game', 'assists_per_game', 'rebounds_per_game')):
            return {'message': 'Missing stats data'}, 400

        new_stat = Stat(
            player_id=player_id,
            points_per_game=body['points_per_game'],
            assists_per_game=body['assists_per_game'],
            rebounds_per_game=body['rebounds_per_game']
        )

        try:
            db.session.add(new_stat)
            db.session.commit()
            return jsonify(new_stat.serialize()), 201  # Ensure you have a serialize method for Stat
        except Exception as e:
            db.session.rollback()
            return {'message': str(e)}, 500
        
    def put(self, player_id):
        body = request.get_json()
        # Ensure all required fields are present
        if not all(key in body for key in ('points_per_game', 'assists_per_game', 'rebounds_per_game')):
            return {'message': 'Missing stats data'}, 400

        stat = Stat.query.filter_by(player_id=player_id).first()
        if stat:
            stat.points_per_game = body['points_per_game']
            stat.assists_per_game = body['assists_per_game']
            stat.rebounds_per_game = body['rebounds_per_game']
        else:
            # Option to create new stats if not found, or return an error
            return {'message': 'Stats for this player not found, consider adding them instead.'}, 404

        try:
            db.session.commit()
            return (stat.read()), 200
        except Exception as e:
            db.session.rollback()
            return {'message': str(e)}, 500

        

# Add the CRUD resource to the API
api.add_resource(BallerCRUD, '/')
api.add_resource(PlayerStats, '/<int:player_id>/stats', methods=['GET', 'POST', 'PUT'])


