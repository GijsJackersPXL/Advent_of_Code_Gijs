with open('2020/Day4/input2.txt') as input_line:
    n = 0
    passport = {}
    inputs = input_line.read().split('\n\n')
    for i in inputs:
        temp = i.replace('\n', ' ').split(' ')
        passport = dict(item.split(':') for item in temp)
        
        if all(field in passport for field in ('byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid')):
            if (
                1920 <= int(passport['byr']) <= 2002 and
                2010 <= int(passport['iyr']) <= 2020 and
                2020 <= int(passport['eyr']) <= 2030 and

                (('cm' in passport['hgt'] and 150 <= int(passport['hgt'].replace('cm', '')) <= 193) or
                ('in' in passport['hgt'] and 59 <= int(passport['hgt'].replace('in', '')) <= 76)) and
                len(passport['hcl']) == 7 and passport['hcl'][0] == '#' and all(c in '0123456789abcdef' for c in passport['hcl'][1:]) and
                passport['ecl'] in ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth') and
                len(passport['pid']) == 9 and passport['pid'].isdigit()):
                n += 1

    print(n)
