students = [
        {'name': 'Rezso', 'age': 9.5, 'candies': 2},
        {'name': 'Gerzson', 'age': 10, 'candies': 1},
        {'name': 'Aurel', 'age': 7, 'candies': 3},
        {'name': 'Zsombor', 'age': 12, 'candies': 5},
        {'name': 'Olaf', 'age': 12, 'candies': 7},
        {'name': 'Teodor', 'age': 3, 'candies': 2}]

def lowcandies(input):
    supcandies = 4
    morecandies = 0
    for x in input:
        if x['candies'] > supcandies:
            morecandies = morecandies + 1
    return morecandies

print(lowcandies(students))
