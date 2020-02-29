import json

#answer is 87842


def part_b_sum (data):
    summation = 0
    for item in data:
        for div in item:
            if isinstance(div, int):
                summation += div
            elif isinstance(div, list):
                summation += sum([int(i) for i in div if type(i) == int])
            elif isinstance(div, dict):
                if "red" in div:
                    print("red")
                else:
                    summation += sum(list(div.values())
            else:
                pass
    print(summation)
            

with open('inputQ12.txt') as json_file:
    data = json.load(json_file)
    part_b_sum(data)

