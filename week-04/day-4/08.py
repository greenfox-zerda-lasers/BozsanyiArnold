# 8. Given a string, compute recursively a new string where all the 'x' chars have been removed.
stringie='Xuxule'
def changer(string):
    if len(string) == 0:
        return string
    elif string[0] == 'x' or string[0] == 'X':
        return changer(string[1:])
    else:
        return string[0] + changer(string[1:])
print (changer(stringie))
