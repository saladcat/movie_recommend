import json
from db import movie_db, redis_serve
from untils.poster_geter import get_poster_src


class Movie(object):
    movie_id = ""
    genres = [

    ]
    title = ""
    total_rating = 0
    total_rating_people_nums = 0
    avg_rating = 0
    tmdbId = ""
    imdbId = ""

    def __init__(self):
        pass

    @staticmethod
    def query_by_id(id):
        redis_str = redis_serve.get(id)
        ret = Movie()
        if redis_str is None:
            mycol = movie_db["detail"]
            resp = mycol.find_one({
                'movie_id': id
            })
            if resp is None:
                print("{}是缺失".format(id))
            resp: dict
            if '_id' in resp:
                resp.pop('_id')
            resp["imdb_hyperlink"] = "https://www.imdb.com/title/tt" + resp["imdbId"]
            resp["img_src"] = get_poster_src(resp["imdb_hyperlink"])
            ret.__dict__ = resp
            print(resp)
            return ret

        print("from redis")
        movie_dict = json.loads(redis_str)
        ret.__dict__ = movie_dict
        return ret

    def to_json(self):
        ret = ""
        ret = self.__dict__
        string = json.dumps(ret)
        redis_serve.set(ret["movie_id"], string, ex=60 * 60 * 24 * 3, nx=True)
        return string


if __name__ == '__main__':
    # id_100010 = Movie.query_by_id("1")
    # print(id_100010.to_json())
    mycol = movie_db["detail"]
    resp = mycol.find()
    cnt = 0
    for item in resp:
        cnt += 1
    print(cnt)
