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
        print(f"1. Read in [{filecsv}]\n2. Show json-data\n3. Add person\n4. Remove person\n5. Save to json\n6. Exit\n")
        choice=input_int("Please type in your choice:","Invalid choice! Try again!")
        if choice==1:
            person_csv_list=read_from_file(filecsv)
        elif choice==2:
            pass
        elif choice==3:
            pass
        elif choice==4:
            pass
        elif choice==5:
            save_list(person_csv_list,filejson)
        elif choice==6:
            break