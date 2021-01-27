from common import error_msg
import json

def get_class_list(filename,path="./"):
    filelist=[]
    try:
        with open((path+filename),"r",encoding="utf-8-sig") as fcsv:
            fcsv.readline()
            for line in fcsv:
                tmp_line=line.strip("\n").split(";")
                filelist.append({"firstnamn":tmp_line[1],"lastnamn":tmp_line[2],"email":tmp_line[3]})
    except:
        error_msg(f"Something went wrong when reading from [{path+filename}]")
    return filelist

def save_json_list(list,filename,path="./"):
    try:
        with open(path+filename,"w",encoding="utf-8") as jsonfile:
            json.dump(list,jsonfile, indent=4)
    except:
        error_msg(f"Something went wrong when writeing to [{path+filename}]")
        return False
    return True

def load_json_list(filename,path="./"):
    newlist=[]
    try:
        with open(path+filename,"r",encoding="utf-8") as jsonfile:
            newlist=json.loads(jsonfile.read())
            #newstring=jsonfile.read().replace("[","[\n").replace("{","\t{").replace("},","},\n")
    except:
        error_msg(f"Something went wrong when reading from [{path+filename}]")
    return newlist