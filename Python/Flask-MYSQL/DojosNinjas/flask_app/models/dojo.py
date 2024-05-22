# import the function that will return an instance of a connection
from flask_app.config.mysqlconnection import connectToMySQL


# model the class after the friend table from our database
class Dojo:
    db_name = "dojos_and_ninjas_schema"

    def __init__(self, data):
        self.id = data["id"]
        self.name = data["name"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

    # Now we use class methods to query our database
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM dojos;"
        # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL(cls.db_name).query_db(query)
        # Create an empty list to append our instances of friends
        dojos = []
        # Iterate over the db results and create instances of friends with cls.
        if results:
            for dojo in results:
                dojos.append(dojo)
        return dojos
    @classmethod
    def get_dojo_by_id(cls, data):
        query = "SELECT * FROM dojos where id=%(id)s;"
        # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL(cls.db_name).query_db(query,data)
        # Create an empty list to append our instances of friends
        dojos = []
        # Iterate over the db results and create instances of friends with cls.
        if results:
            for dojo in results:
                dojos.append(dojo)
        return dojos[0]
    @classmethod
    def create(cls, data):
        query = "INSERT INTO dojos (name) VALUES(%(name)s);"
        return connectToMySQL(cls.db_name).query_db(query, data)
