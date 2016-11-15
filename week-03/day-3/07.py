list1 = [1, 2, 3]
def doubling(list):
    newlist = []
    for x in list:
        newlist.append(x *2)
    return newlist

a = doubling(list1)
print(a)
print(list1)
