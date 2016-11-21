from collections import Counter
def count_lines(filename):
    try:
        f = open(filename)
        ourfile = f.readlines()
        f.close()
        print(len(ourfile))
    except FileNotFoundError:
        print('zero')    
count_lines('zacskostej2.txt')
