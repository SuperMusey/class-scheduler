from app.utils.database_manager import DatabaseManager
from app.services.courses_combinations import CourseCombinations
import os



def handle_data(dataFromRequest):
    # For each class in array
    #   find all rows with the courses course_id
    #   put into dict
    #   use algorithm
    #   return
    database_path = os.path.join(os.path.dirname(__file__), "database", "CoursesTable.sqlite")
    db_manager = DatabaseManager(db_file=database_path)
    requested_course_info = db_manager.get_data(dataFromRequest)   
    course_combinations = CourseCombinations(coursedata=requested_course_info)
    return course_combinations.createCombination()