"""Isabel has an interesting way of summing up the values in a sequence A of
n integers, where n is a power of two. She creates a new sequence B of half
the size of A and sets B[i] = A[2i] + A[2i+ 1], for i= 0,1,...,(n/2) - 1. If
B has size 1, then she outputs B[0]. Otherwise, she replaces A with B, and
repeats the process. What is the running time of her algorithm?"""

A_1 = [3,6,4,1]

# O(nlogn)

def sum_sequence(A):
    n = len(A)
    m = n // 2

    if m == 1:
        return A[0] + A[1]

    B = [0] * (m)
    for i in range((m)):
        B[i] = A[2*i] + A[2*i+1]
    return sum_sequence(B)

    
    


print(sum_sequence(A_1))