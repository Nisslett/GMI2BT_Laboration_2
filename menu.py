from person import Person
from common import input_int, error_msg, press_any_key, is_empty, input_required
from file_operations import CSVfile, Jsonfile


class Menu:
    def __init__(self):
        self.csvfile = CSVfile("labb2-personer.csv", encodeing="utf-8-sig")
        self.jsonfile = Jsonfile("person.json")
        self.person_list = []
        #menu texts
        self.main_menu_text = [f"Read in csv file[{self.csvfile.filename}]",
                               "Show List", "Add person", "Remove person", "Find person",
                               f"Save to json [{self.jsonfile.filename}]",
                               f"Load from json [{self.jsonfile.filename}]",
                               "Exit"]
        self.find_menu_text = ["Username", "Firstname", "Lastname", "Email",
                               "Telephonenumber", "Adress", "Any attribute", "Go back"]
        self.remove_menu_text = ["Find and remove","Remove from index","Go back"]
        #repetable strings
        self.invalid_choice = "Invalid choice! Try again!"
        self.type_in_choice = "Please type in your choice:"

    def print_menu_text(self, text_list):
        for i in range(len(text_list)):
            print(str(f"[{i+1}] ")+text_list[i])

    # menu alternative 1
    def read_from_file(self):
        print(f"Fetching list from file [{self.csvfile.filename}]")
        self.person_list = Person.dict_to_person_list(
            self.csvfile.load_dict_list())
        if len(self.person_list) > 0:
            print("The list has been fetched.")
        else:
            print("List is empty.")
        press_any_key()

    # menu alternative 2
    def showing_json_data(self):
        print("Showing List.")
        print()  # spaceing
        Menu.print_list(self.person_list)
        print()  # spaceing
        press_any_key()

    # menu alternative 3

    def add_person(self):
        print("Inputs with a star are required.")
        print("Adding a person:")
        username = input_required("Please type in the username*:")
        firstname = input_required("Please type in the firstname*:")
        lastname = input_required("Please type in the lastname*:")
        email = input_required("Please type in the email*:")
        telephonenumber = input("Please type in the telephonenumber:").strip()
        if telephonenumber == "":
            telephonenumber = None
        adress = input("Please type in the adress:").strip()
        if adress == "":
            adress = None
        self.person_list.append(
            Person(username, firstname, lastname, email, telephonenumber, adress))

    # menu alternative 4

    def remove_person_menu(self):
        pass
        #find person
        print("Remove menu")
        self.print_menu_text(self.remove_person_menu)
        while True:
            input_int(self.type_in_choice,self.invalid_choice)
            
                
        #list persons if more then one
        
        #chose and ask to delete 
    
    def find_and_remove_person(self):
        pass
        
    def chose_person_menu(self,plist):
        print("\nChose the index of the person you wish to remove\n")
        Menu.print_list(plist,True)
        print(str(len(plist))+". Go back to menu.")
        while True:
            index=input_int(self.type_in_choice,"Invalid Input! Try again!")
            if 0<index and index<(len(plist)+1):
                error_msg("Invalid Input! Try again!")
                continue
            # this is the goback condition
            elif index==len(plist):
                return 
            break
        print(f"Removeing {plist[index].firstname} {plist[index].lastname} . . .")
        self.person_list.remove(plist[index])
        press_any_key()
    # menu alternative 5

    def find_person_menu(self):
        Menu.print_list(self.find_person())
        press_any_key()

    # menu alternative 6
    def save_json_list(self):
        if is_empty(self.person_list):
            error_msg("Can't save file! List is empty!")
            press_any_key()
            return
        print(f"Saveing list to file.[{self.jsonfile.filename}]")
        self.jsonfile.save_to_json(
            Person.person_to_dict_list(self.person_list))
        press_any_key()

    # menu alternative 7
    def load_json_list(self):
        self.person_list = Person.dict_to_person_list(
            self.jsonfile.load_from_json())

    # Generic function to print a list of Persons
    @staticmethod
    def print_list(person_list, index=False):
        offset = 1
        pad = [6, 12, 20, 25, 20, 18]
        # set the offset to decide if the index header should be included
        if index:
            offset = 0
        heads = Person.get_keylist()
        heads.insert(0, "Index")
        head_str = ""
        for i in range(offset, len(heads)):
            if i == (len(heads)-1):
                head_str += heads[i].title()
            else:
                head_str += heads[i].title().ljust(pad[i])
        # prints the header part
        print(head_str)
        for i in range(len(person_list)):
            person = person_list[i]
            tmp_string = ""
            # adds index as a variable in the list
            if index:
                tmp_string += str(i).ljust(pad[0])
            # adds all of the person data
            tmp_string += person.username.ljust(pad[0+offset])+person.firstname.ljust(
                pad[1+offset])+person.lastname.ljust(pad[2+offset])+person.email.ljust(pad[3+offset])
            if person.has_telephonenumber():
                tmp_string += person.telephonenumber.ljust(pad[4+offset])
            if person.has_adress():
                tmp_string += person.adress
            # prints the formated person entry
            print(tmp_string)

    def find_person(self):
        while True:
            print("Search menu. Search for:")
            self.print_menu_text(self.find_menu_text)
            choice = input_int(self.type_in_choice, self.invalid_choice)
            if choice > 8 and choice < 1:
                error_msg("Invalid option! Try again!")
                continue
            if choice == 8:
                print("Going Back")
                break
            option = Person.get_keylist()
            option.append("text")
            option = option[choice-1].title()
            search_string = input(
                f"Type in {option} your are searching for:").lower()
            found_list = []
            for person in self.person_list:
                if self.check_found(person, search_string, choice):
                    found_list.append(person)
            return found_list

    def check_found(self, person, search, choice):
        if choice == 7:
            if self.found_any(person, search):
                return True
        else:
            return self.found_key(person, search, choice)

    def found_any(self, person, search):
        key_list = Person.get_keylist()
        tmp_dict = Person.to_dict(person)
        for key in key_list:
            if (key == key_list[4] and not Person.has_telephonenumber(person)) or (key == key_list[5] and not Person.has_adress(person)):
                continue
            if not tmp_dict[key].lower().find(search) == -1:
                return True
        return False

    def found_key(self, person, search, choice):
        key_list = Person.get_keylist()
        tmp_dict = Person.to_dict(person)
        if (choice == 5 and not person.has_telephonenumber()) or (choice == 6 and not person.has_adress()):
            return False
        if not tmp_dict[key_list[choice-1]].lower().find(search) == -1:
            return True
        return False

    def start(self):
        while True:
            print("\nLaboration 2 - GMI2BT - Nils Broberg")
            self.print_menu_text(self.main_menu_text)
            choice = input_int(self.type_in_choice, self.invalid_choice)
            if choice == 8:
                break
            elif choice == 1:
                self.read_from_file()
            elif choice == 2:
                self.showing_json_data()
            elif choice == 3:
                self.add_person()
            elif choice == 4:
                # remove
                pass
            elif choice == 5:
                self.find_person_menu()
            elif choice == 6:
                self.save_json_list()
            elif choice == 7:
                self.load_json_list()
            else:
                error_msg(self.invalid_choice)
