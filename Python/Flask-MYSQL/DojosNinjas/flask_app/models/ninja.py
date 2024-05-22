# import the function that will return an instance of a connection
from flask_app.config.mysqlconnection import connectToMySQL


# model the class after the friend table from our database
class Ninja:
    db_name = "dojos_and_ninjas_schema"

    def __init__(self, data):
        self.id = data["id"]
        self.first_name = data["first_name"]
        self.last_name = data["last_name"]
        self.age = data["age"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        self.dojo_id = data["dojo_id"]

    # Now we use class methods to query our database
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM ninjas;"
        # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL(cls.db_name).query_db(query)
        # Create an empty list to append our instances of friends
        ninjas = []
        # Iterate over the db results and create instances of friends with cls.
        if results:
            for ninja in results:
                ninjas.append(cls(ninja))
        return ninja

    @classmethod
    def create(cls, data):
        query = "INSERT INTO ninjas (first_name, last_name, age, dojo_id) VALUES(%(first_name)s,%(last_name)s,%(age)s,%(dojo_id)s)"
        return connectToMySQL(cls.db_name).query_db(query, data)
    
    @classmethod
    def get_ninjas_by_id(cls, data):
        query = "SELECT * FROM ninjas where dojo_id = %(id)s;"
        # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL(cls.db_name).query_db(query,data)
        # Create an empty list to append our instances of friends
        ninjas = []
        # Iterate over the db results and create instances of friends with cls.
        if results:
            for ninja in results:
                ninjas.append(ninja)
        return ninjas
