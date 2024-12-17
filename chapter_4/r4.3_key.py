"""Draw the recursion trace for the computation of power(2,18), using the
repeated squaring algorithm, as implemented in Code Fragment 4.12."""

# power(2,18) --> 512 is received from the deeper recursion (below) as the return value for EACH power(2,18) --> 512 * 512 = 262,144 which is returned to as our final value for 2^18. 
    
    #power(2,9) * power(2,9) --> 16 is received from deeper recursion (below) as the return value for EACH power(2,9). BUT if n % 2 == 1, we multiply this all by x --> 16 * 16 * x --> 16 * 16 * 2 = 512 which is returned to prev recursion
        
        #power(2,4) * power(2,4) --> 4 is received from the deeper recursion (below) as the return value for EACH power(2,4) --> 4 * 4 = 16 which is returned to prev recursion
                
            
            #power(2,2) * power(2,2) --> 2 is received from the deeper recursion (below) as the return value for EACH power(2,2) --> 2 * 2 = 4 which is returned to prev recursion
                
                #power(2,1) * power(2,1) --> 1 is received from deeper recursion (below) as the return value for EACH power(2,1). BUT if n % 2 == 1, we multiply this all by x --> 1 * 1 * x --> 1 * 1 * 2 = 2 which is returned to prev recursion
                    
                    #power(2,0) * power(2,0) --> base case met, returns 1 for EACH function of power(x,n=0) --> 1 * 1 = 1 which is returned to prev recursion