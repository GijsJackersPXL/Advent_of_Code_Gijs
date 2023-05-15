with open('2018/Day1/input2.txt') as input_line:
    lines = list(input_line.read().split('\n'))

    total_sum = sum(int(num) for num in lines)
   
    print(total_sum)



