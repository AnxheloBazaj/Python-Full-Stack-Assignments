# import the function that will return an instance of a connection
from flask_app.config.mysqlconnection import connectToMySQL


# model the class after the friend table from our database
class User:
    db_name = "books_schema"

    def __init__(self, data):
        self.id = data["id"]
        self.first_name = data["first_name"]
        self.last_name = data["last_name"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

    # Now we use class methods to query our database
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL(cls.db_name).query_db(query)
        # Create an empty list to append our instances of friends
        users = []
        # Iterate over the db results and create instances of friends with cls.
        if results:
            for user in results:
                users.append(user)
            return users

    @classmethod
    def get_user_by_id(cls, data):
        query = "SELECT * FROM users where id=%(id)s;"
        # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL(cls.db_name).query_db(query, data)
        # Create an empty list to append our instances of friends
        users = []
        # Iterate over the db results and create instances of friends with cls.
        if results:
            for user in results:
                users.append(user)
            return users[0]

    @classmethod
    def create(cls, data):
        query = "INSERT INTO users (first_name, last_name) VALUES(%(first_name)s, %(last_name)s);"
        return connectToMySQL(cls.db_name).query_db(query, data)

    @classmethod
    def get_all_fav_books(cls, data):
        query = "SELECT books.id, books.title, books.num_of_pages FROM books JOIN favourites ON books.id = favourites.book_id WHERE favourites.user_id = %(id)s;"
        results = connectToMySQL(cls.db_name).query_db(query, data)
        books = []
        if results:
            for book in results:
                books.append(book)
            return books
