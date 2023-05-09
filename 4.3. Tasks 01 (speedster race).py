n, k = int(input()), int(input())  # n - Скорость "Зума", k - скорость "Флэша"
if n > k:
    print('NO')
elif n < k:
    print('YES')
else:
    print("Don't know")