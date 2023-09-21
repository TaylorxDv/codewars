import math
def is_square(n):    
    if n < 0 :
        return False
    root =  math.isqrt(n)
    if root * root == n :
        return True
    else :
        return False