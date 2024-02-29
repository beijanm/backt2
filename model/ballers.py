import json
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError
from datetime import datetime, date
from random import randrange
from datetime import date
import os, base64
import json

from __init__ import app, db
from sqlalchemy.exc import IntegrityError
from werkzeug.security import generate_password_hash, check_password_hash



class Baller(db.Model):
    __tablename__ = 'ballers'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), unique=True, nullable=False)
    team = db.Column(db.String(255), nullable=False)
    dob = db.Column(db.Date)
    stats = db.relationship("Stat", cascade='all, delete', backref='players', lazy=True)

    def __init__(self, name, team, dob=date.today()):
        self.name = name
        self.team = team
        self.dob = dob

    def create(self):
        try:
            db.session.add(self)
            db.session.commit()
            return self
        except IntegrityError:
            db.session.remove()
            return None

    def read(self):
        return {
            "id": self.id,
            "name": self.name,
            "team": self.team,
            "dob": self.dob.strftime('%Y-%m-%d'),
            "stats": [stat.read() for stat in self.stats]
        }

class Stat(db.Model):
    __tablename__ = 'stats'

    id = db.Column(db.Integer, primary_key=True)
    player_id = db.Column(db.Integer, db.ForeignKey('ballers.id'))
    points_per_game = db.Column(db.Float, nullable=False)
    assists_per_game = db.Column(db.Float, nullable=False)
    rebounds_per_game = db.Column(db.Float, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __init__(self, player_id, points_per_game, assists_per_game, rebounds_per_game):
        self.player_id = player_id
        self.points_per_game = points_per_game
        self.assists_per_game = assists_per_game
        self.rebounds_per_game = rebounds_per_game

    def create(self):
        try:
            db.session.add(self)
            db.session.commit()
            return self
        except IntegrityError:
            db.session.remove()
            return None

    def read(self):
        return {
            "id": self.id,
            "player_id": self.player_id,
            "points_per_game": self.points_per_game,
            "assists_per_game": self.assists_per_game,
            "rebounds_per_game": self.rebounds_per_game,
            "created_at": self.created_at.strftime('%Y-%m-%d %H:%M:%S')
        }


def initBallers():
    with app.app_context():
        db.create_all()  # Creates all tables if they don't exist
        players = [
            Baller(name='LeBron James', team='Los Angeles Lakers', dob=date(1984, 12, 30)),
            Baller(name='Kevin Durant', team='Brooklyn Nets', dob=date(1988, 9, 29)),
            Baller(name='Stephen Curry', team='Golden State Warriors', dob=date(1988, 3, 14)),
            Baller(name='Giannis Antetokounmpo', team='Milwaukee Bucks', dob=date(1994, 12, 6)),
            Baller(name='Luka Dončić', team='Dallas Mavericks', dob=date(1999, 2, 28))
        ]

        for player in players:
            try:
                player.create()
            except IntegrityError:
                db.session.rollback()
                print(f"Failed to add {Baller.name}, possible duplicate")