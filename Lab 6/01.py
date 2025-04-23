l=[('dirdhit','ashit','Devang'),'ragi','aashna','Darshini',('darshil',)]
boy=0
girl=0
for i in l :
    if(isinstance(i,tuple)):
        for j in i :
            boy=boy+1
    else:
        girl=girl+1

print("total no. of girls is ",girl)
print("total no. of boys is ",boy)