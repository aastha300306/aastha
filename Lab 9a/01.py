def primefac(n,l):
    for i in (2,n+1):
        if (n%i==0):
            l.append(i)
            z=n//i
            primefac(z,l)
            break
n=int(input("enter the number"))
l=[]            
primefac(n,l)
print(l)