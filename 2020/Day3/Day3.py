with open('2020/Day3/input2.txt') as input_line:
    lines = input_line.read()
    line = lines.split("\n")[:-1]
    width = len(line[0])
    trees = 0
    x = 0
    # for i in line:
    #     print(x, ",", i[x % width])
    #     if i[x % width] == "#":
    #         trees += 1
    #     x += 7
    # print(trees+1)

    for n, i in enumerate(line):
        if n % 2 == 0:
            if i[x % width] == "#":
                trees += 1
            x += 1
    print(trees)

#82 * 242 * 71 * 67 * 24