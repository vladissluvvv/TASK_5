n = int(input())
a = 0
b = 1
for i in range(n):
    x = a + b
    a = b
    b = x
    print(a, end = ' ')
