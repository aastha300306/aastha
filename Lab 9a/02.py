l=[]
def binary(n,l):
   if(n>1): 
     if n%2==0:
         l.append(0)
         binary(n/2,l)
     else:
         l.append(1)
         binary((n-1)/2,l)
   elif(n==1):
      l.append(1)
           
n=int(input("enter the number"))
binary(n,l)
print(l[::-1])