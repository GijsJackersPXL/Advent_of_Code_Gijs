with open('2020/Day2/input2.txt') as input_line:
    lines = input_line.readlines()
    lines = [single_line.strip() for single_line in lines]

    count_true = 0
    for line1 in lines:
        min_max_times = line1.split()[0]
        min_times = min_max_times.split('-')[0].strip()
        max_times = min_max_times.split('-')[1].strip()
        letter = line1.split()[1]
        contain_letter = letter[:-1]
        password = line1.split()[2]
        # print(password[1])

        # if contain_letter in password:
        #     count = password.count(contain_letter)
        #     if count >= int(min_times) and count <= int(max_times):
        #         count_true += 1

        if (password[int(min_times)-1] == contain_letter) ^ (password[int(max_times)-1] == contain_letter):
            count_true += 1
        
    
    print(count_true)