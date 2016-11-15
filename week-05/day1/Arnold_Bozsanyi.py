from collections import Counter
import string


def anagramm(string1,string2):
    firststrletters = []
    secondstrletters = []
    if isinstance(string1, str) and isinstance(string2, str):
        for i in string1:
            if i != ' ':
                firststrletters.append(i)
        for x in string2:
            if x != ' ':
                secondstrletters.append(x)
        if sorted(firststrletters) == sorted(secondstrletters):
            return True
        else:
            return False
    else:
        raise TypeError('Please insert only strings.')
#print(anagramm('alma','lama'))
#print(anagramm('al ma','lama'))
#print(anagramm(123, 321))
def count_letters(word):
    if isinstance(word, str):
        lettersofstring = []
        for i in word:
            if i in string.ascii_letters:
                lettersofstring.append(i)
        return Counter(lettersofstring)
    else:
        raise TypeError('Please insert only strings.')
