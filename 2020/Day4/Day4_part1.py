with open('2020/Day4/input2.txt') as input_line:
    lines = input_line.read()
    inputs = lines.split("\n\n")
    n = 0
    for i in inputs:
        if "byr:" in i and \
        "iyr:" in i and \
        "eyr:" in i and \
        "hgt:" in i and \
        "hcl:" in i and \
        "ecl:" in i and \
        "pid:" in i:
            n += 1
    print(n)