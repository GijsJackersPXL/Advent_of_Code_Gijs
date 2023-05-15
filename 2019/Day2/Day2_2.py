
with open('2019/Day2/input2.txt') as input_line:
    raw_data = input_line.read()

program_input = list(map(int, raw_data.split(',')))

for noun in range(100):
    for verb in range(100):
        memory = program_input[:]
        memory[1] = noun
        memory[2] = verb

        instruction_pointer = 0

        while memory[instruction_pointer] != 99:
            opcode = memory[instruction_pointer]
            operand1 = memory[memory[instruction_pointer + 1]]
            operand2 = memory[memory[instruction_pointer + 2]]
            target_position = memory[instruction_pointer + 3]

            if opcode == 1:
                memory[target_position] = operand1 + operand2
            elif opcode == 2:
                memory[target_position] = operand1 * operand2

            instruction_pointer += 4

        output = memory[0]

        if output == 19690720:
            result = 100 * noun + verb
            print(result)
            found = True
            break

