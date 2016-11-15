def adder(n):
    if n ==1:
        return 1
    else:
        return n + adder(n-1)
print (adder(5))
