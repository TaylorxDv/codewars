def series_sum(n):
    lst = []
    for n in range(1,3*n-1,3):
        lst.append(1/n)
    return '{:.2f}'.format(sum(lst))
