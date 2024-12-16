"""Describe a recursive algorithm for finding the maximum element in a se-
quence, S, of n elements. What is your running time and space usage?"""

S_1 = [4, 2, 6, 8, 3, 10, 12, 40, 1, 5]

def find_max(S):
    #base cases:
    if len(S) == 1:
        return S[0]
    
    val = find_max(S[1:])
    if val > S[0]:
        return val
    else:
        return S[0]
    
# the find_max function makes n - 1 slices of n. Thus leading to a O(n^2) time complexity.

# the total space usage of find_max is O(n) (the entire recursion stack proportional to n) + O(n^2) (stack sub-level recurions of sequence S slicing) --> O(n^2)
    

        
       
        
        

        
        

print(find_max(S_1))


