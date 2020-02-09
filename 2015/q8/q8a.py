f = open("inputQ8.txt", 'r')

in_memory_len = 0
code_rep_len = 0
diff = 0

# build a list of length one strings, join them at the end

def string_builder_with_advent_rules(advent_string):
    string_list = []
    i = 0
    while (i < len(advent_string)-1):
        if advent_string[i] == '"':
            pass
        else:
            if advent_string[i] == '\\':
                if advent_string[i+1] == '"':
                    string_list.append('\"')
                    i += 1
                elif advent_string[i+1] == '\\':
                    string_list.append('\\')
                    i += 1
                elif advent_string[i+1] == 'x':
                    string_list.append('a')
                    i += 3
            #what
            else:
                string_list.append(advent_string[i])
        i += 1

    return "".join(string_list)


for line in f:
    line = line.strip()
    in_memory_len = len(line)
    code_rep_len = len(string_builder_with_advent_rules(line))
    diff += in_memory_len - code_rep_len


print(diff)
