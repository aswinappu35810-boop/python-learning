def averageWordLength(sentence):
    total = 0
    words = sentence.split()
    
    for i in words:
        total += len(i)
        
    return total / len(words)
