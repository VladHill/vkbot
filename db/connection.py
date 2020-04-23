import pymysql.cursors
import requests

def connect():
    connection = pymysql.connect(host='localhost',
                                 user='root',
                                 password='',
                                 db='vkbot',
                                 cursorclass=pymysql.cursors.DictCursor)
    return(connection)


