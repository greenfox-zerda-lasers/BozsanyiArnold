def monkey_count(n):
    #your code here
    list1 = []
    while n >=1:
        list1.append(n)
        n -= 1
    return list1
print(monkey_count(5))
