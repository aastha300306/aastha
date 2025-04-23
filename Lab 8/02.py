import random
ct=0
st=set()
j=0
while j<10:
       i=random.randrange(15,46)
       st.add(i)
       j=j+1 
print(st)
for k in st:
    if(k<30):
        ct=ct+1        
for l in st.copy():        
    if(l>35):
        st.discard(l)
print(st)
print("count of number less then 30 is:",ct)