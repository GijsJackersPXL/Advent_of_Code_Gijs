with open('2018/Day1/input2.txt') as input_line:
    lines = list(input_line.read().split('\n'))

    int_input = [int(num) for num in lines]
    size = len(int_input)
    frequency = 0
    reached = {}
    reached_twice = None
    is_found = False

    for val in int_input:
        frequency += val
        if frequency in reached:
            reached_twice = frequency
            is_found = True
            break
        reached[frequency] = True

    i = 0
    while not is_found:
        frequency += int_input[i]
        if frequency in reached:
            reached_twice = frequency
            is_found = True
            break
        reached[frequency] = True
        i = (i + 1) % size

    print(reached_twice)

