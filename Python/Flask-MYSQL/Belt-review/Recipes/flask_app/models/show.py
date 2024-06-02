from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash


class Show:
    db_name = "showsschema"

    def __init__(self, data):
        self.id = data["id"]
        self.title = data["title"]
        self.releaseDate = data["releaseDate"]
        self.description = data["description"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        self.user_id = data["user_id"]

    @classmethod
    def get_all_Shows(cls):
        query = "SELECT * FROM shows"
        result = connectToMySQL(cls.db_name).query_db(query)
        shows = []
        if result:
            for show in result:
                shows.append(show)
            return shows

    @classmethod
    def create(cls, data):
        query = "INSERT INTO shows (title, network, releaseDate, description, user_id) VALUES(%(title)s, %(network)s, %(releaseDate)s,%(description)s,%(user_id)s)"
        return connectToMySQL(cls.db_name).query_db(query, data)

    @classmethod
    def update_show(cls, data):
        query = "UPDATE shows SET title = %(title)s, network=%(network)s, releaseDate = %(releaseDate)s, description = %(description)s  WHERE id = %(show_id)s;"
        return connectToMySQL(cls.db_name).query_db(query, data)

    @classmethod
    def delete_show(cls, data):
        query = "DELETE FROM shows WHERE id = %(show_id)s;"
        return connectToMySQL(cls.db_name).query_db(query, data)

    @classmethod
    def get_show_by_id(cls, data):
        query = "SELECT * FROM shows left join users on shows.user_id = users.id WHERE shows.id = %(show_id)s"
        result = connectToMySQL(cls.db_name).query_db(query, data)
        if result:
            return result[0]
        return False

    @classmethod
    def delete_users_show(cls, data):
        query = "DELETE FROM shows WHERE shows.user_id = %(id)s;"
        return connectToMySQL(cls.db_name).query_db(query, data)

    @classmethod
    def addLike(cls, data):
        query = "INSERT INTO likes (user_id, show_id) VALUES (%(id)s, %(show_id)s);"
        return connectToMySQL(cls.db_name).query_db(query, data)

    @classmethod
    def removeLike(cls, data):
        query = "DELETE FROM likes where show_id = %(show_id)s and user_id = %(id)s;"
        return connectToMySQL(cls.db_name).query_db(query, data)

    @classmethod
    def get_users_who_liked(cls, data):
        query = "SELECT user_id from likes where likes.show_id = %(show_id)s;"
        results = connectToMySQL(cls.db_name).query_db(query, data)
        uswersWhoLiked = []
        if results:
            for person in results:
                uswersWhoLiked.append(person["user_id"])
        return uswersWhoLiked

    @classmethod
    def delete_all_likes(cls, data):
        query = "DELETE FROM likes where show_id = %(show_id)s;"
        return connectToMySQL(cls.db_name).query_db(query, data)

    @staticmethod
    def validate_show(data):
        is_valid = True
        # test whether a field matches the pattern
        if len(data["title"]) < 3:
            flash("Title should be at least 3 characters!", "title")
            is_valid = False
        if len(data["network"]) < 3:
            flash("Network be at least 3 characters!", "network")
            is_valid = False
        if not data["releaseDate"]:
            flash("The year that the show was released is required!", "releaseDate")
            is_valid = False
        if len(data["description"]) < 3:
            flash("Description should be at least 3 characters!", "description")
            is_valid = False
        return is_valid
