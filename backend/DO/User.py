import db
from db import movie_db, movie_db_db
import json


class User(object):
    password = ""
    rcmd_movie_id = [

    ]
    id = ""

    def __init__(self):
        pass

    @staticmethod
    def query_by_id(id):
        mycol = movie_db_db["user"]
        resp = mycol.find_one({
            'id': id
        })
        print(resp)
        ret = User()
        ret.password = resp['password']
        ret.id = resp['id']
        ret.rcmd_movie_id = resp['rcmd_movie_id']
        return ret

    def to_json(self):
        string = json.dumps(self.__dict__)
        return string


if __name__ == '__main__':
    id_1 = User.query_by_id('1')
    print(id_1.to_json())
