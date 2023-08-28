from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config.constants import daymapping
from datetime import datetime

class StudentLinkScraper:

    def scrape(self):
        # Create a new instance of the Chrome driver
        driver = webdriver.Chrome()
        
        # Navigate to the login page
        driver.get("https://student.bu.edu/MyBU/s/")
        input("Press Enter to continue after entering Login and Duo Info:")
        driver.get("https://www.bu.edu/link/bin/uiscgi_studentlink.pl/1693187810?&ModuleName=reg%2Fadd%2F_start.pl&KeySem=20243&ViewSem=Fall%202023&AddPlannerInd=Y")
        
        #parse classes
        input("Select the college to scrape and press Enter....")
        tbody = driver.find_element(By.XPATH,"/html/body/form/table[1]/tbody")
        tr_elements = tbody.find_elements(By.TAG_NAME, "tr")
        for tr in tr_elements:
            td_elements = tr.find_elements(By.TAG_NAME, "td")
            if len(td_elements)>=13:
                if td_elements[2].text and (td_elements[7].text == "Lecture" or td_elements[7].text == "Independent"):
                    class_name = "".join(td_elements[2].text.split()[:-1])
                    instructor = td_elements[3].text.split()[-1]
                    day = [daymapping[day.strip()] for day in td_elements[10].text.split(',')]
                    start_time = [int(datetime.strptime(stime,"%I:%M%p").strftime("%H%M")) for stime in td_elements[11].text.split()]
                    stop_time = [int(datetime.strptime(stime,"%I:%M%p").strftime("%H%M")) for stime in td_elements[12].text.split()]

                    # Print or process the extracted information
                    print("Class:", class_name)
                    print("Instructor:", instructor)
                    print("Day:", day)
                    print("Start Time:", start_time)
                    print("Stop Time:", stop_time)
                    print("=" * 40)  # Separation line

        input("Enter...")
        print("Done")
        driver.quit()

