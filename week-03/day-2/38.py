numbers = [7, 5, 8, -1, 2]

def minimum(input):
    min = input[0]
    for x in input:
        if x < min :
            min = x
    return min

print(minimum(numbers))
