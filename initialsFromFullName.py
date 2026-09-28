def initialsFromFullName(fullName):
    name = fullName.split(" ")
    result = ""
    for i in name:
        # result = name[i][0] + "."
        result = result + i[0].upper()+"."
        
    return result