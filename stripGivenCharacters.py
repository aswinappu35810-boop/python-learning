def stripGivenCharacters(text, chars):
    result = ""
    for i in text:
        found = False
        for j in chars:
            if i == j:
                found = True
        if found == False:
            result += i
            
    return result    
            
