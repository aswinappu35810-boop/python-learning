def shortestWordInSentence(sentence):
    texts = sentence.split(" ")
    min = texts[0]
    for i in range(1, len(texts)):
        if len(texts[i]) < len(min):
            min = texts[i]
    return min
    
