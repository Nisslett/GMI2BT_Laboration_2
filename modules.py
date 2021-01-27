from common import error_msg as erm
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
        erm(f"Something went wrong when reading from [{path}]")
    return filelist

def save_json_list(list,filename,path="./"):
    try:
        with open(path+filename,"w",encoding="utf-8") as jsonfile:
            json.dump(list,jsonfile)
    except:
        erm(f"Something went wrong when reading from [{path}]")
        return False
    return True