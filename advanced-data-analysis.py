import mysql.connector
from mysql.connector import Error

# Defining a function to connect the python script to the MySQL database 'fitness_center_db'
def connect_database():
    database = "fitness_center_db"
    user = "root"
    password = "Ago0#1!$"
    host = "127.0.0.1"

    try:
        conn = mysql.connector.connect(
            database = database,
            user = user,
            password = password,
            host = host
        )
        return conn

    except Error as e:
        print(f"Error: {e}")
        return None

# Task 1: SQL BETWEEN Usage
# Defining a function to retrieve the details of members whose ages fall between '25' and '30'
def get_members_in_age_range(start_age, end_age):
    conn = connect_database()
    if conn is not None:
        try:
            cursor = conn.cursor()

            query = "SELECT id, name, age FROM Members WHERE age BETWEEN %s AND %s"
            cursor.execute(query, (start_age, end_age))
            print(f"Members in age range {start_age}-{end_age}:")
            for member in cursor.fetchall():
                print(member)
        
        except Exception as e:
            print(f"Error: {e}")

        finally:
            cursor.close()
            conn.close()

# Calling the 'get_members_in_age_range()' function with the arguments '25' and '30'
get_members_in_age_range(25, 30)