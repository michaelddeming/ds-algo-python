"""Python allows negative integers to be used as indices into a sequence,
such as a string. If string s has length n, and expression s[k] is used for index −n ≤ k < 0, what is the equivalent index j ≥ 0 such that s[j] references
the same element?"""

s = "michael" #index up to -7
# -7 + 7 = 0
# -k + n = j
# j = -k + n
# given a negative index, s[-k], add length of s, n -> positive index s[j], where s[-k] = s[j]
print(s[-7])
print(s[0])
