str1 = input("Enter string 1: ")
str2 = input("Enter string 2: ")
def check_string(str1, str2):
    
    if str1 in str2 or str2 in str1:
        print("One string is present in other.")
    else:
        print("Neither string is present in other.")
        
check_string(str1, str2)