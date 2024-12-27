"""Implement a function with signature transfer(S, T) that transfers all elements from stack S onto stack T, so that the element that starts at the top
of S is the first to be inserted onto T, and the element at the bottom of S
ends up at the top of T."""

S_1 = [1,2,3,4,5]

T_1 = []



def transfer(S, T):

    while S:
    
        T.append(S.pop())

    return T

print(transfer(S_1, T_1))