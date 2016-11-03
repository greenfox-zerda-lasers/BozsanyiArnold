
numbers = [3, 4, 5, 6, 7]

def evening(input):
    even = []
    for x in input:
        if x % 2 == 0:
            even.append(x)
    print(even)
evening(numbers)
