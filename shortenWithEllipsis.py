def shortenWithEllipsis(text, limit):
    result = ""
    if len(text)<=limit:
        return text
    for i in range(0,limit):
        result = result + text[i]
        
    return result + "..."
        
