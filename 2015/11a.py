import sys
sys.path.append("/home/kit/Documents/advent_of_code")
import aoc

# a=97  z=122

LETTERS = "abcdefghijklmnopqrstuvwxyz"

def convert_to_ascii(chars):
    new_word = []
    for c in chars:
        new_word.append(ord(c))
    return new_word

def convert_to_chars(ascii):
    word = ""
    for a in ascii:
        word += chr(a)
    return word

def increment(word):
    word[-1]+=1
    if word[-1] == 123:
        word[-1] = 97
        word[-2] += 1
        for i in range(2,len(word),1):
            j=-i
            if word[j] == 123:
                word[j] = 97
                word[j-1] +=1
            else:
                break
    return word

def get_next_password(password):
    pass_nums = convert_to_ascii(password)
    next_pass = increment(pass_nums)
    pass_chars = convert_to_chars(next_pass)
    return pass_chars

def condition_abc(password):
    for i in range(len(password)-2):
        string = password[i]+password[i+1]+password[i+2]
        if string in LETTERS:
            return True
    return False

def condition_iol(password):
    if "i" in password or "o" in password or "l" in password:
        return False
    else:
        return True
    
def condition_pairs(password):
    pairs = []
    while len(password) > 1:
        if password[0]==password[1]:
            pairs.append(password[0]+password[1])
            password = password[2:]
        else:
            password = password[1:]
    unique_pairs = set(pairs)
    if len(unique_pairs)>1:
        return True
    else:
        return False

def allowed_password(password):
    if condition_abc(password) and condition_iol(password) and condition_pairs(password):
        return True
    else:
        return False

data = list(aoc.read("2015","11","str"))
test = "hepxxyzz"
password = test

run = True
while run:
    password = get_next_password(password)
    if allowed_password(password):
        run = False
    
print(f"santa's new password is {password}")
