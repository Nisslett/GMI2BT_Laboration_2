def error_msg(error_text):
    print("\033[0;31;40m"+error_text+"\033[0;37;40m")

def input_int(input_text,error_text="Input not an integer! Try again!"):
    while True:
        try:
            value=int(input(input_text))
        except ValueError:
            error_msg(error_text)
            continue
        return value

def press_any_key(pak_text="Press any key to continue . . ."):
    input(pak_text)

def is_empty(list):
    if len(list)==0:
        return True
    else:
        return False
