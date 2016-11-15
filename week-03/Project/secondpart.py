def palindrome_check(string):
    n = string[0]               #starting point from where we check equvivalance.
    j = string[n + 3]           #ending point should alwazs expanded by 1.
    candidates = []
    while x in range(0,-1):
        x = string[n:j]               # I would love this to be my candidate variable.
        if n == j and x == reversed(x):
            candidates.append(x)
            if j > -1 :
