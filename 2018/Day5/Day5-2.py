with open('2018/Day5/input2.txt', 'r') as f:
    lines = f.readlines()

line = lines[0].strip()
result = ['']

# Part 2
min_length = float('inf')
for c in set(line.lower()):
    modified_line = line.replace(c, '').replace(c.upper(), '')
    modified_result = ['']
    for char in modified_line:
        if char == modified_result[-1].swapcase():
            modified_result.pop()
        else:
            modified_result.append(char)
    min_length = min(min_length, len(''.join(modified_result)))

print(min_length)
