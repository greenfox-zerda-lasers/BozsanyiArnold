def triangle(num):
    space = num
    space2 = num *2
    for x in range(0,num):
        x += 1
        space -= 1
        space2 -= 1
        print(        ((space*" ") + (x*'*') + ((x-1)*'*')) + '     '+ ((space2*" ") + (x*'*') + ((x-1)*'*'))        )
stars = 10
gizda = 10
print(triangle(stars))
