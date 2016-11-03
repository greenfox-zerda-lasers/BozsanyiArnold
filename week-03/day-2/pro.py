ourlist = [4,5,6]

def searchlin(input , number):
    for index, value in enumerate(input):
        if value == number:
            return index
    return -1

print(searchlin(ourlist, 6))


firstlist = [4,5,6]
secondlist = [1,2,3]

def uniting(input1 , input2):
    unitedlist = input1
    for x in input2:
        if x not in input1:
            unitedlist = unitedlist + [x]
    return unitedlist

print(uniting(firstlist , secondlist))

bublelist = [3,9,4,5,2,1]

def bublesort(input):
    for i in range(len(input)):
        for index in range(1 , len(input)):
            if input[index-1] > input[index]:
                a = input[index]
                input[index] = input[index-1]
                input[index-1] = a
    return input

print(bublesort(bublelist))


binarylist1 = [4, 5, 6]
binarylist2 = [4, 5, 7]
binarylist3 = [9, 8 ,6, 7, 3, 5, 4, 2, 1]


def issorted(input):
    sorted = True
    for index in range(1, len(input)):
        if input[index-1] > input[index]:
            sorted = False
    return sorted


def binarysearch(input, number):
    if issorted(input) == False:
        input = bublesort(input)
        return True
    first = 0
    last = len(input)- 1
    found = False
    while first <= last and not found:
        mid = (first + last) //2
        if input[mid] == number:
            found = True
        else:
            if number < input[mid]:
                last = mid-1
            else:
                first = mid+1
    return found


print(binarysearch(binarylist3, 6))
