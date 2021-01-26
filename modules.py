
def get_class_list(filename="labb2-personer.csv",path="./"):
    filelist=[]
    path+=filename
    with open(path,"r",encoding="utf-8-sig") as fcsv:
        for line in fcsv:
            tmp_line=line.strip("\n").split(";")
            filelist.append({"förnamn":tmp_line[1],"efternamn":tmp_line[2],"email":tmp_line[3]})
    return filelist

