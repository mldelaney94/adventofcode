""" Takes in a lowercase string 8 chars long, and turns it into a string that
follows these rules: three letters have a difference of 1, 'abc' or 'xyz';
may not contain i, o or l and two different pairs of chars like: 'aa' and 'bb'.
"""

already_guessed = 'hxccaabc'

def increment_string(to_inc):
    """ takes in a lowercase ascii string and increments the final char by 1,
    if it passes from z to a, then the char directly before that char is
    incremented by one """
    inc_list = list(to_inc)
    if inc_list[7] == 'z':
        inc_list[7] = 'a'
        if inc_list[6] == 'z':
            inc_list[6] = 'a'
            if inc_list[5] == 'z':
                inc_list[5] = 'a'
                if inc_list[4] == 'z':
                    inc_list[4] = 'a'
                    if inc_list[3] == 'z':
                        inc_list[3] = 'a'
                        if inc_list[2] == 'z':
                            inc_list[2] = 'a'
                            if inc_list[1] == 'z':
                                inc_list[1] = 'a'
                                if inc_list[0] == 'z':
                                    inc_list[0] = 'a'
                                else:
                                    inc_list[0] = chr(ord(inc_list[0])+1)
                            else:
                                inc_list[1] = chr(ord(inc_list[1])+1)
                        else:
                            inc_list[2] = chr(ord(inc_list[2])+1)
                    else:
                        inc_list[3] = chr(ord(inc_list[3])+1)
                else:
                    inc_list[4] = chr(ord(inc_list[4])+1)
            else:
                inc_list[5] = chr(ord(inc_list[5])+1)
        else:
            inc_list[6] = chr(ord(inc_list[6])+1)
    else:
        inc_list[7] = chr(ord(inc_list[7])+1)
    return ''.join(inc_list)

def is_legal_string(to_verify):
    """ takes in lowercase ascii string 8 chars long """
    list_verify = list(to_verify)
    if ('i', 'o', 'l') in list_verify:
        return False
    return has_increasing_straight(list_verify) and has_two_nonoverlapping_pairs(list_verify)

def has_increasing_straight(this_list):
    """ Checks string has three chars in a row with a numerical distance of
    1 """
    first = this_list[0]
    middle = this_list[1]
    for i in range(2, 8):
        if ord(first) == ord(middle)-1 and ord(middle) == ord(this_list[i])-1:
            return True
        first = middle
        middle = this_list[i]
    return False

def has_two_nonoverlapping_pairs(this_list):
    """ checks string has 2 separate pairs of chars that do not overlap """
    num = 0
    already_discovered = ''
    for i in range(0, 8, 1):
        if i == 7:
            break
        first = this_list[i]
        middle = this_list[i+1]
        if first == middle and middle != already_discovered:
            num += 1
            already_discovered = first
    if num >= 2:
        return True
    return False

def main():
    curr_password = 'hxbxxzaa'
    while not is_legal_string(curr_password):
        curr_password = increment_string(curr_password)

    print(curr_password)


if __name__ == '__main__':
    main()


assert increment_string('xxxxxxxx') == 'xxxxxxxy'
assert increment_string('xxxxxxxz') == 'xxxxxxya'
assert increment_string('zazazaza') == 'zazazazb'
assert increment_string('zzzzzzzz') == 'aaaaaaaa'
assert increment_string('aacczzzz') == 'aacdaaaa'
assert has_increasing_straight(['a', 'b', 'c']) == True
assert has_increasing_straight(['c', 'b', 'c', 'd']) == True
assert has_increasing_straight(['c', 'b', 'c', 'e', 'e', 'e', 'e', 'e']) == False
assert has_two_nonoverlapping_pairs(['c', 'c', 'd', 'd', 'p', 'h', 'n', 'z']) == True
assert has_two_nonoverlapping_pairs(['c', 'b', 'c', 'e', 'e', 'e', 'e',
                                     'e']) == False
assert has_increasing_straight(['a', 'b', 'c', 'd', 'f', 'f', 'a', 'a']) == True
assert has_two_nonoverlapping_pairs(['a', 'b', 'c', 'd', 'f', 'f', 'a', 'a']) == True
assert is_legal_string('hijklmmn') == False
assert is_legal_string('abcdffaa') == True
