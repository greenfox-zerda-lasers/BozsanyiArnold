ac = 8
time = 120
out = ''
if ac % 4 == 0 and time <= 200:
    out = 'check'
elif time >200:
    out = 'time out'
else:
    out = 'run forest run'
print(out)            
