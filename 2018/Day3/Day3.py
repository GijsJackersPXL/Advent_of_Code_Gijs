with open('2018/Day3/input2.txt') as input_file:
    input_data = input_file.read()

fabric = [[0 for _ in range(1000)] for _ in range(1000)]
claims = []

for line in input_data.split("\n"):
    claim_parts = line.split()
    claim_id = int(claim_parts[0][1:])
    dist_to_left, dist_to_top = map(int, claim_parts[2][:-1].split(","))
    width, height = map(int, claim_parts[3].split("x"))
    claims.append((claim_id, dist_to_left, dist_to_top, width, height))

alone = list(range(1, len(claims) + 1))

for claim in claims:
    claim_id, dist_to_left, dist_to_top, width, height = claim
    for i in range(dist_to_left, dist_to_left + width):
        for j in range(dist_to_top, dist_to_top + height):
            if fabric[i][j] == 0:
                fabric[i][j] = claim_id
            else:
                if claim_id in alone:
                    alone.remove(claim_id)
                if fabric[i][j] > 0 and fabric[i][j] in alone:
                    alone.remove(fabric[i][j])
                fabric[i][j] = -1

over_claimed = sum(fabric[i][j] < 0 for i in range(1000) for j in range(1000))

print(over_claimed)
print(alone[0])
