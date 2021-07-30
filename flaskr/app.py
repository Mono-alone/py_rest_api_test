from dataclasses import dataclass

from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
db_uri = 'sqlite:///C:\\Users\\egor.rybakov\\test.db'
app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
db = SQLAlchemy(app)


@app.route('/')
def index():
    return 'Hello, world!'


@app.route('/user/<username>')
def user(username):
    user_mapper = UserMapper()
    if username is None:
        return jsonify(user_mapper.to_dto(u) for u in User.query.all())
    else:
        found_user = User.query.filter_by(username=username).first()
        return jsonify(user_mapper.to_dto(found_user))


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)


@dataclass
class UserDto:
    id: int
    username: str
    email: str


class UserMapper:
    def to_dto(self, u):
        return UserDto(id=u.id, username=u.username, email=u.email)
