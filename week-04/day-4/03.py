
# 3. Given a non-negative int n,
# return the sum of its digits recursively (no loops).
# Note that mod (%) by 10 yields the rightmost digit (126 % 10 is 6),
# while divide (/) by 10 removes the rightmost digit (126 / 10 is 12).

def summer(n):
    if isinstance(n,int) and n % n == 0 and n > 0:
        if n < 10:
            return n
        else:
            return (n % 10) + summer(n // 10)
    else:
        return ('Please insert a number which is not negative and not equial to zero.')
print (summer(256))
