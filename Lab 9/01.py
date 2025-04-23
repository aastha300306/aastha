str1=input("enter the string")
def count_lower_upper():
    low=0
    upp=0
    for i in str1:
        if(i.isupper()):
            upp=upp+1
        else:
            low=low+1
    print("total upper:",upp,"total low:",low)
count_lower_upper()