def disemvowel(string_):
    string_f = ""
    vowles = ['a', 'e', 'i', 'o', 'u','A','E','I','O','U']
    for i in string_ :
        if i in vowles :
            continue    
        string_f += i
    return string_f