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
    
# Task 1: Add a Member
# Defining a function to add a new member to the 'Members' table with error handling for constraint violations
def add_member(id, name, age):
    conn = connect_database()
    if conn is not None:
        try:
            cursor = conn.cursor()

            new_member = (id, name, age)
            query = "INSERT INTO Members (id, name, age) VALUES (%s, %s, %s)"
            cursor.execute(query, new_member)
            conn.commit()
            print("New member added to gym database.")

        except Exception as e:
            print(f"Error: {e}")

        finally:
            cursor.close()
            conn.close()

# Task 2: Add a Workout Session
# Defining a function to add a new workout session to the 'WorkoutSessions' table for a specific member with error handling for constraint violations
def add_workout_session(member_id, date, duration_minutes, calories_burned):
    conn = connect_database()
    if conn is not None:
        try:
            cursor = conn.cursor()

            new_session = (member_id, date, duration_minutes, calories_burned)
            query = "INSERT INTO WorkoutSessions (session_id, member_id, session_date, session_time, activity) VALUES (%s, %s, %s, %s, %s)"
            cursor.execute(query, new_session)
            conn.commit()
            print("New workout session added to gym database.")

        except Exception as e:
            print(f"Error: {e}")

        finally:
            cursor.close()
            conn.close()

# Task 3: Updating Member Information
# Defining a function to update the age of a member after checking whether the member exists
def update_member_age(member_id, new_age):
    conn = connect_database()
    if conn is not None:
        try:
            cursor = conn.cursor()

            updated_member = (new_age, member_id)
            query_check = "SELECT * FROM Members WHERE id = %s"
            cursor.execute(query_check, (member_id,))
            
            if cursor.fetchall():
                query = "UPDATE Members SET age = %s WHERE id = %s"
                cursor.execute(query, updated_member)
                conn.commit()
                print("Member age updated in gym database.")
            else:
                print("Member not found in gym database.")

        except Exception as e:
            print(f"Error: {e}")

        finally:
            cursor.close()
            conn.close()

# Task 4: Delete a Workout Session
# Defining a function to delete a workout session based on its 'session_id' with error handling for invalid IDs
def delete_workout_session(session_id):
    conn = connect_database()
    if conn is not None:
        try:
            cursor = conn.cursor()

            session_to_delete = (session_id,)
            query_check = "SELECT * FROM WorkoutSessions WHERE session_id = %s"
            cursor.execute(query_check, session_to_delete)

            if cursor.fetchall():
                query = "DELETE FROM WorkoutSessions WHERE session_id = %s"
                cursor.execute(query, session_to_delete)
                conn.commit()
                print("Workout session deleted from gym database.")
            else:
                print("Workout session not found in gym database.")

        except Exception as e:
            print(f"Error: {e}")

        finally:
            cursor.close()
            conn.close()