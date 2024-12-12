"""For each function f (n) and time t in the following table, determine the
largest size n of a problem P that can be solved in time t if the algorithm
for solving P takes f (n) microseconds (one entry is already completed)."""

# f(n) <= t


#           1 second            1 hour                                   1 month                      1 century
# logn     ~10^(300_000)    ~10^(2.350*10^11)                        ~10^(1_083_600)                10^(9.492*10^14)
# n         1_000_000         3_600_000_000                              2.592*10^12                    3.1536*10^15
# nlogn     10^300006   (~10^(2.350*10^11))(3_600_000_000)     (~10^(1_083_600))(2.592*10^12)    (10^(9.492*10^14))( 3.1536*10^15)
# n^2        1_000_000^2        ( 3_600_000_000)^2                      ( 2.592*10^12)^2                (  3.1536*10^15)^2
# 2^n        2^( 1_000_000 )     2^(3_600_000_000)                     2^( 2.592*10^12  )          2^( 3.1536*10^15)