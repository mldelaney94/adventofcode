input = '1113222113'

def look_and_say_string_generator (in_str):
    str_list = []
    old = ''
    count = 0
    i = 0
    while (i < len(in_str)):
        if i == 0:
            if len(in_str) == 1:
                str_list.append('1')
                str_list.append(in_str[i])
            else:
                old = in_str[i]
                count += 1
        elif i == len(in_str)-1:
            if old == in_str[i]:
                count += 1
                str_list.append(str(count))
                str_list.append(in_str[i])
            else:
                str_list.append(str(count))
                str_list.append(old)
                str_list.append('1')
                str_list.append(in_str[i])
        else:
            if old == in_str[i]:
                count += 1
            else:
                str_list.append(str(count))
                str_list.append(old)
                old = in_str[i]
                count = 1
        i += 1

    return "".join(str_list)


output = look_and_say_string_generator(input)

i = 0
while (i < 39):
    output = look_and_say_string_generator(output)
    i += 1

print (len(output))
