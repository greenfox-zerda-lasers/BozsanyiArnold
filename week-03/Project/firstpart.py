def reverser(string):
        revers = ''
        i = 0
        while i < len(string):
            revers += string[(len(string)-1)-i]
            i += 1
        return revers

def crtpalindrome(string):
    palindrome = string + reverser(string)
    return palindrome

print(crtpalindrome('paer'))

def if_palindrome(string):
    
