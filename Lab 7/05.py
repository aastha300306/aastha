d1={'a':50,'b':20 ,'c':45}
d2={'a':10,'b':5,'c':15}
l=[]
for i in d1:
    j=d1[i]*d2[i]
    l.append(j)
    
print("total bill is ",sum(l))