with open('2019/Day1/input2.txt') as input_line:
    lines = input_line.readlines()
    lines = [single_line.strip() for single_line in lines]

    # total = []
    # for input in lines:
    #     total.append((int(input)//3) - 2)
    # print(total) 

    total_fuel = 0
    for mass in lines:
        fuel_mass = int(mass)
        fuel_for_module = 0
        while fuel_mass // 3 - 2 > 0:
            fuel_mass = fuel_mass // 3 - 2
            fuel_for_module += fuel_mass
        total_fuel += fuel_for_module
    print(total_fuel)
