with open('2019/Day3/input2.txt') as f:
    data = [s.split(',') for s in f.read().split('\n')[:-1]]

wire1 = {}
wire2 = {}
x = y = steps = 0

for j in data[0]:
    direction = j[0]
    distance = int(j[1:])
    for _ in range(distance):
        if direction == 'R':
            x += 1
        elif direction == 'L':
            x -= 1
        elif direction == 'U':
            y += 1
        elif direction == 'D':
            y -= 1
        steps += 1
        wire1[(x, y)] = steps

x = y = steps = 0
intersections = []

for j in data[1]:
    direction = j[0]
    distance = int(j[1:])
    for _ in range(distance):
        if direction == 'R':
            x += 1
        elif direction == 'L':
            x -= 1
        elif direction == 'U':
            y += 1
        elif direction == 'D':
            y -= 1
        steps += 1
        if (x, y) in wire1:
            intersections.append((x, y, steps + wire1[(x, y)]))

manhattan_distances = [abs(x) + abs(y) for x, y, _ in intersections]
total_steps = [steps for _, _, steps in intersections]

print(min(manhattan_distances))
