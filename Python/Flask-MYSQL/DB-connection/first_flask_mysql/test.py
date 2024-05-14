from flask_app.config.mysqlconnection import MySQLConnection
mysql = MySQLConnection("first_flask")
data={
    "first_name":"Agur",
    "last_name":"Bobinr1",
    "occupation":"Doctornr1"
}
query = "INSERT INTO friends(first_name, last_name, occupation, created_at, updated_at) Values(%(first_name)s, %(last_name)s, %(occupation)s, NOW(), NOW());"

mysql.query_db(query, data)