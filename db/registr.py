from db.connection import connect

def registr(user_id):
    connection = connect()
    try:
        with connection.cursor() as cursor:
            result = cursor.execute(f"SELECT * FROM anketa where uid = {user_id}")
            row = cursor.fetchone()
            if result == 0:
                cursor.execute(f"insert into anketa(uid) values ({user_id}) ")
                connection.commit()
            else:
                return row
    finally:
        connection.close()
