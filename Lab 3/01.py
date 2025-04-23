def count_vowels(str):
    count = 0
    i=0
    vowels = ["a","e","i","o","u","A","E","I","O","U"]
    while i<len(str):
        if str[i] in vowels:
            count += 1
        i += 1
    return count

str = input("Enter a string: ")
print(count_vowels(str))