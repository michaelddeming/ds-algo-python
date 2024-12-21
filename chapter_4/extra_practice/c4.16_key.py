"""Write a short recursive Python function that takes a character string s and
outputs its reverse. For example, the reverse of pots&pans would be
snap&stop."""

def reverse(s: str) -> str:

    n = len(s)

    if n == 1:
        return s
    else:
       return reverse(s[1:]) + s[-n]

print(reverse("abc"))