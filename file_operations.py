from common import error_msg
from person import Person
import json


class Basefile:
    def __init__(self, filename, path="./", encodeing="utf-8"):
        self.filename = filename
        self.path = path
        self.encodeing = encodeing
        self.fp = None

    def get_fullpath(self):
        return self.path + self.filename

    def open(self, mode="r"):
        try:
            self.fp = open(self.get_fullpath(), mode, encoding=self.encodeing)
            return True
        except FileNotFoundError:
            error_msg(f"File [{self.get_fullpath}] was not found!")
        except FileExistsError:
            error_msg(f"File [{self.get_fullpath}] did not exist!")
        except IOError:
            error_msg(f"File [{self.get_fullpath}] could be opened!")
        self.fp = None
        return False

    def close(self):
        if not self.fp == None:
            self.fp.close()


class CSVfile(Basefile):
    def load_dict_list(self):

        if not self.open():
            return
        keys = self.fp.readline().rstrip("\n").split(";")
        Person.change_keylist(keys)
        newlist = []
        for line in self.fp:
            tmp_element_list = line.rstrip("\n").split(";")
            new_dict = {}
            for i in range(len(keys)):
                new_dict[keys[i]] = tmp_element_list[i]
            newlist.append(new_dict)
        self.close()
        return newlist


class Jsonfile(Basefile):
    def save_to_json(self, plist):
        self.open(mode="w")
        json.dump(plist, self.fp, indent=4)
        self.close()

    def load_from_json(self):
        if not self.open():
            return
        newlist = json.loads(self.fp.read())
        self.close()
        return newlist
