a = input("Enter a string: ")
count = 0
for i in a:
    if i.isalpha():
        count += 1
digit = 0
for i in a:
    if i.isdigit():
        digit += 1
print("Number of alphabet are: ",count)
print("Number of digits are: ",digit)