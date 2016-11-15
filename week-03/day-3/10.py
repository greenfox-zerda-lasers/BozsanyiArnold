
def triangle(num):
    space = num
    for x in range(0,num):
        x += 1
        space -= 1
        print((space*" ") + (x*'*') + ((x-1)*'*'))
stars = 6
print(triangle(stars))
