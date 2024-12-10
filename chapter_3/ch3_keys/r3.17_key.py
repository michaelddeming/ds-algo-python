"""Show that (n + 1)^5 is O(n^5)."""

# (a + b)^5 = a^5 + 5a^4 b + 10a^3 b^2 + 10a^2 b^3 + 5a^1 b^4 + b^5 --> use as template to expand the polynomial

# (n + 1)^5 = n^5 + 5n^4 + 10n^3 + 10n^2 + 5n + 1

# (n + 1)^5 ~ n^5 -->  for LARGE values of N

# log((n+1)^5) ~ log(n^5) -->  for LARGE values of N

# 5 * log(n+1) ~ 5 * log(n)

# log(n+1) ~ log(n)

# This is valid. For large n, the difference between  \log(n+1)  and  \log(n)  becomes negligible, and they are asymptotically equivalent.

# This is valid. For large n, the difference between  \log(n+1)  and  \log(n)  becomes negligible, and they are asymptotically equivalent.








 