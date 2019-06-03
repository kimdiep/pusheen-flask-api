import sys
sys.path.append('../')

from datetime import date
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from main import db

from sqlalchemy import create_engine, and_, text
from sqlalchemy.orm import sessionmaker

class Pusheen(db.Model):
    __tablename__ = 'pusheen'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=False, nullable=True)
    date_of_birth = db.Column(db.Date, unique=False, nullable=True)
    pusheen_fav_food = db.relationship('PusheenFavFood', backref='pusheen', lazy='dynamic')

    def __repr__(self):
        return '<Pusheen %r>' % self.name

    def __init__(self, name, date_of_birth):
        self.name = name
        self.date_of_birth = date_of_birth

class Food(db.Model):
    __tablename__ = 'fav_food'
    id = db.Column(db.Integer, primary_key=True)
    food = db.Column(db.String(120), unique=False, nullable=True)
    pusheen_fav_food = db.relationship('PusheenFavFood', backref='fav_food', lazy='dynamic')

    def __repr__(self):
        return '<Pusheen %r>' % self.name
    
    def __init__(self, food):
        self.food = food

class PusheenFavFood(db.Model):
    __tablename__ = 'pusheen_fav_food'
    id = db.Column(db.Integer, primary_key=True)
    pusheen_id = db.Column(db.Integer, db.ForeignKey('pusheen.id'))
    fav_food_id = db.Column(db.Integer, db.ForeignKey('fav_food.id'))