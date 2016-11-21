def divider(user_num):
    try:
        return 10/user_num
    except ZeroDivisionError:
        print ('zacskós tej')
print(divider(0))
