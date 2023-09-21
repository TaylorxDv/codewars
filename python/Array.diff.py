def array_diff(a, b):
    result = []
    
    if len(b) == 0 :
        return a
    
    for list in a :
        if list not in b :
            result.append(list)
    return result