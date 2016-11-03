students = [
        {'name': 'Rezso', 'age': 9.5, 'candies': 2},
        {'name': 'Gerzson', 'age': 10, 'candies': 1},
        {'name': 'Aurel', 'age': 7, 'candies': 3},
        {'name': 'Zsombor', 'age': 12, 'candies': 5}]

def belowten(input):
    supage = 10
    scandies = 0
    for x in input:
        if x['age'] < supage:
            scandies = scandies + x['candies']
    return scandies

prinqt(belowten(students))
