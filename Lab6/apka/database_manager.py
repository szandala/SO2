from pymongo import MongoClient


def add_user(username):
    client = MongoClient("database", 27017)

    user = {"username": username}
    users = client.sub_db.users #
    # client["sub_db"]["users"]
    users.insert_one(user)
