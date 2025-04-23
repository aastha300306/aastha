l=[(1,2,3),(),('hello','hi'),("dude"),()]
l1=[]
for i in l :
    if not i :
         continue
    else:
        l1.append(i) 

print(l1)