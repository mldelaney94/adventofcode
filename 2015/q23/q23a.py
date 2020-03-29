""" simulates a computer with tpl, hlp, inc, jmp, jio, jie commands
2 points of improvement: ONE, didn't read the question problem, JIO means jump
if ONE not jump if ODD, initially didn't have that. Second is
i < len(instruction) as opposed to i < len(instruction)-1, these two problems
held me up for over an hour"""

REG_A = 1
REG_B = 0

def inc(register):
    global REG_A, REG_B
    if register == 'a':
        REG_A = REG_A + 1
    else:
        REG_B = REG_B + 1

def hlf(register):
    global REG_A, REG_B
    if register == 'a':
        REG_A = REG_A // 2
    else:
        REG_B = REG_B // 2

def tpl(register):
    global REG_A, REG_B
    if register == 'a':
        REG_A = REG_A * 3
    else:
        REG_B = REG_B * 3

def jmp(curr_place, offset):
    return curr_place + offset

def jie(register, curr_place, offset):
    global REG_A, REG_B
    if register == 'a':
        if REG_A % 2 == 0:
            return curr_place + offset
    else:
        if REG_B % 2 == 0:
            return curr_place + offset
    return curr_place

def jio(register, curr_place, offset):
    global REG_A, REG_B
    if register == 'a':
        if REG_A == 1:
            return curr_place + offset
    else:
        if REG_B == 1:
            return curr_place + offset
    return curr_place

INSTR_DICT = {'inc': inc,
              'hlf': hlf,
              'tpl': tpl} #literally just saves some lines in loop

def main():
    global REG_A, REG_B
    instructions = []
    with open('inputQ23.txt', 'r') as f:
        for line in f:
            line = line.replace(',', '')
            line = line.strip()
            line = line.strip(' ')
            instructions.append(line)
    loop(instructions)

def loop(instructions):
    global REG_A, REG_B
    i = 0
    while i < len(instructions):
        instruction = instructions[i]
        instr_split = instruction.split()
        jumped = False
        if instr_split[0] in ('inc', 'hlf', 'tpl'):
            INSTR_DICT[instr_split[0]](instr_split[1])
            print(instr_split[0] + instr_split[1])
        else:
            tmp = i
            if instr_split[0] == 'jmp':
                print(instr_split[0] + instr_split[1])
                i = jmp(i, int(instr_split[1]))
                if tmp != i:
                    jumped = True
            elif instr_split[0] == 'jio':
                print(instr_split[0] + instr_split[1] + instr_split[2])
                i = jio(instr_split[1], i, int(instr_split[2]))
                if tmp != i:
                    jumped = True
            elif instr_split[0] == 'jie':
                print(instr_split[0] + instr_split[1] + instr_split[2])
                i = jie(instr_split[1], i, int(instr_split[2]))
                if tmp != i:
                    jumped = True
        if jumped == False:
            i += 1

if __name__ == '__main__':
    main()
    print(REG_B)
