import sqlite3
from app.models.test_data import datadict

class DatabaseManager:
    def __init__(self, db_file):
        self.db_file = db_file
        self.conn = None
        self.cursor = None

    def connect(self):
        self.conn = sqlite3.connect(self.db_file)
        self.cursor = self.conn.cursor()

    def close(self):
        if self.conn:
            self.conn.commit()
            self.conn.close()

    def insert_data(self):
        for course_code, course_data in datadict.items():
            self.cursor.execute("SELECT course_id FROM courses WHERE course_name = (?)",(course_code,))
            existing_course_id = self.cursor.fetchone() #if exists, gives course_id else none

            if existing_course_id:
                course_id = existing_course_id[0]
            else:
                self.cursor.execute("INSERT INTO courses (course_name) VALUES (?)", (course_code,))
                course_id = self.cursor.lastrowid
            
            for unique_class, course_info in enumerate(course_data):
                professor_name = course_info['prof']
                self.cursor.execute("SELECT professor_id FROM professors WHERE professor_name = ?", (professor_name,))
                existing_professor_id = self.cursor.fetchone() #if exists, gives professor_id else none

                if existing_professor_id:
                    professor_id = existing_professor_id[0]
                else:
                    self.cursor.execute("INSERT INTO professors (professor_name, rating) VALUES (?, ?)",
                                        (course_info['prof'], course_info['rating']))
                    professor_id = self.cursor.lastrowid

                class_start_times = course_info['starttime']
                for index, times in enumerate(class_start_times):
                    self.cursor.execute("INSERT INTO course_info (class_uniqueness_id, course_id, professor_id, start_time, end_time, days) VALUES (?, ?, ?, ?, ?, ?)",
                                   (unique_class, course_id, professor_id, course_info['starttime'][index], course_info['endtime'][index],''.join(course_info['days'][index])))
        
        self.conn.commit()

    def remove_data(self):
        tables = ['courses','professors','course_info']
        for table in tables:
            query = f"DELETE FROM {table}"
            self.cursor.execute(query)

    def run(self):
        try:
            self.connect()
            self.remove_data()
            self.insert_data()
        except sqlite3.Error as e:
            print("Error:", e)
        finally:
            self.close()


db_manager = DatabaseManager("../services/database/CoursesTable.sqlite")
db_manager.run()
