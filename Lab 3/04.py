str1 = input("Enter string: ")
str2 = input("Enter string to remove: ")

def remove_string(str1, str2):
    return str1.replace(str2 , "")

print(remove_string(str1, str2))