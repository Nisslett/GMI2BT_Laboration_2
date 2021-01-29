import modules
from common import input_int,error_msg,press_any_key
from file_operations import CSVfile, Jsonfile

class Menu:
    def __init__(self):
        self.csvfile=CSVfile("labb2-personer.csv",encodeing="utf-8-sig")
        self.jsonfile=Jsonfile("person.json")
        self.person_list=None
    #menu alternative 1
    def read_from_file(self):
        print(f"Fetching list from file [{self.csvfile.filename}]")
        self.person_list=self.csvfile.load_dict_list()
        if len(self.person_list)>0:
            print("The list has been fetched.")
        else:
            print("List is empty.")
        press_any_key()

    #menu alternative 2
    def showing_json_data(self):
        print("Showing List.")
        jsonstr=str(self.person_list).replace("[","[\n").replace("{","\t{").replace("},","},\n").replace("}]","}\n]")
        print(jsonstr)
        press_any_key()

    #menu alternative 3
    def add_person(self):
        print("Adding a person:")
        firstname=input("Please type in the firstname:")
        lastname=input("Please type in the lastname:")
        email=input("Please type in the email:")
        self.person_list.append({"firstname":firstname,"lastname":lastname,"email":email})
        
    def find_person_menu(self):
        while True:
            print("Search menu. Search for:")
            print("1. firstname\n2. lastname\n3. email\n4. go back to main menu")
            choice=input_int("Please type in your choice:","Invalid choice! Try again!")
            if choice==4:
                break
            if choice<1 or choice>4:
                continue
            #key=
            #modules.find_person(plist,)
        
    #menu alternative 5
    def save_list(self):
        if len(self.person_list)==0:
            error_msg("Can't save file! List is empty!")
            press_any_key()
            return
        print(f"Saveing list to file.[{self.jsonfile.filename}]")
        self.jsonfile.save_to_json()
        press_any_key()

    def start(self):
        while True:
            print("\nLaboration 2 - GMI2BT - Nils Broberg")
            #menu text
            print(f"1. Read in [{self.csvfile.filename}]\n2. Show List\n3. Add person\n4. Remove person\n5. Save to json\n6. Exit\n")
            choice=input_int("Please type in your choice:","Invalid choice! Try again!")
            if choice==1:
                self.read_from_file()
            elif choice==2:
                self.showing_json_data()
            elif choice==3:
                self.add_person()
            elif choice==4:
                pass
            elif choice==5:
                self.save_list()
            elif choice==6:
                break