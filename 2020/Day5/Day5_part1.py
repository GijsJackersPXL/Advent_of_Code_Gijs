with open("2020/Day5/input2.txt") as input_line:
    lines = input_line.read().splitlines()

ids = []
for line in lines:
    binary_str = ""
    for c in line:
        if c in "BR":
            binary_str += "1"
        else:
            binary_str += "0"
    seat_id = int(binary_str, 2)
    # print(seat_id)
    ids.append(seat_id)

ids = sorted(ids)
print(ids[-1])