import sys
sys.path.append("/home/kit/Documents/advent_of_code")
import aoc
import copy

class seed_map:
    def __init__(self):
        self.dest_range = []
        self.source_range = []
        self.range_len = []

def read():
    seed_maps = []
    data = aoc.read("2023","05","list")

    for i in range(len(data)):
        data[i] = data[i].replace("\n","")
    # first line is seeds (or seed ranges)
    seeds = aoc.get_nums_from_string(data[0]) 
    # remove first two lines (seeds and empty space)
    data.pop(0)
    data.pop(0)

    destrange = []
    sourcerange = []
    rangelen = []

    for line in data:
        if len(line) == 0: # empty line, this set of mappings has ended
            m.dest_range = destrange
            m.source_range = sourcerange
            m.range_len = rangelen
            seed_maps.append(m)
            destrange = []
            sourcerange = []
            rangelen = []
        elif ":" in line: # a new mapping begins
            m = seed_map()
        else:
            nums = aoc.get_nums_from_string(line)
            destrange.append(nums[0])
            sourcerange.append(nums[1])
            rangelen.append(nums[2])
    # add the final mapping
    m.dest_range = destrange
    m.source_range = sourcerange
    m.range_len = rangelen
    seed_maps.append(m)
    return seed_maps, seeds

def do_the_map_thing(m,seeds,i,offset = 0):
    idx = i + offset
    for j in range(len(m.dest_range)):
        # checks if the "initial" seed is within the maps range
        if seeds[idx] >= m.source_range[j] and seeds[idx] < m.source_range[j] + m.range_len[j]:
            # difference between the seed number and the start of the mapping range
            diff = seeds[idx] - m.source_range[j]
            # get the maximum number of seeds that can be mapped
            # source_range + range_len gives the top end of the mapping range
            # -seeds[i] accounts for where in the range you start
            maxseeds = m.source_range[j] + m.range_len[j] - seeds[idx]
            # if we can map all the seeds in our range
            if maxseeds >= seeds[idx+1]:
                # map seeds[i] to the destination range, plus its offset from the start of the range
                seeds[idx] = m.dest_range[j] + diff
            else:
                # set the new range of these seeds to the maximum number of seeds we can map
                temp = seeds[idx+1]
                seeds[idx+1] = maxseeds
                # new starting position is current position + the most seeds we could map
                seeds.append(seeds[idx] + maxseeds)
                # new range is original range - maximum mappable seeds
                seeds.append(temp - maxseeds)
                seeds[idx] = m.dest_range[j] + diff
            # DON'T MAP THE SAME SEED TWICE
            break
    return seeds

def part_one(seeds, seed_maps):
    for m in seed_maps:
        for i in range(len(seeds)):
            for j in range(len(m.dest_range)):
                if seeds[i] >= m.source_range[j] and seeds[i] < m.source_range[j]+m.range_len[j]:
                    # difference between the seed number and the start of the mapping range
                    diff = seeds[i] - m.source_range[j]
                    # map seeds[i] to the destination range, plus its offset from the start of the range
                    seeds[i] = m.dest_range[j] + diff
                    # DON'T MAP THE SAME SEED TWICE
                    break
    return min(seeds)

def part_two(seeds, seed_maps):
    for m in seed_maps:
        # loop over every other element of seeds
        # gets the start position, not the range length
        for i in range(0,len(seeds),2):
            # maps all the seed ranges that were initially in the list
            seeds = do_the_map_thing(m,seeds,i)
        # we might have added some extra seed ranges, so we need to deal with those
        # loops until we have gone through all added seed ranges (including ones added in this loop)
        # could I build the first for loop into this? yes probably but I'm not about to
        while i+2 < len(seeds):
            seeds = do_the_map_thing(m,seeds,i,2)
            i += 2
    minimum = -1
    for i in range(0,len(seeds),2):
        if minimum == -1 or seeds[i] < minimum:
            minimum = seeds[i]
    return minimum

seed_maps,seeds = read()

print(f"the answer to part one is {part_one(copy.deepcopy(seeds),seed_maps)}")
print(f"the answer to part two is {part_two(copy.deepcopy(seeds),seed_maps)}")