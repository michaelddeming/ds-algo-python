"""The collections.Sequence abstract base class does not provide support for comparing two sequences to each other. Modify our Sequence class from
Code Fragment 2.14 to include a definition for the eq method, so
that expression seq1 == seq2 will return True precisely when the two
sequences are element by element equivalent."""

def __eq__(self, other):
   
    if len(self) != len(other):
        return False
    
    
    for index in range(self):
        if self[index] != other[index]:
            return False
    return True

            
    




        

    

    
    



