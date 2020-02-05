f = open ("inputQ1.txt", "r") # read mode

i = 0
j = 0
for line in f:
    for char in line:
        if char == '(':
            i += 1
        else:
            i -= 1
        j += 1
        if (i == -1):
            break

print (j)
f.close()
