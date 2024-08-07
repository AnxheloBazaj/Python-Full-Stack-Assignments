from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash


class Team:
    db_name = "footballteams"

    def __init__(self, data):
        self.id = data["id"]
        self.name = data["name"]
        self.founded = data["founded"]
        self.league = data["league"]
        self.nrOfPlayers = data["nrOfPlayers"]
        self.homeStadium = data["homeStadium"]
        self.trophies = data["trophies"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        self.user_id = data["user_id"]

    @classmethod
    def get_all_Teams(cls):
        query = "SELECT * FROM teams"
        result = connectToMySQL(cls.db_name).query_db(query)
        teams = []
        if result:
            for team in result:
                teams.append(team)
            return teams

    @classmethod
    def create(cls, data):
        query = "INSERT INTO teams (name, founded, league, homeStadium, trophies, user_id) VALUES(%(name)s,%(founded)s,%(league)s,%(homeStadium)s,%(trophies)s,%(user_id)s)"
        return connectToMySQL(cls.db_name).query_db(query, data)

    @classmethod
    def update_team(cls, data):
        query = "UPDATE teams SET name = %(name)s, founded = %(founded)s, league = %(league)s,trophies = %(trophies)s,nrOfPlayers = %(nrOfPlayers)s, homeStadium = %(homeStadium)s WHERE id = %(team_id)s;"
        return connectToMySQL(cls.db_name).query_db(query, data)

    @classmethod
    def delete_team(cls, data):
        query = "DELETE FROM teams WHERE id = %(team_id)s;"
        return connectToMySQL(cls.db_name).query_db(query, data)

    @classmethod
    def get_team_by_id(cls, data):
        query = "SELECT * FROM teams left join users on teams.user_id = users.id WHERE teams.id = %(team_id)s"
        result = connectToMySQL(cls.db_name).query_db(query, data)
        if result:
            return result[0]
        return False

    @classmethod
    def delete_users_team(cls, data):
        query = "DELETE FROM teams WHERE teams.user_id = %(id)s;"
        return connectToMySQL(cls.db_name).query_db(query, data)

    @classmethod
    def addLike(cls, data):
        query = "INSERT INTO likes (user_id, team_id) VALUES (%(id)s, %(team_id)s);"
        return connectToMySQL(cls.db_name).query_db(query, data)

    @classmethod
    def removeLike(cls, data):
        query = "DELETE FROM likes where team_id = %(team_id)s and user_id = %(id)s;"
        return connectToMySQL(cls.db_name).query_db(query, data)

    def get_likers(cls, data):
        query = "SELECT user_id from likes where likes.team_id = %(team_id)s;"
        results = connectToMySQL(cls.db_name).query_db(query, data)
        likers = []
        if results:
            for person in results:
                likers.append(person["user_id"])
        return likers

    @classmethod
    def get_likers_info(cls, data):
        query = "SELECT * from likes left join users on likes.user_id = users.id where likes.team_id = %(team_id)s;"
        results = connectToMySQL(cls.db_name).query_db(query, data)
        likers = []
        if results:
            for person in results:
                likers.append(person)
        return likers

    # @classmethod
    # def get_user_by_email(cls, data):
    #     query = "SELECT * FROM users WHERE email = %(email)s"
    #     result = connectToMySQL(cls.db_name).query_db(query, data)
    #     if result:
    #         return result[0]
    #     return False
    @staticmethod
    def validate_team(data):
        is_valid = True
        # test whether a field matches the pattern
        if len(data["name"]) < 3:
            flash("Team name should be at least 3 characters!", "name")
            is_valid = False
        if not data["founded"]:
            flash("The year that the team was founded is required!", "founded")
            is_valid = False
        if len(data["league"]) < 3:
            flash("League name should be at least 3 characters!", "league")
            is_valid = False
        if len(data["homeStadium"]) < 3:
            flash("Stadium name required!", "homeStadium")
            is_valid = False
        if not data["trophies"]:
            flash("The trophies number is required!", "trophies")
            is_valid = False
        if "nrOfPlayers" in data:
            if int(data["nrOfPlayers"]) < 0 or int(data["nrOfPlayers"]) > 26:
                flash(
                    "Number of players is required to be between 0-26!", "nrOfPlayers"
                )
                is_valid = False
        return is_valid
