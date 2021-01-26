import modules

def input_int(input_text,error_text="Input not an integer! Try again!"):
    while True:
        try:
            value=int(input(input_text))
        except ValueError:
            print(error_text)
            continue
        print("value="+str(value))
        return value
        

def menu():
    while True:
        print("\nLaboration 2 - GMI2BT - Nils Broberg")
        #menu text
        print("1. Läs in orginal (labb2-person.csv)\n2. Visa json-data\n3. Lätt till person\n4. Ta bort person\n5. Spara fil (json)\n6. Avsluta\n")
        choice=input_int("Please type in your choice:","Invalid choice! Try again!")
        if choice==1:
            pass
        elif choice==2:
            pass
        elif choice==3:
            pass
        elif choice==4:
            pass
        elif choice==5:
            pass
        elif choice==6:
            break