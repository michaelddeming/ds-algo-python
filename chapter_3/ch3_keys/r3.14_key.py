"""Show that O(max{f(n),g(n)}) = O(f(n) + g(n))."""

# max{f(n),g(n)} <= c_1 * (f(n) + g(n))

# if f(n) >= g(n) --> max{f(n),g(n)} = f(n) 
#      10 >= 5    --> max{f(n),g(n)} = 10

    # f(n) <= c_1 * (f(n) + g(n))
    # 10 <= c_1 * (10+5) --> true

# if g(n) >= f(n) --> max{f(n),g(n)} = g(n)
#      30 >= 7    --> max{f(n),g(n)} = 30

    # g(n) <= c_1 * (f(n) + g(n)) 
    # # 30 <= c_1 * (30+7) --> true



