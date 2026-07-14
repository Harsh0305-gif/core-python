number = 152
n = number
r = 0
sum = 0

while n > 0:  # n = 151, 15, 1y
    r = n % 10  # r = 1, 5, 1
    sum = (sum * 10) + r  # sum = 1, 15, 151
    n = n // 10  # n = 15, 1, 0

if number == sum:
    print('palindrome number:', sum)
else:
    print('not palindrome number:', sum)
