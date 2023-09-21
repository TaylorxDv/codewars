def solution(text, ending):
    i = 0
    j = -1
    d = -1
    if len(text) < len(ending):
        return False
    while i < len(ending) :
        if ending[j] == text[d] :
            j -= 1
            d -= 1
            i += 1
        else :
            return False
        
    return True