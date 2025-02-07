"""Answer the following questions so as to justify Proposition 8.8.
a. What is the minimum number of external nodes for a proper binary
tree with height h? Justify your answer.
b. What is the maximum number of external nodes for a proper binary
tree with height h? Justify your answer.
c. Let T be a proper binary tree with height h and n nodes. Show that:
        log(n+1) - 1 <= h <= (n-1) / 2
d. For which values of n and h can the above lower and upper bounds
on h be attained with equality?
"""

# a. Minimum Number External Nodes: h + 1
# b. Maximum Number External Nodes: 2^h
# c. n = 7, h = 2
# 
# log(7+1) - 1 <= 2 <= (7-1) / 2 --> 2 <= 2 <= 3 --> TRUE
# 
# d.
#   Lower: 2^(h+1) - 1
#   Upper: n = 2h + 1

