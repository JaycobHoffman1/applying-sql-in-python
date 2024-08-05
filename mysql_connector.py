import mysql.connector
from mysql.connector import Error

class MySQLConnector:
    def connect_database():
        db_name = "gym_db"
        user = "root"
        password = "Jajoconi@1"
        host = "localhost"

        try:
            conn = mysql.connector.connect(
                database = db_name,
                user = user,
                password = password,
                host = host
            )

            if conn.is_connected():
                print("Connected to the MySQL server successfully!")

                return conn
        except Error as e:
            print(f"Error: {e}")

            return None