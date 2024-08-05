from mysql_connector import MySQLConnector as c

# Task 1: Add a Member

class MemberAdder:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def get_name(self):
        return self.__name
    
    def get_age(self):
        return self.__age
    
    def set_name(self, new_name):
        self.__name = new_name

    def set_age(self, new_age):
        self.__age = new_age

    def add_member(self):
        conn = c.connect_database()

        if conn:
            try:
                cursor = conn.cursor()
                new_member = (self.get_name(), self.get_age())
                
                # Inserts values into "Members" table
                main_query = """
                INSERT INTO Members (name, age)
                VALUES
                (%s, %s);
                """

                cursor.execute(main_query, new_member)
                
                conn.commit()

                print("New member added successfully!")
            except Exception as e:
                print(f"Error: {e}.")
            finally:
                cursor.close()
                conn.close()

member_adder = MemberAdder("Jayde Nicholson", 35) # Provides "name" and "age" as attributes of object "member_adder"

member_adder.add_member()

# Task 2: Add a Workout Session

class WorkoutSessionAdder:
    def __init__(self, member_id, date, duration_minutes, calories_burned):
        self.__member_id = member_id
        self.__date = date
        self.__duration_minutes = duration_minutes
        self.__calories_burned = calories_burned

    def get_member_id(self):
        return self.__member_id
    
    def get_date(self):
        return self.__date
    
    def get_duration_minutes(self):
        return self.__duration_minutes
    
    def get_calories_burned(self):
        return self.__calories_burned
    
    def set_member_id(self, new_member_id):
        self.__member_id = new_member_id

    def set_date(self, new_date):
        self.__date = new_date

    def set_duration_minutes(self, new_duration_minutes):
        self.__duration_minutes = new_duration_minutes

    def set_calories_burned(self, new_calories_burned):
        self.__calories_burned = new_calories_burned

    def add_workout_session(self):
        conn = c.connect_database()

        if conn:
            try:
                cursor = conn.cursor()
                new_workout_session = (self.get_member_id(), self.get_date(), self.get_duration_minutes(), self.get_calories_burned())

                # Inserts values into "WorkoutSessions" table
                main_query = """
                INSERT INTO WorkoutSessions (member_id, date, duration_minutes, calories_burned)
                VALUES
                (%s, %s, %s, %s);
                """

                cursor.execute(main_query, new_workout_session)

                conn.commit()

                print("New workout session added successfully!")
            except Exception as e:
                print(f"Error: {e}.")
            finally:
                cursor.close()
                conn.close()

workout_session_adder = WorkoutSessionAdder(31, "2024-08-04", 45, 600) 
# Provides "member_id", "date", "duration_minutes", and "calories_burned" as attributes of object "workout_session_adder"

workout_session_adder.add_workout_session()

# Task 3: Updating Member Information

class MemberAgeUpdater:
    def __init__(self, id, new_age):
        self.__id = id
        self.__new_age = new_age

    def get_id(self):
        return self.__id
    
    def get_new_age(self):
        return self.__new_age
    
    def set_id(self, new_id):
        self.__id = new_id

    def set_new_age(self, new_new_age):
        self.__new_age = new_new_age

    def update_member_age(self):
        conn = c.connect_database()

        if conn:
            try:
                cursor = conn.cursor()

                # Selects all "id"s from Members to ensure "id" attribute exists in table
                selection_query = "SELECT id FROM Members;"

                cursor.execute(selection_query)

                # Checks if "id" exists and raises ValueError if not
                if self.get_id() not in [id[0] for id in cursor.fetchall()]:
                    raise ValueError("Cannot update member age. This id does not exist")

                update_information = (self.get_new_age(), self.get_id())

                # Updates member in "Members" table with new age
                main_query = """
                UPDATE Members
                SET age = %s
                WHERE id = %s;
                """
                
                cursor.execute(main_query, update_information)

                conn.commit()

                print("Age updated successfully!")
            except ValueError as v:
                print(f"Error: {v}.")
            except Exception as e:
                print(f"Error: {e}.")
            finally:
                cursor.close()
                conn.close()

member_age_updater = MemberAgeUpdater(31, 36) # Provides "id" and "new_age" as attributes of object "member_age_updater"

member_age_updater.update_member_age()

# Task 4: Delete a Workout Session

class WorkoutSessionDeleter:
    def __init__(self, member_id):
        self.__member_id = member_id

    def get_member_id(self):
        return self.__member_id
    
    def set_member_id(self, new_member_id):
        self.__member_id = new_member_id

    def delete_workout_session(self):
        conn = c.connect_database()

        if conn:
            try:
                cursor = conn.cursor()

                # Selects all "member_id"s from Members to ensure "member_id" attribute exists in table
                selection_query = "SELECT member_id FROM WorkoutSessions;"

                cursor.execute(selection_query)

                # Checks if "member_id" exists and raises ValueError if not
                if self.get_member_id() not in [member_id[0] for member_id in cursor.fetchall()]:
                    raise ValueError("Cannot delete workout session. This member id does not exist")

                member_id_to_delete = (self.get_member_id(),)

                # Deletes entry with selected "member_id" from "WorkoutSessions"
                main_query = """
                DELETE FROM WorkoutSessions
                WHERE member_id = %s;
                """

                cursor.execute(main_query, member_id_to_delete)

                conn.commit()

                print("Workout session deleted successfully!")
            except ValueError as v:
                print(f"Error: {v}.")
            except Exception as e:
                print(f"Error: {e}.")
            finally:
                cursor.close()
                conn.close()

workout_session_deleter = WorkoutSessionDeleter(31) # Provides "member_id" as attribute of object "workout_session_deleter"

workout_session_deleter.delete_workout_session()