with open('Day1/Day1_input2.txt') as f:
    total = []
    sub_total = 0
    for line in f:
        line = line.strip()
        if not line:
            total.append(sub_total)
            sub_total = 0
            continue
        sub_total += int(line)
    if sub_total:
        total.append(sub_total)
print("Total array:", total)

highest = max(total)
print("Highest element:", highest)

highest = sorted(total, reverse=True)[:3]
total_sum = sum(highest)
print("Sum of top 3 highest elements:", total_sum)



