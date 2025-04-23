a = 'abcdefg.txt'          
b = 'ABCDEFG.txt'    


with open(a, 'r', encoding='utf-8') as src:
    content = src.read()


c = content.upper()


with open(b, 'w', encoding='utf-8') as dest:
    dest.write(c)

print(f"Contents copied from '{a}' to '{b}' with lowercase converted to uppercase.")