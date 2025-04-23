file1 = 'One.txt'
file2 = 'Two.txt'
file3 = 'Three.txt'


with open(file1, 'r', encoding='utf-8') as f1:
    lines1 = f1.readlines()

with open(file2, 'r', encoding='utf-8') as f2:
    lines2 = f2.readlines()


merged_lines = []
max_len = max(len(lines1), len(lines2))

for i in range(max_len):
    if i < len(lines1):
        merged_lines.append(lines1[i].rstrip('\n') + '\n')
    if i < len(lines2):
        merged_lines.append(lines2[i].rstrip('\n') + '\n')


with open(file3, 'w', encoding='utf-8') as out:
    out.writelines(merged_lines)

print(f" Merged content written to '{file3}'.")