from app.services.scrapers.StudentLink import StudentLinkScraper
from app.utils.picklehandler import PickleHandler

#Look at CASEN306 value data, 
# [{'prof': 'Kearnan', 'rating': 0, 'starttime': [1630], 'endtime': [1815], 'days': [['M']]}, 
# [{'prof': 'Davis', 'rating': 5, 'starttime': [1230], 'endtime': [1515], 'days': [['R']]}]] -> extra []

if __name__ == "__main__":
    scraperobj = StudentLinkScraper()
    choice = input("Scrape (1) or access pickles (2)\n")
    choice = int(choice)
    if choice==1:
        scraperobj.scrape()
    elif choice==2:
        list_files = [
            "CAS_total"
        ]
        pickleObj = PickleHandler()
        pickleObj.open_named_pickles(list_pickles=list_files)
        pickleObj.view_first_n_entries(list_files[0],1)
        pickleObj.view_last_n_entries(list_files[0],1)
        