import sys
import hashlib
sys.path.append("/home/kit/Documents/advent_of_code")
import aoc

data = aoc.read("2015","04","str")

zeros = False
i = 0

while not zeros:
    string = data + str(i)
    string = string.encode()
    result = str(hashlib.md5(string).hexdigest())
    if result[:5] == "00000":
        print(result)
        print(i)
        zeros = True
    i+=1
