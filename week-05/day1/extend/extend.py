# Adds a and b, returns as result
def add(a, b):
    if isinstance(a, int) and isinstance(b, int):
        return a + b
    else:
        raise TypeError('Please insert only numbers.')
# Returns the highest value from the three given params
def max_of_three(a, b, c):
    listofnum =[]
    if isinstance(a, int) and isinstance(b, int) and isinstance(c, int):
        listofnum.append(a)
        listofnum.append(b)
        listofnum.append(c)
        return sorted(listofnum)[-1]
    else:
        raise TypeError('Its not working , if you don\'t give numbers.')

# Returns the median value of a list given as param
def median(pool):
    if isinstance(pool,list) and len(pool) == 0:
        raise ValueError('Please fill that list.')
    elif isinstance(pool, list):
        if len(pool) % 2 == 0:
            return (sorted(pool)[int(len(pool)/2)-1] + sorted(pool)[int(len(pool)/2)]) /2
        elif len(pool) == 1:
            return pool[0]
        else:
            return sorted(pool)[int((len(pool) - 1) / 2)]
    else:
        raise TypeError('Please be kind , and insert a list instead of this crap.')
# Returns true if the param is a vovel
def is_vovel(char):
    if isinstance(char, str) and len(char) == 0:
        raise ValueError('Could you please put a letter? Seriously. Don\'t tell me it\'s beyond your capabilities.')
    elif isinstance(char, str) and len(char) == 1:
        return char.lower() in 'aeiouéáőűöüóí'
    elif isinstance(char, str) and len(char) != 1:
        raise ValueError('Your string is too long mate.')
    else:
        raise TypeError('Use string for god\'s sake.')

# Create a method that translates hungarian into the teve language
def translate(hungarian):
    teve = hungarian
    if isinstance(hungarian, str):
        for char in teve:
            if is_vovel(char):
                teve = (char+'v'+char).join(teve.split(char))
        return teve
    else:
        raise TypeError('Put a string.')
