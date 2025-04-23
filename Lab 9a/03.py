st=input("enter the string ")
count=1
v=['a','e','i','o','u']
def check(st,count):
    if len(st)==0:
        return 0
    else:
        if st[0].lower() in v:
            count=count+1
            return 1 + check(st[1:],count) 

    return check(st[1:],count)          
print(check(st,count))