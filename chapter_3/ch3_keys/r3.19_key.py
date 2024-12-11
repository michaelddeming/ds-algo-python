"""Show that n is O(nlogn)."""

# f(n) <= c_1 * g(n)

# n <= c_1 * nlogn

# divide n on both sides

# 1 <= c_1 * logn

# divide by the costant on both sides

# 1/c_1 <= logn

# need to plug-in sample values to "mimic" a input and constant, using "easy" values for math purposes, we plug in 1 for a constant, and use n=e w

# 1/1 <= log_e(e)

# 1 <= 1 --> True

# proves that for a c_1 > 0 and a n = e that n is O(nlogn)



