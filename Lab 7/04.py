st=input("enter the string  ")
l1=list(st)
st1=set(l1)
d=dict()
for i in st1:
    d.update({i:l1.count(i)})

print(d)