from person import Person
from common import input_int,error_msg,press_any_key,is_empty
from file_operations import CSVfile, Jsonfile

class Menu:
    def __init__(self):
        self.csvfile=CSVfile("labb2-personer.csv",encodeing="utf-8-sig")
        self.jsonfile=Jsonfile("person.json")
        self.person_list=[]
        self.main_menu_text=[f"Read in csv file[{self.csvfile.filename}]",
                             "Show List","Add person","Remove person","Find person",
                             f"Save to json [{self.jsonfile.filename}]",
                             f"Load from json [{self.jsonfile.filename}]",
                             "Exit"]
        self.find_menu_text=["Username","Firstname","Lastname","Email",
                             "Telephonenumber","Adress","Any attribute","Go back"]
        self.invalid_choice="Invalid choice! Try again!"
        self.type_in_choice="Please type in your choice:"
        
    def print_menu_text(self,text_list):
        for i in range(len(text_list)):
            print(str(f"[{i+1}] ")+text_list[i])
    
    #menu alternative 1
    def read_from_file(self):
        print(f"Fetching list from file [{self.csvfile.filename}]")
        self.person_list=Person.dict_to_person_list(self.csvfile.load_dict_list())
        if len(self.person_list)>0:
            print("The list has been fetched.")
        else:
            print("List is empty.")
        press_any_key()

    #menu alternative 2
    def showing_json_data(self):
        print("Showing List.")
        pad=[20,25,12,16,18]
        heads=["Firstname","LastName","Username","Email","Telephonenumber","Adress"]
        head_str=""
        for i in range(len(heads)):
            if i==(len(heads)-1):
                head_str+=heads[i]
            else:    
                head_str+=heads[i].ljust(pad[i])
        print(head_str)
        for person in self.person_list:
            tmp_string=person.firstname.ljust(pad[0])+person.lastname.ljust(pad[1])+person.username.ljust(pad[2])+person.email.ljust(pad[3])
            if person.is_telephonenumber():
                tmp_string+=person.telephonenumber.ljust(pad[4])
            if person.is_adress():
                tmp_string+=person.adress
            print(tmp_string)
        press_any_key()

    #menu alternative 3
    def add_person(self):
        print("Adding a person:")
        username=input("Please type in the username:")
        firstname=input("Please type in the firstname:")
        lastname=input("Please type in the lastname:")
        email=input("Please type in the email:")
        telephonenumber=input("Please type in the telephonenumber:")
        adress=input("Please type in the adress:")
        self.person_list.append(Person(username,firstname,lastname,email,telephonenumber,adress))
    
    #menu alternative 6
    def find_person_menu(self):
        pass
        
    #menu alternative 6
    def save_json_list(self):
        if is_empty(self.person_list):
            error_msg("Can't save file! List is empty!")
            press_any_key()
            return
        print(f"Saveing list to file.[{self.jsonfile.filename}]")
        self.jsonfile.save_to_json(Person.person_to_dict_list(self.person_list))
        press_any_key()
    
    #menu alternative 7
    def load_json_list(self):
        self.person_list=Person.dict_to_person_list(self.jsonfile.load_from_json())

    def find_person(self):
        while True:
            print("Search menu. Search for:")
            self.print_menu_text(self.find_menu_text)
            choice=input_int(self.type_in_choice,self.invalid_choice)
            if choice>8 and choice<1:
                error_msg("Invalid option! Try again!")
                continue
            if choice==8:
                print("Going Back")
                break
            
            

    def start(self):
        while True:
            print("\nLaboration 2 - GMI2BT - Nils Broberg")
            self.print_menu_text(self.main_menu_text)
            choice=input_int(self.type_in_choice,self.invalid_choice)
            if choice==8:
                break
            elif choice==1:
                self.read_from_file()
            elif choice==2:
                self.showing_json_data()
            elif choice==3:
                self.add_person()
            elif choice==4:
                #remove
                pass
            elif choice==5:
                self.find_person_menu()
            elif choice==6:
                self.save_json_list()
            elif choice==7:
                self.load_json_list()
            else:
                error_msg(self.invalid_choice)