a = int(input("Enter 1st number : "))
b = int(input("Enter 2nd number : "))
c = int(input("Enter 3rd number : "))

largest = a

if(largest < b and c<b):
    print("largest : ",b)
elif(largest < c and b<c):
    print("largest : ",c)
elif(largest == b and b==c):
    print("all are equal")
elif(largest == b):
    print("largest : ",largest)
elif(largest == c):
    print("largest : ",largest)
elif(b==c and largest < b):
    print("largest : ",b)
else:
    print("largest :",largest)