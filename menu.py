import modules
from common import input_int,error_msg,press_any_key

#menu alternative 1
def read_from_file(pfile):
    print(f"Fetching list from file [{pfile}]")
    plist=modules.get_class_list(pfile)
    if len(plist)>0:
        print("The list has been fetched.")
    else:
        print("List is empty.")
    press_any_key()
    return plist

#menu alternative 2
def showing_json_data(jfile):
    print("Showing json data.")
    jsonstr=str(modules.load_json_list(jfile)).replace("[","[\n").replace("{","\t{").replace("},","},\n").replace("}]","}\n]")
    print(jsonstr)
    press_any_key()

#menu alternative 3
def add_person(plist):
    print("Adding a person:")
    firstname=input("Please type in the firstname:")
    lastname=input("Please type in the lastname:")
    email=input("Please type in the email:")
    plist.append({"firstname":firstname,"lastname":lastname,"email":email})
    
def find_person_menu(plist):
    while True:
        print("Search menu. Search for:")
        print("1. firstname\n2. lastname\n3. email\n4. go back to main menu")
        choice=input_int("Please type in your choice:","Invalid choice! Try again!")
        if choice==4:
            break
        if choice<1 or choice>4:
            continue
        key=
        modules.find_person(plist,)
    
#menu alternative 5
def save_list(plist,jfile):
    if len(plist)==0:
        error_msg("Can't save file! List is empty!")
        press_any_key()
        return
    print("Saveing list to file.")
    if modules.save_json_list(plist,jfile):
        print("List saved.")
    else:
        print("Saveing of list failed")
    press_any_key()

def menu():
    filecsv="labb2-personer.csv"
    filejson="person.json"
    person_csv_list=[]
    while True:
        print("\nLaboration 2 - GMI2BT - Nils Broberg")
        #menu text
        print(f"1. Read in [{filecsv}]\n2. Show json-data in [{filejson}]\n3. Add person\n4. Remove person\n5. Save to json\n6. Exit\n")
        choice=input_int("Please type in your choice:","Invalid choice! Try again!")
        if choice==1:
            person_csv_list=read_from_file(filecsv)
        elif choice==2:
            showing_json_data(filejson)
        elif choice==3:
            add_person(person_csv_list)
        elif choice==4:
            pass
        elif choice==5:
            save_list(person_csv_list,filejson)
        elif choice==6:
            break