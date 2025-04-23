def ispangram():
    str1=input('enter the string')
    st=set(str1)
    st1=set("qwertyuiopasdfghjklzxcvbnm")
    if(st1<=st):
        print('it is pangram')
    else:
        print('it is not pangram')
ispangram()