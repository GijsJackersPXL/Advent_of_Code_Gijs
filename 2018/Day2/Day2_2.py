with open('2018/Day2/input2.txt') as input_line:
    box_ids = [line.strip() for line in input_line]

two_count = 0
three_count = 0

for box_id in box_ids:
    counts = {}
    for char in box_id:
        counts[char] = counts.get(char, 0) + 1

    if 2 in counts.values():
        two_count += 1
    if 3 in counts.values():
        three_count += 1

checksum = two_count * three_count
#print(f"checksum: {checksum}")

for i in range(len(box_ids)):
    for j in range(i+1, len(box_ids)):
        id1 = box_ids[i]
        id2 = box_ids[j]

        differing_chars = [c1 for c1, c2 in zip(id1, id2) if c1 != c2]
        if len(differing_chars) == 1:
            common_letters = id1.replace(differing_chars[0], "")
            print(f"{common_letters}")
            exit()

print("/") # no common letters
