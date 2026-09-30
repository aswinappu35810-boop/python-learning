def ordinalSuffix(n):
    n = str(n)
    if int(n) >= 10 and int(n)<=20:
        return n + "th"
    if int(n) >= 110 and int(n)<=120:
        return n + "th"

    if n[-1] == "1":
        return n + "st"
    if n[-1] == "2":
        return n + "nd"
    if n[-1] == "3":
        return  n + "rd"
    if int(n[-1])>3:
        return n + "th"