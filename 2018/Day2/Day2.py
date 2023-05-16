two_count = 0
three_count = 0

with open('2018/Day2/input2.txt') as input_line:
    for line in input_line:
        counts = {}
        for char in line.strip():
            counts[char] = counts.get(char, 0) + 1

        if 2 in counts.values():
            two_count += 1
        if 3 in counts.values():
            three_count += 1

checksum = two_count * three_count
print(f"The checksum is: {checksum}")
