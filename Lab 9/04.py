def sum_avg():
    l=[]
    for i in range (0,5):
        n=int(input("enter the marks"))
        l.append(n)
    print(sum(l))
    print(sum(l)/len(l))
sum_avg()