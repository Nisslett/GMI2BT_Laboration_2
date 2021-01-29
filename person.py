
class Person:
    def __init__(self, username, firstname, lastname, email, telephonenumber=None, adress=None):
        self.username = username
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        if telephonenumber != None:
            self.telephonenumber = telephonenumber
        if adress != None:
            self.adress = adress

    def add_telephonenumber(self, number):
        self.telephonenumber = number

    def add_adress(self, adress):
        self.adress = adress

    def has_telephonenumber(self):
        try:
            self.telephonenumber
            return True
        except AttributeError:
            return False

    def has_adress(self):
        try:
            self.adress
            return True
        except AttributeError:
            return False

    def to_dict(self):
        dict_entry = {"username": self.username, "firstname": self.firstname,
                      "lastname": self.lastname, "email": self.email}
        if self.has_telephonenumber():
            dict_entry["telephonenumber"] = self.telephonenumber
        if self.has_adress():
            dict_entry["adress"] = self.adress
        return dict_entry

    @staticmethod
    def get_keylist():
        return ["username", "firstname", "lastname", "email", "telephonenumber", "adress"]

    # static functions
    @staticmethod
    def change_keylist(keylist):
        ckeys = {"Användarnamn": "username", "Förnamn": "firstname",
                 "Efternamn": "lastname", "epost": "email"}
        for i in range(len(keylist)):
            if keylist[i] in ckeys.keys():
                keylist[i] = ckeys[keylist[i]]

    @staticmethod
    def dict_to_person_entry(dict_imp):
        per = Person(dict_imp["username"], dict_imp["firstname"],
                     dict_imp["lastname"], dict_imp["email"])
        if "telephonenumber" in dict_imp.keys():
            per.add_telephonenumber(dict_imp["telephonenumber"])
        if "adress" in dict_imp.keys():
            per.add_adress(dict_imp["adress"])
        return per

    @staticmethod
    def dict_to_person_list(dict_list_imp):
        newplist = []
        for item in dict_list_imp:
            newplist.append(Person.dict_to_person_entry(item))
        return newplist

    @staticmethod
    def person_to_dict_list(person_list):
        newlist = []
        for person in person_list:
            newlist.append(person.to_dict())
        return newlist
