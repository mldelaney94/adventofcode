import hashlib

def fiveZeroes (string):
    if (string[0] == '0' and string[1] == '0' and string[2] == '0' and string[3] == '0' and string[4] == '0'and string[5] == '0'):
        return True
    return False

digit = 0
salt = 'ckczppom' + str(digit)
result = hashlib.md5(salt.encode())
while (fiveZeroes(result.hexdigest()) == False):
    digit += 1
    salt = 'ckczppom' + str(digit)
    result = hashlib.md5(salt.encode())

print(digit)
