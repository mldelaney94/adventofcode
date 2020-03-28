""" finds the *REAL* aunt Sue
In particular, what the problem means is that the real Sue has > 7 cats, > 3 trees,
< 5 goldfish and < 3 pomeranians, so equalling that number is also wrong
I struggled because I thought it meant that the sue's in the input had greater
than that many cats and trees"""
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
            for index, attrib in enumerate(curr_sue[0]):
                if attrib in ('trees', 'cats'):
                    if int(curr_sue[0][index+1]) <= AUNT_SUE[attrib]:
                        break_out = True
                elif attrib in ('goldfish', 'pomeranians'):
                    if int(curr_sue[0][index+1]) >= AUNT_SUE[attrib]:
                        break_out = True
                else:
                    if index % 2 == 1:
                        if int(curr_sue[0][index+1]) != AUNT_SUE[attrib]:
                            break_out = True
                if break_out:
                    break
            if break_out:
                continue
            print(curr_sue)

find_sue()
