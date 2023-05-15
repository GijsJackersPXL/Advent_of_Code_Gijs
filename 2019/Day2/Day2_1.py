with open('2019/Day2/input2.txt') as file:
    values = list(map(int, file.read().split(',')))

values[1] = 12
values[2] = 2
i = 0

while i < len(values):
    opcode = values[i]
    if opcode == 1:
        values[values[i+3]] = values[values[i+1]] + values[values[i+2]]
    elif opcode == 2:
        values[values[i+3]] = values[values[i+1]] * values[values[i+2]]
    elif opcode == 99:
        break
    else:
        raise ValueError("error")
    i += 4

print(values)
