
last = range(2000)
start = 1
for start in last:
    x = start
    y = start
    isSingleToneValue = (id(x) == id(y))
    print(isSingleToneValue)
    start = start + 1
    
x = 2222
y = 2222
print(id(x) == id(y))
