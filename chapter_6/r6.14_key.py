"""Repeat the previous problem using the deque D and an initially empty
stack S."""

from collections import deque

D_1 = [1, 2, 3, 4, 5, 6, 7, 8]


def swap(D):

    D = deque(D)
    S = deque()

    while D[-1] != 5:
        S.append(D.pop()) #S = [8]
        D.appendleft(S.pop())


        # D = [6, 7, 8, 1 ,2, 3, 4, 5]

    while D[-1] != 3:

        S.append(D.pop()) # S = [5, 4]
    D.appendleft(S.pop())
    D.appendleft(S.pop())

    # D = [5, 4, 6, 7, 8, 1, 2, 3]

    while D[-1] != 8:
        S.append(D.pop())
        D.appendleft(S.pop())
    
    return D

print(swap(D_1))


