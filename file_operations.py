from common import error_msg
from person import Person

class Json:
    pass


class CSVfile:
    def __init__(self,filename,path="./",encodeing="utf-8-sig"):
        self.filename=filename
        self.path=path
        self.encodeing=encodeing
    
    def get_fullpath(self):
        return self.path + self.filename
    
    def open(self,mode="r"):
        try:
            return open(self.get_fullpath(),mode,encoding=self.encodeing)
        except FileNotFoundError:
            error_msg(f"File [{self.get_fullpath}] was not found!")
            return None
            
def export_dict_list():
    file=CSVfile("labb2-personer.csv")
    csvfile=file.open()
    if csvfile==None:
        error_msg("Could not open file")
        return
    keys=csvfile.readline().rstrip("\n").split(";")
    Person.change_keylist(keys)
    newlist=[]
    for line in csvfile:
        tmp_element_list=line.rstrip("\n").split(";")
        new_dict={}
        for i in range(len(keys)):
            new_dict[keys[i]]=tmp_element_list[i]
        newlist.append(new_dict)
    return newlist
            
            

    