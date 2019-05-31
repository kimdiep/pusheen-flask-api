from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine, and_, text
from sqlalchemy.orm import sessionmaker

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://kimdiep:test123@localhost/pusheen'
db = SQLAlchemy(app)

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

if __name__=="__main__":
    app.run(debug=True)