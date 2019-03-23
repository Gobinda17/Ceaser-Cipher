print ("Enter a number: ")

x = int(raw_input())

arm = x
rem = 0
sum = 0

while  x != 0:
    rem = x % 10
    num = rem ** 3
    sum = sum + num
    x = x / 10

if arm == sum:
    print ("The number is armstrong")
else:
    print ("Not a armstrong")
