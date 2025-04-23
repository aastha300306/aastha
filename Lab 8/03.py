st=set()
for i in range(0,5):
    n=input("enter name")
    st.add(n)
print(st)
lt=list(st)
lt[2]="ajay"
st=set(lt)
print(st)
st.pop()
st.pop()
print(st)