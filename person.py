
class Person:
    def __init__(self, username, firstname, lastname, email, telephonenumber=None, address=None):
        self.username = username
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        if telephonenumber != None:
            self.telephonenumber = telephonenumber
        if address != None:
            self.address = address

    def add_telephonenumber(self, number):
        self.telephonenumber = number

    def add_address(self, address):
        self.address = address

    def has_telephonenumber(self):
        try:
            self.telephonenumber
            return True
        except AttributeError:
            return False

    def has_address(self):
        try:
            self.address
            return True
        except AttributeError:
            return False

    def to_dict(self):
        dict_entry = {"username": self.username, "firstname": self.firstname,
                      "lastname": self.lastname, "email": self.email}
        if self.has_telephonenumber():
            dict_entry["telephonenumber"] = self.telephonenumber
        if self.has_address():
            dict_entry["address"] = self.address
        return dict_entry

    def get_current_keylist(self):
        tmp_list = ["username", "firstname", "lastname", "email"]
        if self.has_telephonenumber():
            tmp_list.append("telephonenumber")
        if self.has_address():
            tmp_list.append("address")
        return tmp_list

    # static functions
    @staticmethod
    def get_keylist():
        return ["username", "firstname", "lastname", "email", "telephonenumber", "address"]

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
        if "address" in dict_imp.keys():
            per.add_address(dict_imp["address"])
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
