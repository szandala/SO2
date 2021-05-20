from pymongo import MongoClient


def add_user(username):
    user = {"username": username}
    client = MongoClient("database", 27017)

    users = client.my_db.users
    user_id = users.insert_one(user)
