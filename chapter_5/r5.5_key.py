"""Redo the justification of Proposition 5.1 assuming that the the cost of
growing the array from size k to size 2k is 3k cyber-dollars. How much
should each append operation be charged to make the amortization work?"""

# 4 cyber dollars --> 1 cyber dollar for the O(1) append, w/ 3 cyber dollars extra per "cell" in the array to cover the future cost of increasing from k "cells" to 2k "cells" (doubling the array size).

