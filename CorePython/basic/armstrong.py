number = 259
n = number
r = 0
sum = 0

while n>0:
    r = n % 10
    sum = sum + (r*r*r)
    n= n//10
if number == sum:
    print("armstrong")
else:
    print(" not armstrong")