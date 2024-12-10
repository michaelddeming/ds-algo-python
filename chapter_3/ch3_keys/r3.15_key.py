"""Show that f(n) is O(g(n)) if and only if g(n) is Ω(f(n))."""

# f(n) is O(g(n)) --> f(n) <= c_1 * g(n)

    # f(n) <= c_1 * g(n)
    # (f(n)* (1 / c_1)) <= (c_1 * g(n)) * (1 / c_1) 
    # (f(n)* (1 / c_1)) <= g(n) --> refactor Big Oh definition to reflect Big Omega
    # because we have now inverted c_1 as (1 / c_1) to fit the Big Omega definition we can now say that (1 / c_1) = c2
    # f(n)* c_2 <= g(n) --> satisfies the Big Omega definition
    # Omega(f(n)) = g(n)






# g(n) is Omega(f(n)) --> g(n) >= c_2 * f(n)

    # g(n) >= c_2 * f(n)
    # (g(n) * (1 / c_2)) >= (c_2 * f(n)) * (1 / c_2) 
    # (g(n) * (1 / c_2)) >= f(n) --> refactor Big Omega definition to reflect Big Oh
    # becuase we have now invereted c_2 as (1 / c_2) to fit the Big Oh definition we can now say that (1 / c_2) = c_1
    # g(n) * c_2 >= f(n) --> satisfies the Big Oh definition
    # O(g(n)) = f(n)
    # 


