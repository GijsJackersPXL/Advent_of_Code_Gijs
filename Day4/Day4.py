with open('Day4/input2.txt', 'r') as f:
    lines = f.readlines()
    lines = [single_line.strip() for single_line in lines]

    def part1_in_part2(part_a, part_b):
        start_a, end_a = map(int, part_a.split('-'))
        start_b, end_b = map(int, part_b.split('-'))
        #print("start a: ", start_a, "b: ", start_b)
        
        return start_b <= start_a and end_a <= end_b

    pairs = 0
    overlap = 0

    for line in lines:
        part1, part2 = line.split(',')
        if part1_in_part2(part1, part2) or part1_in_part2(part2, part1):
            #print("true")
            pairs += 1
        
        start_a, end_a = map(int, part1.split('-'))
        start_b, end_b = map(int, part2.split('-'))
        if start_a in range(start_b, end_b+1) or end_a in range(start_b, end_b+1) or  start_b in range(start_a, end_a+1) or end_b in range(start_a, end_a+1):
            overlap += 1
    
    print("part1: ", pairs)
    print("part2: ", overlap)