class Person:
    def __init__(self,username,firstname,lastname,email=None,telephonenumber=None,adress=None):
        self.username=username
        self.firstname=firstname
        self.lastname=lastname
        if email!=None:
            self.email=email
        if telephonenumber!=None:
            self.telephonenumber=telephonenumber
        if adress!=None:
            self.adress=adress
            
    def add_telephonenumber(self,number):
        self.telephonenumber=number
        
    def add_adress(self,adress):
        self.adress=adress
    
    def is_telephonenumber(self):
        try:
            self.telephonenumber
            return True
        except NameError:
            return False
        
    def is_adress(self):
        try:
            self.adress
            return True
        except NameError:
            return False
        
    #static functions
    @staticmethod
    def change_keylist(keylist):
        ckeys={"Användarnamn":"username","Förnamn":"firstname","Efternamn":"lastname","epost":"email"}
        for i in range(len(keylist)):
            if keylist[i] in ckeys.keys():
                keylist[i]=ckeys[keylist[i]]
    @staticmethod
    def import_person(dict_imp):
        per=Person(dict_imp["username"],dict_imp["firstname"],dict_imp["lastname"],dict_imp["email"])
        if "telephonenumber" in dict_imp.keys():
            per.add_telephonenumber(dict_imp["telephonenumber"])
        if "adress" in dict_imp.keys():
            per.add_adress(dict_imp["adress"])
        return per
    
    @staticmethod
    def import_person_list(dict_list_imp):
        newplist=[]
        for item in dict_list_imp:
            newplist.append(Person.import_person(item))
        return newplist