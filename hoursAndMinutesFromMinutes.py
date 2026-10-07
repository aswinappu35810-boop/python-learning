def hoursAndMinutesFromMinutes(totalMinutes):
    result  = []
    time = totalMinutes//60
    result.append(time) 
    time = totalMinutes%60
    result.append(time)
    return result