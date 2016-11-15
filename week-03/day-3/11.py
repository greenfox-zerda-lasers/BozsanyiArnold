def triangle(num):
    space = num
    for x in range(0,num):
        x += 1
        space -= 1
        print((space*" ") + (x*'*') + ((x-1)*'*'))
    for x in range(num,0,-1):
        x -= 1
        space += 1
        print((space*" ") + (x*'*') + ((x-1)*'*'))
stars = 10
gizda = 10
print(triangle(stars))
