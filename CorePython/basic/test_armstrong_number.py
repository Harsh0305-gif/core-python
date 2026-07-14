number = 152
n = number
r = 0
sum = 0

while n > 0:  # n = 153, 15, 1, n = 0 (false)
    r = n % 10  # r = 3, 5, 1
    sum = sum + (r * r * r)  # sum = 27, 152, 153
    n = n // 10  # n = 15, 1, 0

if number == sum:
    print('armstrong number')
else:
    print('not armstrong number')
