with open('Day3/input2.txt', 'r') as f:
    lines = f.readlines()
    lines = [single_line.strip() for single_line in lines]

    sum_value = 0
    # for letter in lines:
    #     first_half = set(letter[ :len(letter)//2])
    #     second_half = set(letter[len(letter)//2: ])
         
    #     overlap_char = (first_half.intersection(second_half)).pop()

    #     if overlap_char.isupper():
    #         sum_value += ord(overlap_char) - ord('A') + 27
    #     else:
    #         sum_value += ord(overlap_char) - ord('a') + 1
    # print(sum_value)

    while len(lines) > 0:
        first_part = set(lines.pop())
        second_part = set(lines.pop())
        third_part = set(lines.pop())
        
        overlap_char = ((first_part.intersection(second_part)).intersection(third_part)).pop()

        if overlap_char.isupper():
            sum_value += ord(overlap_char) - ord('A') + 27
        else:
            sum_value += ord(overlap_char) - ord('a') + 1
    print(sum_value)