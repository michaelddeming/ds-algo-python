"""What is the sum of all the even numbers from 0 to 2n, for any positive
integer n?"""

# i = 0 sum --> 2n f(i) = f(i) + f(i+1).... f(2n)

# S =  0 +   2  +   4  + ... + 2n
# S = 2n + 2n-2 + 2n-4 + ... + 0

# 2*S = (0+2n) + (2+(2n-2)) + (4+(2n-4)) + ... + (2n+0)

# 2*S =  2n + 2n + 2n + ... + 2n

# 2*S = 2n(1 + 1 + 1 + ... + 1)

# 2*S = 2n(n+1)

# S = (2n(n+1)/2)

# S = n(n+1)


def sum_even(n):
    n = int(n)
    print(n*(n + 1))


sum_even(4)
