import pymysql.cursors
import requests
import random

class Bot():
    def __init__(self):
        self.connection()

    def connection(self):
        connect = pymysql.connect(host='localhost',
                                     user='root',
                                     password='',
                                     db='vkbot',
                                     cursorclass=pymysql.cursors.DictCursor)
        return connect

    def get_username(self, user_id, token):
        data = requests.get(f"https://api.vk.com/method/users.get?v=5.103&user_id={user_id}&access_token={token}")
        name = data.json()['response'][0]['first_name']
        return name

    #def get_userphoto(self, user_id, token):

    def get_profile(self, user_id):
        connect = Bot().connection()
        try:
            with connect.cursor() as cursor:
                result = cursor.execute(f"SELECT * FROM anketa WHERE gender = 'парень' order by rand() LIMIT 1")
                row = cursor.fetchone()
                return row
        finally:
            connect.close()

    def get_anketa(self, user_id):
        connect = Bot().connection()
        try:
            with connect.cursor() as cursor:
                result = cursor.execute(f"SELECT * FROM anketa WHERE uid={user_id}")
                row = cursor.fetchone()
                return row
        finally:
            connect.close()

    def insert_anketa_pm(self, user_id):
        connect = Bot().connection()
        try:
            with connect.cursor() as cursor:
                result = cursor.execute(f"SELECT * FROM anketa where uid = {user_id}")
                row = cursor.fetchone()
                if result == 1:
                    cursor.execute(f"UPDATE anketa SET poisk = 'парня' WHERE uid = {user_id}")
                    connect.commit()
                else:
                    return row
        finally:
            connect.close()

    def insert_anketa_pw(self, user_id):
        connect = Bot().connection()
        try:
            with connect.cursor() as cursor:
                result = cursor.execute(f"SELECT * FROM anketa where uid = {user_id}")
                row = cursor.fetchone()
                if result == 1:
                    cursor.execute(f"UPDATE anketa SET poisk = 'девушку' WHERE uid = {user_id}")
                    connect.commit()
                else:
                    return row
        finally:
            connect.close()

    def insert_anketa_m(self, user_id):
        connect = Bot().connection()
        try:
            with connect.cursor() as cursor:
                result = cursor.execute(f"SELECT * FROM anketa where uid = {user_id}")
                row = cursor.fetchone()
                if result == 1:
                    cursor.execute(f"UPDATE anketa SET gender = 'парень' WHERE uid = {user_id}")
                    connect.commit()
                else:
                    return row
        finally:
            connect.close()

    def insert_anketa_w(self, user_id):
        connect = Bot().connection()
        try:
            with connect.cursor() as cursor:
                result = cursor.execute(f"SELECT * FROM anketa where uid = {user_id}")
                row = cursor.fetchone()
                if result == 1:
                    cursor.execute(f"UPDATE anketa SET gender = 'девушка' WHERE uid = {user_id}")
                    connect.commit()
                else:
                    return row
        finally:
            connect.close()

    def reg(self, user_id):
        connect = Bot().connection()
        try:
            with connect.cursor() as cursor:
                result = cursor.execute(f"SELECT * FROM anketa where uid = {user_id}")
                row = cursor.fetchone()
                if result == 0:
                    cursor.execute(f"insert into anketa(uid) values ({user_id}) ")
                    connect.commit()
                else:
                    return row
        finally:
            connect.close()
bot = Bot()
