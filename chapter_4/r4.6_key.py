"""Describe a recursive function for computing the nth Harmonic number,
H_n = ∑ni=1 1/i."""

def harmonic(n):
    
    if n == 1:
       return 1
    else:
         return 1 / n + harmonic(n - 1)
    


print(harmonic(3))

    
    

       

    

    