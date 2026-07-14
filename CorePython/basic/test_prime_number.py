from itertools import count

number = 18
count = 0

for i in range(2, number):
    if number % i == 0:
        count = count + 1
        break

if count == 0:
    print('prime')
else:
    print('not prime')
