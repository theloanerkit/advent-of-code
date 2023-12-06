import sys
sys.path.append("/home/kit/Documents/advent_of_code")
import aoc
import math

def how_long_to_button(t,x):
    options = 0
    # don't start from one, there's no point
    min_button = math.floor((t-math.sqrt((t*t)-(4*x)))/2)
    for button_time in range(min_button,t+1):
        moving_time = t - button_time
        distance = moving_time * button_time
        if distance > x:
            options += 1
        # if you stopped travelling far enough, you will never travel far enough again
        elif distance < x and options > 0:
            break
    return options

def part_one(data):
    times = aoc.get_nums_from_string(data[0])
    distances = aoc.get_nums_from_string(data[1])

    num_options = []

    for i in range(len(times)):
        options = how_long_to_button(times[i],distances[i])
        num_options.append(options)

    return aoc.multiply_list(num_options)

def part_two(data):
    for i in range(len(data)):
        data[i] = data[i].replace(" ","")

    times = aoc.get_nums_from_string(data[0])
    distances = aoc.get_nums_from_string(data[1])

    options = how_long_to_button(times,distances)
    return options

data = aoc.read("2023","06","list")
for i in range(len(data)):
    data[i] = data[i].replace("\n","")


print(f"the answer to part one is {part_one(data)}")
print(f"the answer to part two is {part_two(data)}")