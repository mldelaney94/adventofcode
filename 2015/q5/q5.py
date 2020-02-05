import re
f = open ("inputQ5.txt", 'r')

p = re.compile(".*[aeiou].*[aeiou].*[aeiou].*") # ensure 3 vowels anywhere in the string
q = re.compile(r".*(\w)\1.*")                   # ensure 2 repeating letters
t = re.compile("^(?!.*(ab|cd|pq|xy))")          # ensure does not contain ab, cd, pq or xy using negative lookaheads
x = re.compile(r".*(\w)(\w).*\1\2.*")           # matches 2 pairs of words
y = re.compile(r".*([a-z]){1}.{1}\1{1}.*")             # matches one letter with a letter between them, like yxy

i = 0
for line in f:
    if (y.match(line) and x.match(line)):
        print(line)
        i += 1

print (i)

f.close()
