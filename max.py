print ("Enter three numbers: ")

x = int(raw_input())
y = int(raw_input())
z = int(raw_input())

if x > y and x > z:
    print ("Greater number is", x)
elif y > z:
    print ("Greater number is", y)
else:
    print ("Greater number is", z)
