from app.utils.database_manager import DatabaseManager
import os



def handle_data(dataFromRequest):
    # For each class in array
    #   find all rows with the courses course_id
    #   put into dict
    #   use algorithm
    #   return
    print(dataFromRequest)
    database_path = os.path.join(os.path.dirname(__file__), "database", "CoursesTable.sqlite")
    db_manager = DatabaseManager(database_path)
    requested_course_info = db_manager.get_data(dataFromRequest)   
    print(requested_course_info)
    return 0