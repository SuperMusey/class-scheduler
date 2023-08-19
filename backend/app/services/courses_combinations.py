from itertools import product

class CourseCombinations:
    def __init__(self, coursedata):
        self.coursedata = coursedata #from the db tables
        self.combinations = []

    #create combinations based on data from table
    def createCombination(self):
        for key,values in self.coursedata.items():
            for value in values:
                value['course'] = key

        all_combinations = []
        # all_combinations will be an array of tuples where each tuple contains dicts of the class info for that combination
        for combination in product(*(self.coursedata[key] for key in self.coursedata)):
            all_combinations.append(combination)

        result = [self.checkValidCombo(combo) for combo in all_combinations]
        for index, isValid in enumerate(result):
            if isValid:
                current_valid_combo = all_combinations[index]  
                avgrating = 0 
                for course in current_valid_combo:
                    avgrating = avgrating + course['rating']
                avgrating = avgrating/len(current_valid_combo)
                self.combinations.append({'avgrating':avgrating,'tabledata':list(current_valid_combo)})
        
        return sorted(self.combinations,key=lambda x:x['avgrating'],reverse=True)

    def extract_time_slots(self,course):
        starttimes = course['starttime']
        endtimes = course['endtime']
        days = course['days']
        time_slots = [(start, end, day) for start, end, day in zip(starttimes, endtimes, days)]
        return time_slots

    #check validity of combo
    def checkValidCombo(self,class_combination):
        time_slots_by_course = {course['course']: self.extract_time_slots(course) for course in class_combination}

        for course, section_timings in time_slots_by_course.items():
            cross_check_with_courses = {key: value for key, value in time_slots_by_course.items() if key != course}
            for specific_section in section_timings:
                starttime_of_section, endtime_of_section, days_of_section = specific_section
                for course_cross_check, cross_check_timings in cross_check_with_courses.items():
                    for cross_check_section in cross_check_timings:
                        starttime_of_crosscheck, endtime_of_crosscheck, days_of_crosscheck = cross_check_section
                        if any(day in days_of_crosscheck for day in days_of_section) and 'A' not in days_of_section and 'A' not in days_of_crosscheck:
                            if (
                                (starttime_of_section <= starttime_of_crosscheck <= endtime_of_section) or
                                (starttime_of_section <= endtime_of_crosscheck <= endtime_of_section) or
                                (starttime_of_section >= starttime_of_crosscheck and endtime_of_section <= endtime_of_crosscheck)
                            ):
                                return False
                    
        return True
    
    #calculate avg rating
    def averageRating(self,data):
        pass