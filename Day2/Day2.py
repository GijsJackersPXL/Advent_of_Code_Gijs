with open('Day2/input2.txt') as input_line:
    score = 0
    for line in input_line:
        char1 = line[0]
        char2 = line[2]
        
        #PART1
        # #starting with A (Rock)
        # if char1 == 'A' and char2 == 'X':
        #     score += 1+3
        # elif char1 == 'A' and char2 == 'Y':
        #     score += 2+6
        # elif char1 == 'A' and char2 == 'Z':
        #     score += 3+0

        # #starting with B (Paper)
        # elif char1 == 'B' and char2 == 'X':
        #     score += 1+0
        # elif char1 == 'B' and char2 == 'Y':
        #     score += 2+3
        # elif char1 == 'B' and char2 == 'Z':
        #     score += 3+6

        # #starting with C (Scissors)
        # elif char1 == 'C' and char2 == 'X':
        #     score += 1+6
        # elif char1 == 'C' and char2 == 'Y':
        #     score += 2+0
        # elif char1 == 'C' and char2 == 'Z':
        #     score += 3+3

        #PART2
        #starting with A (Rock)
        if char1 == 'A' and char2 == 'X':
            score += 3+0
        elif char1 == 'A' and char2 == 'Y':
            score += 1+3
        elif char1 == 'A' and char2 == 'Z':
            score += 2+6

        #starting with B (Paper)
        elif char1 == 'B' and char2 == 'X':
            score += 1+0
        elif char1 == 'B' and char2 == 'Y':
            score += 2+3
        elif char1 == 'B' and char2 == 'Z':
            score += 3+6

        #starting with C (Scissors)
        elif char1 == 'C' and char2 == 'X':
            score += 2+0
        elif char1 == 'C' and char2 == 'Y':
            score += 3+3
        elif char1 == 'C' and char2 == 'Z':
            score += 1+6
        else:
            print("fout")
    print(score)


