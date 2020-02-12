f = open("inputQ12.txt", "r")

num = []
all_nums = []
total = 0
for line in f:
    for c in line:
        if c.isdigit() or c == '-':
            num.append(c)
        else:
            if len(num) > 0:
                all_nums.append(int("".join(num)))
                num.clear()

print(sum(all_nums))
