"""Implement a function that reverses a list of elements by pushing them onto a stack in one order, and writing them back to the list in reversed order."""


l_1 = [1,2,3,4,5]

def rev_list(l):

    S_1 = []
    S_2 = []

    while l:
        S_1.append(l.pop())
    
    while S_1:
        S_2.append(S_1.pop())
    
    while S_2:
        l.append(S_2.pop())
    return l


print(rev_list(l_1))


    
