names = ['Zakarias', 'Hans', 'Otto', 'Ole']

def shortie(input):
        shortest = input[0]
        for x in input:
            if len(x) < len(shortest):
                shortest = x
        return shortest

print(shortie(names))
