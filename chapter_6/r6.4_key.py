"""Give a recursive method for removing all the elements from a stack."""

S_1 = [1,2,3,4,5]
print(S_1)

def del_stack(S):

    if  len(S) == 0:
        return 
    S.pop()
    del_stack(S)
        

del_stack(S_1)

print(S_1)

# O(n)

