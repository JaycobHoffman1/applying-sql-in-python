from mysql_connector import MySQLConnector as c

# Task 1: SQL BETWEEN Usage

class SelectorWithBetween:
    def __init__(self, start_age, end_age):
        self.__start_age = start_age
        self.__end_age = end_age

    def get_start_age(self):
        return self.__start_age
    
    def get_end_age(self):
        return self.__end_age
    
    def set_start_age(self, new_start_age):
        self.__start_age = new_start_age

    def set_end_age(self, new_end_age):
        self.__end_age = new_end_age

    def get_members_in_age_range(self):
        conn = c.connect_database()

        if conn:
            try:
                cursor = conn.cursor()
                age_range = (self.get_start_age(), self.get_end_age())

                # Selects entries in "Members" table whose ages fall in specified range
                query = """
                SELECT * FROM Members
                WHERE age BETWEEN %s AND %s;
                """

                cursor.execute(query, age_range)

                print("Members selected successfully!")

                for member in cursor.fetchall():
                    print(member)
            except Exception as e:
                print(f"Error: {e}.")
            finally:
                cursor.close()
                conn.close()

selector_with_between = SelectorWithBetween(25, 30) # Provides "start_age" and "end_age" as attributes of object "selector_with_between"

selector_with_between.get_members_in_age_range()