"""Write a short recursive Python function that rearranges a sequence of in-
teger values so that all the even values appear before all the odd values."""

S_1 = [2,7,9,6,5,3,7,8,4,5,3,2,3]

def sort_ints(S):

    n = len(S)

    if n <= 1:
       return S
    else:
        if S[0] % 2 == 0:
            return [S[0]] + sort_ints(S[1:])
        else:
           return sort_ints(S[1:]) + [(S[0])]
        
  
    
print(sort_ints(S_1)) 

        
        
    
    


