CREATE TABLE pusheen (
  id SERIAL PRIMARY KEY,
  name VARCHAR(120),
  date_of_birth DATE
);

CREATE TABLE fav_food (
  id SERIAL PRIMARY KEY,
  food VARCHAR(120)
);

CREATE TABLE pusheen_fav_food (
  id SERIAL PRIMARY KEY,
  pusheen_id INTEGER REFERENCES pusheen(id),
  fav_food_id INTEGER REFERENCES fav_food(id)
);