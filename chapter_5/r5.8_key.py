"""Experimentally evaluate the efficiency of the pop method of Python's list
class wihen using varyng indices as a parameter, as we did for insert on
page 205. Report your results akin to Table 5.5."""

from time import time

def time_pop(N: int):

    data = [None] * N

    start_time = time()
    for _ in range(N):
        data.pop(len(data) // 2)
    end_time = time()

    return (end_time - start_time)

print(time_pop(1000000))

#                       100             1000            10000               100000              1_000_000
# k = 0               6.91E-06        9.49E-05         .0068                .6931                 .6975 
# k = n // 2          6.20E-06        .0001            .0038                .0035                 .3472
# k = n               4.05E-06        1.91E-05         .00023               .0023                 .018
