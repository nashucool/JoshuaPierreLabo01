"""
User DAO (Data Access Object) for MongoDB
SPDX - License - Identifier: LGPL - 3.0 - or -later
Auteurs : Gabriel C. Ullmann, Fabio Petrillo, 2025
"""

import os
from dotenv import load_dotenv
from pymongo import MongoClient
from bson.objectid import ObjectId

from models.user import User


class UserDAOMongo:
    def __init__(self):
        try:
            env_path = ".env"
            print(os.path.abspath(env_path))

            load_dotenv(dotenv_path=env_path)

            mongo_host = os.getenv("MONGODB_HOST")
            mongo_port = os.getenv("MONGODB_PORT")
            mongo_db = os.getenv("MONGODB_NAME")

            mongo_user = os.getenv("MONGO_INITDB_ROOT_USERNAME")
            mongo_pass = os.getenv("MONGO_INITDB_ROOT_PASSWORD")

            mongo_uri = (
                f"mongodb://{mongo_user}:{mongo_pass}"
                f"@{mongo_host}:{mongo_port}/"
                f"?authSource=admin"
            )

            self.client = MongoClient(mongo_uri)

            self.db = self.client[mongo_db]

            self.collection = self.db["users"]

        except FileNotFoundError:
            print("Attention : Veuillez créer un fichier .env")

        except Exception as e:
            print("Erreur : " + str(e))

    def select_all(self):
        """ Select all users from MongoDB """

        users = []

        for doc in self.collection.find():

            user = User(
                str(doc["_id"]),
                doc["name"],
                doc["email"]
            )

            users.append(user)

        return users

    def insert(self, user):
        """ Insert given user into MongoDB """

        result = self.collection.insert_one({
            "name": user.name,
            "email": user.email
        })

        return str(result.inserted_id)

    def update(self, user):
        """ Update given user in MongoDB """

        self.collection.update_one(
            {"_id": ObjectId(user.id)},
            {
                "$set": {
                    "name": user.name,
                    "email": user.email
                }
            }
        )

    def delete(self, user_id):
        """ Delete user from MongoDB with given user ID """

        self.collection.delete_one({
            "_id": ObjectId(user_id)
        })

    def delete_all(self):
        """ Delete all users from MongoDB """

        self.collection.delete_many({})

    def close(self):
        """ Close MongoDB connection """

        self.client.close()