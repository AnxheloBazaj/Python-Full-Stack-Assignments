from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash


class Painting:
    db_name = "cars_schema"

    def __init__(self, data):
        self.id = data["id"]
        self.title = data["title"]
        self.description = data["description"]
        self.price = data["price"]
        self.quantity = data["quantity"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        self.user_id = data["user_id"]

    @classmethod
    def get_all_Paintings(cls):
        query = "SELECT * FROM paintings left join users on paintings.user_id = users.id"
        result = connectToMySQL(cls.db_name).query_db(query)
        paintings = []
        if result:
            for painting in result:
                paintings.append(painting)
            return paintings

    @classmethod
    def create(cls, data):
        query = "INSERT INTO paintings (model, description,price, make, user_id) VALUES(%(title)s, %(description)s, %(price)s, %(quantity)s,%(user_id)s)"
        return connectToMySQL(cls.db_name).query_db(query, data)

    @classmethod
    def update_paintig(cls, data):
        query = "UPDATE paintings SET title = %(title)s,  description = %(description)s, price=%(price)s, quantity = %(quantity)s WHERE id = %(painting_id)s;"
        return connectToMySQL(cls.db_name).query_db(query, data)

    @classmethod
    def delete_painting(cls, data):
        query = "DELETE FROM paintings WHERE id = %(painting_id)s;"
        return connectToMySQL(cls.db_name).query_db(query, data)

    @classmethod
    def get_painting_by_id(cls, data):
        query = "SELECT * FROM paintings left join users on paintings.user_id = users.id WHERE paintings.id = %(painting_id)s"
        result = connectToMySQL(cls.db_name).query_db(query, data)
        if result:
            return result[0]
        return False

    @classmethod
    def delete_users_paintings(cls, data):
        query = "DELETE FROM cars WHERE paintings.user_id = %(id)s;"
        return connectToMySQL(cls.db_name).query_db(query, data)

    # @classmethod
    # def addLike(cls, data):
    #     query = "INSERT INTO likes (user_id, show_id) VALUES (%(id)s, %(show_id)s);"
    #     return connectToMySQL(cls.db_name).query_db(query, data)

    # @classmethod
    # def removeLike(cls, data):
    #     query = "DELETE FROM likes where show_id = %(show_id)s and user_id = %(id)s;"
    #     return connectToMySQL(cls.db_name).query_db(query, data)

    # @classmethod
    # def get_users_who_liked(cls, data):
    #     query = "SELECT user_id from likes where likes.show_id = %(show_id)s;"
    #     results = connectToMySQL(cls.db_name).query_db(query, data)
    #     uswersWhoLiked = []
    #     if results:
    #         for person in results:
    #             uswersWhoLiked.append(person["user_id"])
    #     return uswersWhoLiked

    # @classmethod
    # def delete_all_likes(cls, data):
    #     query = "DELETE FROM likes where show_id = %(show_id)s;"
    #     return connectToMySQL(cls.db_name).query_db(query, data)

    @staticmethod
    def validate_painting(data):
        is_valid = True
        # test whether a field matches the pattern
        if len(data["title"]) < 3:
            flash("Title should be at least 3 characters!", "title")
            is_valid = False
        if int(data["quantity"]) <=0 :
            flash("Quantity must be greater than 0!", "quantity")
            is_valid = False
        if  int(data["price"])<=0:
            flash("The price must be greater than 0!", "price")
            is_valid = False
        if len(data["description"]) < 10:
            flash("Description should be at least 10 characters!", "description")
            is_valid = False
        return is_valid
