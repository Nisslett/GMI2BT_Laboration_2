def error_msg(error_text):
    print(error_text)

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