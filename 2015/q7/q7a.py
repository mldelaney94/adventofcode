

f = open ("inputQ7.txt", 'r')

for line in f:
    lline = line.strip()
    lline = line.split()
    if len(lline) < 5:
        print ('5')
        if len(lline) < 4:
            print ('numAssignment')
        else:
            print ('NOT assignment')
    else:
        wire1 = lline[0] # sometimes they're just numbers 
        wire2 = lline[2]
        wire3 = lline[4]
        if lline[1] == 'AND':
            print ('AND')
        elif lline[1] == 'OR':
            print ('OR')
        elif lline[1] == 'RSHIFT':
            print ('RIGHTSHIFT')
        elif lline[1] == 'LSHIFT':
            print ('LEFTSHIFT')


f.close()
