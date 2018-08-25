
from coursearrangement import python_mysql_connect2
from mysql.connector import Error

class DBHelper:

    # Instantiate a DBHelper object with the configured connection information
    def __init__(self, conn = python_mysql_connect2.connect()):
        self.conn = conn
    # Add a new user input record
    def add_module(self, course, index, number, time, kind, type):
        query = "INSERT IGNORE INTO allcourses(course, indexNo, {}, {}, {}) VALUES(\"{}\", {}, \"{}\", {}, \"{}\")".format("session" + str(number), "week" + str(number), "tag" + str(number), course, index, time, kind, type)
        print(query)
        try:
            print("inserting a new module...")
            cursor = self.conn.cursor()
            cursor.execute(query)
            self.conn.commit()
            cursor.close()
        except Error as err:
            print(err.msg)

    def update_module(self, index, number, time, kind, type):
        query1 = """UPDATE allcourses
                SET {} = \"{}\"
                 where indexNo = {}""".format("session" + str(number), time, index)
        query2 = """UPDATE allcourses
                SET {} = \"{}\"
                where indexNo = {}""".format("week" + str(number), kind, index)
        query3 = """UPDATE allcourses
                        SET {} = \"{}\"
                        where indexNo = {}""".format("tag" + str(number), type, index)
        try:
            cursor = self.conn.cursor()
            cursor.execute(query1)
            cursor.execute(query2)
            cursor.execute(query3)
            self.conn.commit()
            cursor.close()
        except Error as err:
            print(err)

    def get_course(self, name):
        query = "select indexNo, session1, week1, session2, week2, session3, week3, session4, week4, session5, week5, session6, week6 from allcourses where course = %s;"
        args = (name,)
        result = None
        try:
            cursor = self.conn.cursor()
            cursor.execute(query, args)
            result = cursor.fetchall()
            cursor.close()
        except Error as err:
            print(err)
        return result

    def get_info(self,name):
        query = "select session1, week1,tag1, session2, week2,tag2, session3, week3,tag3, session4, week4,tag4, session5, week5,tag5, session6, week6,tag6 from allcourses where indexNo = %s"
        args = (name,)
        try:
            cursor = self.conn.cursor()
            cursor.execute(query, args)
            result = cursor.fetchall()
            cursor.close()
            return result
        except Error as err:
            print(err)
