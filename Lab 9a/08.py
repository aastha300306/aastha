def recursive_length(s):
    if s == "":
        return 0
    return 1 + recursive_length(s[1:])
string = "hello"
print("The length of the string ",string," is:", recursive_length(string))