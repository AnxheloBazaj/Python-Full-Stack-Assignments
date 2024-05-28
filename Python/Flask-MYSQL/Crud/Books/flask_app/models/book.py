# import the function that will return an instance of a connection
from flask_app.config.mysqlconnection import connectToMySQL


# model the class after the friend table from our database
class Book:
    db_name = "books_schema"

    def __init__(self, data):
        self.id = data["id"]
        self.title = data["title"]
        self.num_of_pages = data["num_of_pages"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

    # Now we use class methods to query our database
    @classmethod
    def get_book_by_id(cls, data):
        query = "SELECT * FROM books WHERE id=%(id)s;"
        # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL(cls.db_name).query_db(query, data)
        # Create an empty list to append our instances of friends
        books = []
        # Iterate over the db results and create instances of friends with cls.
        if results:
            for book in results:
                books.append(book)
            return books[0]

    @classmethod
    def create(cls, data):
        query = "INSERT INTO books (title, num_of_pages) VALUES(%(title)s,%(num_of_pages)s);"
        return connectToMySQL(cls.db_name).query_db(query, data)

    @classmethod
    def get_books(cls):
        query = "SELECT * FROM books;"
        # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL(cls.db_name).query_db(query)
        # Create an empty list to append our instances of friends
        books = []
        # Iterate over the db results and create instances of friends with cls.
        if results:
            for book in results:
                books.append(book)
        return books

    @classmethod
    def update(cls, data):
        query = "UPDATE ninjas SET first_name =%(first_name)s , last_name=%(last_name)s , age= %(age)s WHERE id =%(id)s;"
        return connectToMySQL(cls.db_name).query_db(query, data)

    @classmethod
    def delete(cls, data):
        query = "DELETE FROM ninjas WHERE id =%(id)s;"
        return connectToMySQL(cls.db_name).query_db(query, data)

    @classmethod
    def addFav(cls, data):
        query = (
            "INSERT INTO favourites (user_id, book_id) VALUES(%(user_id)s,%(book_id)s);"
        )
        return connectToMySQL(cls.db_name).query_db(query, data)

    @classmethod
    def get_all_user_fav(cls, data):
        query = "SELECT users.id, users.first_name, users.last_name FROM users JOIN favourites ON users.id = favourites.user_id WHERE favourites.book_id =%(id)s"
        results = connectToMySQL(cls.db_name).query_db(query, data)
        users = []
        if results:
            for user in results:
                users.append(user)
            return users
