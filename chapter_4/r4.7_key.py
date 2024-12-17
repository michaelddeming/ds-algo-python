"""Describe a recursive function for converting a string of digits into the in-
teger it represents. For example, "13531" represents the integer 13,531."""

def convert(string):
    n = len(string)


    if n == 1:
        return int(string[0])
    else:                                           #
        return 10**(n-1) * int(string[0]) + convert(string[1:])
    
print(convert("657"))
