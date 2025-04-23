st={'aa','ab','ba','bb'}
s1=set()
s2=set()
for i in st:
    if (i[0]=='a'):
        s1.add(i)
    else:
        s2.add(i)

print(s1)
print(s2)