from os import error


def error_msg(error_text):
    print("\033[0;31;40m"+error_text+"\033[0;37;40m")


def input_int(input_text, error_text="Input not an integer! Try again!"):
    while True:
        try:
            value = int(input(input_text))
        except ValueError:
            error_msg(error_text)
            continue
        return value


def input_required(text):
    while True:
        input_text = input(text).strip()
        if input_text == "":
            error_msg(
                "This field is required! Empty input is invlaid! Try Again!")
            continue
        return input_text


def press_any_key(pak_text="Press any key to continue . . ."):
    input(pak_text)


def is_empty(list):
    if len(list) == 0:
        return True
    else:
        return False


def prompt_yes_or_no(text):
    while True:
        answer = input(text+" (yes/no):").lower()
        if answer == "yes":
            return True
        elif answer == "no":
            return False
        error_msg("Input must be yes or no! Try again!")
