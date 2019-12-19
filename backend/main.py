import json

from flask import Flask, request
from flask_cors import CORS

from DO.Movie import Movie
from DO.User import User
from db import movie_db_db

app = Flask(__name__)
CORS(app, supports_credentials=True)


@app.route('/')
def hello_world():
    return 'Hello World!'


def getPassword(user_id):
    return User.query_by_id(str(user_id)).password


@app.route('/login', methods=['post'])
def check_password():
    user_id = request.form.get('user_id')
    password = request.form.get('password')
    print(f"user_id={user_id}")
    print(f"password={password}")

    return json.dumps(password == getPassword(user_id))


@app.route('/recommend', methods=['get'])
def recommend_by_user_id():
    user_id = request.args.get("user_id")
    user = User.query_by_id(user_id)
    return json.dumps(user.rcmd_movie_id)


@app.route('/query_by_movie_id', methods=['get'])
def query_movie_by_id():
    movie_id = request.args.get("movie_id")
    movie = Movie.query_by_id(movie_id)
    return movie.to_json()


@app.route('/top_movie', methods=['get'])
def top_movie():
    mycol = movie_db_db["top10"]
    top10 = mycol.find()
    return json.dumps(top10[0]['top_rank'])


if __name__ == '__main__':
    app.run(
        port=5001,
    )
