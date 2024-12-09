"""Show that if d(n) is O(f(n)) and e(n) is O(g(n)), then d(n) - e(n) is not
necessarily O(f(n) - g(n))."""

# d(n) <= c_1 * f(n)

# e(n) <= c_2 * g(n)

# d(n) - e(n) <= c_1 - c_2 * (f(n) - g(n))

# if f(n) and g(n) are relatively close in size, the result of (f(n) - g(n)) would be a small value, and in some cases close to 0 or even 0. That being said, d(n) - e(n) could potentially have a faster growth rate than f(n) - g(n), equation NOT true.



