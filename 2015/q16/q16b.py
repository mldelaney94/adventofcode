""" finds the *REAL* aunt Sue """
import re

AUNT_SUE = {
    'children': 3,
    'cats': 7,
    'samoyeds': 2,
    'pomeranians': 3,
    'akitas': 0,
    'vizslas': 0,
    'goldfish': 5,
    'trees': 3,
    'cars': 2,
    'perfumes': 1,
}

def find_sue():
    with open('inputQ16.txt', 'r') as f:
        for line in f:
            break_out = False
            #each susan only has 3 attributes
            curr_sue = re.findall(r"(\d\d*\d*): (\w+): (\d+\d*), (\w+): (\d+\d*), (\w+): (\d+\d*)", line)
            for index, item in enumerate(curr_sue[0]):
                if item in ('trees', 'cats'):
                    if int(curr_sue[0][index+1]) >= AUNT_SUE[item]:
                        break_out = True
                elif item in ('goldfish', 'pomeranians'):
                    if int(curr_sue[0][index+1]) <= AUNT_SUE[item]:
                        break_out = True
                else:
                    if index % 2 == 1:
                        if int(curr_sue[0][index+1]) != AUNT_SUE[item]:
                            break_out = True
                if break_out:
                    break
            if break_out:
                continue
            print(curr_sue)

find_sue()
