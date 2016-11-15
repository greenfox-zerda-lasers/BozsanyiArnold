# 9. Given a string, compute recursively a new string where all the
# adjacent chars are now separated by a "*".
stringie='Xuxule'
def changer(string):
    if len(string) ==1:
        return string
    else:
        return string[0] + '*' + changer(string[1:])
print(changer(stringie))
