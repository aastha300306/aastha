for i in range(24):
    if(i==0):
        print("12 Midnight")
    elif(i==12):
        print("12 Noon")
    elif(i<12):
        print(i,"AM")
    elif(i>12):
        print(i,"PM")