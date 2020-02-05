import re
f = open ("inputQ5.txt", 'r')

p = re.compile('[aeiou][^ab][^cd][^pq][^xy]*{2,}')

i = 0
for line in f:
    if (p.match(line)):
        i += 1

print (i)

f.close()
