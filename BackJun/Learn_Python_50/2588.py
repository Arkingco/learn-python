import math

a = int(input())
b = int(input())
UNIT_VALIAVLE = {100, 10, 1}
qwe = list(UNIT_VALIAVLE)
qwe.reverse()
stack = []
stack.append(a*b)
for unit in qwe:
    b_unit = math.floor(b/unit)
    b = b - (b_unit*unit)
    result = round(a*b_unit)
    stack.append(result)

re = range(4)
for i in re:
    print(stack.pop())


