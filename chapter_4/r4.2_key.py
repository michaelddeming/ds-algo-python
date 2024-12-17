""" Draw the recursion trace for the computation of power(2,5), using the
traditional function implemented in Code Fragment 4.11."""

def power(x, n):
    if n == 0:
        return 1
    else:
        return x * power(x, n - 1)

power(2, 5)

# power(2,5) = 32, not additional math needed on original function call. 32 is return to it. 2^5 = 32. 
    # 2 * power(2,4) --> 2 * 16 = 32, returns 32 in place of the power(2,5) as prev recursion's return value.
        # 2 * power(2,3) --> 2 * 8 = 16, returns 8 in place of power(2,4) as prev recursion's reutrn value.
            # 2 * power(2,2) --> 2 * 4 = 8, returns 8 in place of power (2,3) as prev recursion's return value.
                # 2 * power(2, 1) --> 2 * 2 = 4, returns 4 in place of power(2,2) as prev recursion's return value.
                    # 2 * power(2,0) ---> base case met n = 0, returns 1 for power(2,0), 2 * 1 = 2, 2 is returned as the prev recursion's return value.