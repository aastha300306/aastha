n = int(input("Enter a number: "))
fact = 1
for i in range(n):
    fact = fact * (i+1)
    i += 1
print(fact)