with open('2018/Day5/input2.txt', 'r') as f:
    lines = f.readlines()

line = lines[0].strip()
result = ['']

for c in line:
    if c == result[-1].swapcase():
        result.pop()
    else:
        result.append(c)

print(len(''.join(result)))