"""Given an n-element sequence S of integers, Algorithm C executes an
O(n)-time computation for each even number in S, and an O(logn)-time
computation for each odd number in S. What are the best-case and worst-
case running times of Algorithm C?"""


# assuming S has more than 1 integer.

# best case --> if S has only odd numbers, S = 1,3 --> O(nlogn)

# worst case --> if S has multiple even values, S = 2,4,6,8 --> O(n^2)
