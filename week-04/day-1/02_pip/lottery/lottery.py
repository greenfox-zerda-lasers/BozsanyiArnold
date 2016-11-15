# Create a method that returns the five most frequent lottery number in a pretty table format
from collections import Counter
from prettytable import PrettyTable
def five_most_frequent(file_name):
    f = open(file_name)
    lines = f.readlines()
    f.close()
    frequent = []
    numbers = []
    for line in lines:
        numbers += line.rstrip().split(';')[-5:]
    count = Counter(numbers)
    most_common = count.most_common()
    i = 0
    while i < 5:
        frequent.append(most_common[i])
        i += 1
    table = PrettyTable(['number', 'frequency'])
    i = 0
    while i < 5:
        table.add_row(frequent[i])
        i += 1
    return table


print(five_most_frequent('otos.csv'))
