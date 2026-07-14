# number = 1524
# n = number
# r = 0
# sum = 0
#
# while n > 0:  # n = 152, 15, 1, n = 0 (false)
#     r = n % 10  # r = 2, 5, 1
#     sum = (sum * 10) + r  # sum = 2, 25, 251
#     n = n // 10  # n = 15, 1, 0
# print('reverse number:', sum)

#numbers = 987
# n = numbers
# r =0
# sum =0
#
# while n > 0:
#     r =n%10
#     sum= (sum * 10)+r
#     n= n//10
#     print ('reverse number',sum)
number = 775
n= number
r =0
sum = 0

while n>0:
    r = n%10
    sum =(sum *10) + r
    n = n//10
    print('reverse number',sum)
