import sys
sys.path.append('./models')

from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine, and_, text
from sqlalchemy.orm import sessionmaker

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://kimdiep:test123@localhost/pusheen'
db = SQLAlchemy(app)

from pusheen_food import *

def create_session(config):
    engine = create_engine(config['SQLALCHEMY_DATABASE_URI'])
    Session = sessionmaker(bind=engine)
    session = Session()
    session._model_changes = {}
    return session

manual_session = create_session(app.config)

@app.route('/')
def index():
    return 'hello world!'

@app.route('/api/get_pusheen', methods=['GET'])
def get_pusheen():
    return jsonify([
    {'id': pusheen.id, 'name': pusheen.name, 'date_of_birth': pusheen.date_of_birth}
    for pusheen in Pusheen.query.all()
  ])

@app.route('/api/create_pusheen', methods=["POST"])
def create_pusheen():
    dict_body = request.get_json()
    print(dict_body)
    pusheen = Pusheen(name=dict_body['name'],
                      date_of_birth=dict_body['date_of_birth'])
    manual_session.add(pusheen)
    manual_session.commit() 
    return jsonify({'message': 'Hey, a pusheen has been successfully created! Woohoo!'}), 200

@app.route('/api/get_food', methods=['GET'])
def get_food():
    return jsonify([
    {'id': food.id, 'food': food.food}
    for food in Food.query.all()
  ])

@app.route('/api/create_food', methods=["POST"])
def create_food():
    dict_body = request.get_json()
    print(dict_body)
    food = Food(food=dict_body['food'])
    manual_session.add(food)
    manual_session.commit()
    return jsonify({'message': 'Hey, a food item has been successfully created! Woohoo!'}), 200


if __name__=="__main__":
    app.run(debug=True)