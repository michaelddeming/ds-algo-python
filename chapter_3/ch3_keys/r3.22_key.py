"""Show that ⌈f(n)⌉ is O(f(n)), if f(n) is a positive nondecreasing function that is always greater than 1."""

# f(n) > 1

# ⌈f(n)⌉ <= c_1 * f(n)

# f(n) <= ⌈f(n)⌉ < f(n) + 1

# divide by f(n)

# 1 <= ⌈f(n)⌉ / f(n) < 1 + (1/f(n)) 

# mulitply f(n) out of the denominator 

# f(n) <= ⌈f(n)⌉ < f(n) * (1 + (1/f(n)))

# simplify right side

# f(n) <= ⌈f(n)⌉ < f(n) + 1

# ⌈f(n)⌉ <= f(n) + 1 --> use in our Big Oh inequality

# f(n) + 1 <= c_1 * f(n)






