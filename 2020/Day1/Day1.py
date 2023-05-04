with open('2020/Day1/input2.txt') as input_line:
    lines = input_line.readlines()
    lines = [single_line.strip() for single_line in lines]

    # for line1 in lines:
    #     # print(line1)
    #     for line2 in lines:
    #         # print(line2)
    #         if (int(line1) + int(line2) == 2020):
    #             print(int(line1) * int(line2))

    for line1 in lines:
        # print(line1)
        for line2 in lines:
            # print(line2)
            for line3 in lines:
                if (int(line1) + int(line2) + int(line3) == 2020):
                    print(int(line1) * int(line2) * int(line3))
