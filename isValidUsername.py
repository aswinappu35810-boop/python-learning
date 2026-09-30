def isValidUsername(name):
    if len(name)<4:
        return False
    for i in range(0, len(name)):
        
        if name[i].islower() or name[i].isdigit() or name[i]=="_":
            return True 
        else:
            return False
            
        
                      
