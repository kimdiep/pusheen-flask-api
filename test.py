import sys
sys.path.append('./models')

from datetime import datetime
import json
from flask_testing import TestCase
import unittest
from main import app, db
from pusheen_food import *

class TestingViews(TestCase):

  #creates instance of flask app
  def create_app(self):
    app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///testing.db'
    return app

  def setUp(self):
    db.create_all()
    date = datetime(2019, 1, 1, 0, 0, 0)
    pusheen1 = Pusheen("Pusheen", date)
    pusheen2 = Pusheen("Pusheenicorn", date)
    food1 = Food("muffin")
    food2 = Food("chocolate")
    db.session.add_all([pusheen1, pusheen2, food1, food2])
    db.session.commit()
    
  def test_homepage(self):
    response = self.client.get('/', content_type = 'html/text')
    self.assertEqual(response.status_code, 200)
    self.assertIn(b'hello world!', response.data)

  def test_get_pusheen(self):
    response = self.client.get('/api/get_pusheen', content_type = 'html/text')
    self.assertEqual(response.status_code, 200)
    self.assertIn(b'Pusheen', response.data)
    self.assertIn(b'Pusheenicorn', response.data)

  # def test_creates_pusheen(self):
  #   response = self.client.post('/api/create_pusheen', 
  #     data = json.dumps(dict(name = "Classic Pusheen", date_of_birth = "2019-01-01")),
  #     content_type = 'application/json',
  #     follow_redirects = True
  #   )
  #   self.assertIn(b'{"message":"Hey, a pusheen has been successfully created! Woohoo!"}\n', response.data)
  #   self.assertEqual(response.status_code, 200)
    
  def test_get_food(self):
    response = self.client.get('/api/get_food', content_type = 'html/text')
    self.assertEqual(response.status_code, 200)
    self.assertIn(b'muffin', response.data)
    self.assertIn(b'chocolate', response.data)

  # def test_creates_food_item(self):
  #   response=self.client.post('/api/create_food', 
  #     data = json.dumps(dict(food = "Cookies")),
  #     content_type = 'application/json',
  #     follow_redirects = True
  #   )
  #   self.assertIn(b'{"message":"Hey, a food item has been successfully created! Woohoo!"}\n', response.data)
  #   self.assertEqual(response.status_code, 200)

  def tearDown(self):
    db.drop_all()
    db.session.remove()


if __name__ == '__main__':
  unittest.main()



