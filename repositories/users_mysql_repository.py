import models_mysql
import mysql.connector


class UsersMysqlRepository:
    def __init__(self, con):
        self.con = con

    def get_all(self):
        with self.con.cursor() as cur:
            cur.execute('SELECT * FROM users')
            result = cur.fetchall()
            users = []
            for user in result:
                users.append(models_mysql.User(user[0], user[1], user[2], user[3]))

            return users
