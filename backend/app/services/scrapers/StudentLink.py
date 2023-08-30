from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
import ratemyprofessor
from config.constants import *
from datetime import datetime
import time
import pickle
import os

class StudentLinkScraper:
    def __init__(self):
        self.coursesDict = {}
        self.picklepath = ""

    def __picklestorage__(self,college):
        # Subfolder name
        subfolder_name = 'Data'
        if not os.path.exists(subfolder_name):
            os.makedirs(subfolder_name)
        # Path to the pickle file inside the subfolder
        self.picklepath = os.path.join(subfolder_name, college+'_data.pkl')
    
    def open_pickle(self,college):
        data = ""
        with open(os.path.join('Data', college+'_data.pkl'), "rb") as pickle_file:
            data = pickle.load(pickle_file)
        return data
    
    def getRmpRating(self,class_name,instructor):
        professor = ratemyprofessor.get_professor_by_course_and_name_for_bu(class_name[-5:], instructor)
        if professor is not None:
            return professor.rating
        return 0

    def scrape(self):
        # Create a new instance of the Chrome driver
        driver = webdriver.Chrome()
        # Navigate to the login page
        driver.get("https://student.bu.edu/MyBU/s/")
        input("Press Enter to continue after entering Login and Duo Info:")
        driver.get("https://www.bu.edu/link/bin/uiscgi_studentlink.pl/1693187810?&ModuleName=reg%2Fadd%2F_start.pl&KeySem=20243&ViewSem=Fall%202023&AddPlannerInd=Y")
        
        # Parse classes
        # Lecture <=> Independent are interchangable
        # Any day/time may be Arranged
        # Table => Course    | Instructor | Type      | Day | Start | Stop
        # Typ 1 => CASAS101  | Name       | Lec       | T,R | 9:00am| 12:00pm
        # Typ 2 => CASAS202  | Name       | Lec       | Arr |       |
        # Typ 3 => CASAS303  | Name       | Lec       | Tues| 9:00am| 12:00pm
        #                                 | Lab/      | day | time  | time
        # Typ 4 => CASAS404  | Name       | Lec       | Arr |       | 
        # Typ 5 => CASAS505  | Name       | Disc/Lab  | day | time  | time (May be Directed Studies)
        # Typ 6 => CASAS606  | Name       | Lec       | day | time  | time
        #                                             | day | time  | time 
        # Typ 7 => CASAS707  | Name       | Lec       | Tues| 9:00am| 12:00pm
        #                                 | Lab       | day | time  | time
        #                                 | Dis       | day | time  | time
        # Typ 8 => CASAS808  | Name       | Lec       | day | time  | time 
        #                                             |Nov..|

        # Do not include -> Typ 5, Typ 7
        # Keep Lab/Disc/Directed Study only if paired with Lec -> Typ 3

        # td_elements should have:
        # 0 - Flag
        # 1 - Align
        # 2 - Class
        # 3 - Title/Instructor
        # 4 - Align
        # 5 - Open Seats
        # 6 - Cr Hrs
        # 7 - Type
        # 8 - Bld
        # 9 - Room
        # 10 - Day
        # 11 - Start
        # 12 - Stop
        # 13 - Notes
        college = input("Enter college you want to scrape\n")
        class_to_start = input("Enter class to start scraping from if applicable else enter 'n'\n")
        if class_to_start.lower() != 'n':
            college = college+"_fromafter_"+class_to_start
        self.__picklestorage__(college=college)
        input("Select the college to scrape in the website and go to class to scrape from if applicable\npress Enter....\n")
        try:
            while True:
                ContinueSearchFromButton = driver.find_element(By.XPATH,"/html/body/form/center[2]/table/tbody/tr/td[2]/input") 
                tbody = driver.find_element(By.XPATH,"/html/body/form/table[1]/tbody")
                tr_elements = tbody.find_elements(By.TAG_NAME, "tr")
                for tr in tr_elements:
                    td_elements = tr.find_elements(By.TAG_NAME, "td")
                    if len(td_elements)>=13:
                        if td_elements[CLASS].text and ("Lecture" in td_elements[TYPE].text or "Independent" in td_elements[TYPE].text) and (len(td_elements[TYPE].text.split())<=2): #Typ 5,7 ignored
                            class_name = "".join(td_elements[CLASS].text.split()[:-1])
                            instructor = td_elements[TITLE_INSTRUCTOR].text.split()[-1]
                            day = [
                                [DAY_MAP[day.strip()] for day in day_collection.split(',') if day.strip() in DAY_MAP]
                                  for day_collection in td_elements[DAY].text.split()
                                  ]
                            day = [sub_day for sub_day in day if sub_day] # Remove empty arrays
                            start_time = [int(datetime.strptime(stime,"%I:%M%p").strftime("%H%M")) for stime in td_elements[11].text.split()]
                            end_time = [int(datetime.strptime(etime,"%I:%M%p").strftime("%H%M")) for etime in td_elements[12].text.split()]

                            # Make start and end time to have 0's when day is 'A'
                            for idx, days in enumerate(day):
                                if 'A' in days:
                                    if idx == 0:
                                        start_time = [0] + start_time
                                        end_time = [0] + end_time
                                    elif idx == 1:
                                        start_time = start_time + [0]
                                        end_time = end_time + [0]

                            rating = self.getRmpRating(class_name=class_name,instructor=instructor)

                            # Store data into dict
                            if self.coursesDict.get(class_name) is None:
                                self.coursesDict[class_name] = []
                            self.coursesDict[class_name].append({
                                'prof':instructor,
                                'rating':rating,
                                'starttime':start_time,
                                'endtime':end_time,
                                'days':day
                            })

                            # Print or process the extracted information
                            print("Class:", class_name)
                            print("Instructor:", instructor)
                            print("Rating:",rating)
                            print("Type:", td_elements[TYPE].text)
                            print("Day:", day)
                            print("Start Time:", start_time)
                            print("Stop Time:", end_time)
                            print("=" * 40)  # Separation line

                with open(self.picklepath, 'wb') as pickle_file:
                    pickle.dump(self.coursesDict, pickle_file)
                print("Saved to ",self.picklepath)

                driver.execute_script("arguments[0].click();", ContinueSearchFromButton)
                time.sleep(2)
        except NoSuchElementException:
            input("Enter...")
            print("Done")
            driver.quit()

