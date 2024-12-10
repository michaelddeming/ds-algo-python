"""Show that if p(n) is a polynomial in n, then log p(n) is O(logn)."""

# p(n) = a_0 + a_1*n + a_2*n^2 + a_3*n^3 + ... + a_d*n^d

# log_2(p(n)) = log_2(a_0 + a_1*n + a_2*n^2 + a_3*n^3 + ... + a_d*n^d)

# log_2(p(n)) ~ log_2(a_d*n^d) --> for LARGE n values we can assume that the above polynomial

# log_2(a_d*n^d) ~ log_2(a_d) + log_2(n^d) --> simplify the logs

# log_2(a_d*n^d) ~ log_2(a_d) + d * log_2(n)

# log_2((p)) = O(log_2(n))
