def marks(math, phy, chem):
    total = int(math + phy + chem)
    average = (total)/3 
    
    if(100>=math>=80):
        print("O")
    elif(79>=math>=70):
        print("A+")
    elif(69>=math>=60):
        print("A")
    elif(59>=math>=55):
        print("B+")
    elif(54>=math>=50):
        print("B")
    elif(49>=math>=45):
        print("C")
    elif(44>=math>=40):
        print("P")
    elif(0>=math>=39):
        print("F")

    if(100>=phy>=80):
        print("O")
    elif(79>=phy>=70):
        print("A+")
    elif(69>=phy>=60):
        print("A")
    elif(59>=phy>=55):
        print("B+")
    elif(54>=phy>=50):
        print("B")
    elif(49>=phy>=45):
        print("C")
    elif(44>=phy>=40):
        print("P")
    elif(0>=phy>=39):
        print("F")

    if(100>=chem>=80):
        print("O")
    elif(79>=chem>=70):
        print("A+")
    elif(69>=chem>=60):
        print("A")
    elif(59>=chem>=55):
        print("B+")
    elif(54>=chem>=50):
        print("B")
    elif(49>=chem>=45):
        print("C")
    elif(44>=chem>=40):
        print("P")
    elif(0>=chem>=39):
        print("F")

math = int(input("Enter marks: " ))
phy = int(input("Enter marks: " ))
chem = int(input("Enter marks: " ))
marks(math, phy, chem)