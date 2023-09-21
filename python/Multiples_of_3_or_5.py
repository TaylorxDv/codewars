def solution(number):
    sum_f = 0
    if number > 0 :
        i = 1
        while  i < number :
            if i % 3 == 0 or i % 5 == 0:
                sum_f += i
            
            i += 1
    else :
        return 0
    return sum_f
