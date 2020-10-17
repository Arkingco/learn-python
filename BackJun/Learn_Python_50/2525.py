a, b = map(int, input().split())
c = int(input())
sixten_minitues = 60

sum = b+c
bnanu = sum//sixten_minitues
a = a + bnanu
b = sum % sixten_minitues
if a >= 24:
    a = a % 24
print(a, b)
