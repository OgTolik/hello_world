a = int(input())
b = int(input())
c = int(input())

if  c > a > b or b > a > c:
    print(a)
elif a > b > c or c > b > a:
    print(b)
elif b > c > a or a > c > b:
    print(c)