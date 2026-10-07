def clockToTwelveHour(hour24):
    if hour24 == 0:
        return "12 AM"
    elif hour24 < 12:
        return str(hour24)+" AM"
    elif hour24 == 12:
        return "12 PM"
    else:
        return str(hour24-12)+" PM"
