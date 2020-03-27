""" finds the real aunt Sue """
import re

aunt_sue = {
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
            #each susan only has 3 attributes
            sue = re.findall(r"(\d\d*\d*): (\w+): (\d+\d*), (\w+): (\d+\d*), (\w+): (\d+\d*)", line)
            if aunt_sue[sue[0][1]] == int(sue[0][2]) and aunt_sue[sue[0][3]] == int(sue[0][4]) and aunt_sue[sue[0][5]] == int(sue[0][6]):
                print(sue[0])
                break

find_sue()
