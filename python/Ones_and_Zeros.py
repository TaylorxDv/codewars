def binary_array_to_number(arr):
    l = [str(i) for i in arr ]
    return (int(str(''.join(l)),2))