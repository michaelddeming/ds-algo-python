"""In similar spirit to the previous problem, augment the Sequence class with method __lt__ , to support lexicographic comparison seq1 < seq2."""

def __lt__(self, other):
    
    # self = 10
    # other = 100
                    #take min   #2      #3
    for index in range(min(len(self), len(other))):        
                    # range(0,3)
        if self[index] < other[index]:
            return True
        elif self[index] > other[index]:
            return False

    return len(self) < len(other)



