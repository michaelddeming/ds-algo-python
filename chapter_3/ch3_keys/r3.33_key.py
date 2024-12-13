"""Al and Bob are arguing about their algorithms. Al claims his O(nlogn)-
time method is always faster than Bob's O(n^2)-time method. To settle the
issue, they perform a set of experiments. To Al's dismay, they find that if
n < 100, the O(n^2)-time algorithm runs faster, and only when n ≥ 100 is
the O(nlogn)-time one better. Explain how this is possible."""

# For determining time complexitity of functions/algorithms, we are specifically targeting very large input values, n--> infinity, when defining "Big Oh".

# For n < 100, costants and other lower-order terms can significantly impact run times. If Al has constants or other factors in his algorithm, it may perform slower than Bob's for n < 100.