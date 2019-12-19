import pymongo
import redis
import time

pool = redis.ConnectionPool(host='47.101.151.170', port=6379, decode_responses=True)
redis_serve = redis.Redis(connection_pool=pool)

myclient = pymongo.MongoClient("mongodb://47.101.151.170:27017")
movie_db = myclient["movieDB"]
movie_db_db = myclient["movieDB"]

if __name__ == '__main__':
    mycol = movie_db_db["detail"]
    a = mycol.find_one({
        'movie_id':'177209',
    })
    print(a)
