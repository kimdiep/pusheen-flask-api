# pusheen-flask-api

This is my personal project to create a a Pusheen API server using Flask and SQLAlchemy. P.S. Pusheen is a cat =(^.^)=

## Features


## Motivation: What are my goals for this project?

I want to learn more about:

- Python
- Flask server API
- SQLAlchemy
- Postman

## Build status

## Code style

## Screenshots

## Tech/framework used

- Python
- Flask
- SQLAlchemy

SQLAlchemy is the Python SQL toolkit and Object Relational Mapper that gives application developers the full power and flexibility of SQL.
https://www.sqlalchemy.org/

- psycopg2-binary
Psycopg is the most popular PostgreSQL database adapter for the Python programming language.


## Code Example

## Getting started/Installation

`git clone https://github.com/kimdiep/pusheen-flask-api.git`

```bash
pip3 install -r requirements.txt # to install python dependencies
```

Ensure postgresql is installed, on macOS:
`brew install postgresql`

- Postman
Go to this link to install Postman:
https://www.getpostman.com/downloads/

### Creating a database and database tables in psql using SQLAlchemy

1. Enter `psql` to connect to the database server
2. `CREATE DATABASE "pusheen";` will create a database for pusheen
3. `\l` to list database to ensure `pusheen` is a database, `\q` to quit psql server
4. In the root directory, start `python3` and enter the following commands to initialise database tables from the `pusheen.py` SQLAlchemy model:

```python

>>> from main import db
>>> db.create_all()
>>> exit()

```

## How to use?

To start up the Flask API server: 
`python3 main.py`

As an example to test, open up postman and do a POST request to `http://localhost:5000/create_pusheen` with the body:

```json
{
    "name":"Pusheen",
    "date_of_birth":"2019-01-01"
}
```

The data will be posted to the API endpoint `create_pusheen`.

## Credits

## License

MIT © 2019 thekimmykola (Kim Diep)
