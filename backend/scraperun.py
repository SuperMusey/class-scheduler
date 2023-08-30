from app.services.scrapers.StudentLink import StudentLinkScraper
from app.utils.picklehandler import PickleHandler

if __name__ == "__main__":
    scraperobj = StudentLinkScraper()
    choice = input("Scrape (1) or access pickles (2)\n")
    choice = int(choice)
    if choice==1:
        scraperobj.scrape()
    elif choice==2:
        list_files = [
            "CAS_fromafter_CASLJ111-Staff",
        ]
        pickleObj = PickleHandler()
        pickleObj.open_named_pickles(list_pickles=list_files)

        pickleObj.view_last_n_entries(list_files[0],1)
        pickleObj.view_first_n_entries(list_files[0],1)

        pickleObj.view_first_n_entries(list_files[1],1)

        # pickleObj.delete_keys(list_files[0],["CASBI421"])
        # pickleObj.view_last_n_entries(list_files[0],2)
        # pickleObj.view_first_n_entries(list_files[1],2)
        # print("-"*40)
        # pickleObj.view_last_n_entries(list_files[1],2)
        # pickleObj.view_first_n_entries(list_files[2],2)
        # pickleObj.view_last_n_entries(list_files[2],1)
        # print("-"*40)
        # pickleObj.append_data(list_files,"CAS_fromafter_CASLJ111-Staff")



