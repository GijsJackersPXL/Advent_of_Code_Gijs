from datetime import datetime

with open("2018/Day4/input2.txt") as file:
    input_data = file.read()

input_data = [(datetime.strptime(line[1:17], "%Y-%m-%d %H:%M"), line[19:]) for line in input_data.strip().split("\n")]
input_data.sort()

sleep = {}
current_guard = None

for timestamp, event in input_data:
    if event.startswith("Guard #"):
        current_guard = int(event.split()[1][1:])
    elif event == "falls asleep":
        sleep_start = timestamp
    elif event == "wakes up":
        sleep_end = timestamp
        if current_guard not in sleep:
            sleep[current_guard] = [0] * 60
        for minute in range(sleep_start.minute, sleep_end.minute):
            sleep[current_guard][minute] += 1

sleepiest_guard = max(sleep, key=lambda k: sum(sleep[k]))
sleepiest_minute = max(range(60), key=lambda i: sleep[sleepiest_guard][i])
part1_result = sleepiest_guard * sleepiest_minute
print("Part 1:", part1_result)

guard_sleep = {}

for timestamp, event in input_data:
    if event.startswith("Guard #"):
        current_guard = int(event.split()[1][1:])
    elif event == "falls asleep":
        sleep_start = timestamp
    elif event == "wakes up":
        sleep_end = timestamp
        if current_guard not in guard_sleep:
            guard_sleep[current_guard] = [0] * 60
        for minute in range(sleep_start.minute, sleep_end.minute):
            guard_sleep[current_guard][minute] += 1

most_frequent_guard = max(guard_sleep, key=lambda k: max(guard_sleep[k]))
most_frequent_minute = max(range(60), key=lambda i: guard_sleep[most_frequent_guard][i])
part2_result = most_frequent_guard * most_frequent_minute
print("Part 2:", part2_result)