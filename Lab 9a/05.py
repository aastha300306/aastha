def power(a,b):
    return 1 if b==0 else a*power(a,b-1)
a=int(input("enter the number"))
b=int(input("enter the number"))
print(power(a,b))