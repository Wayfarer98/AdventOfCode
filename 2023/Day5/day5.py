from Helpers.DataHelper import DataHelper
import numpy as np

data = DataHelper(2023, 5).get_data()
splits = np.where(data == '')[0]
seeds = data[0].split(': ')[1].split()

#---------------------PART 1---------------------#

def get_location(seed):
    mapping = int(seed)
    for i in range(len(splits)-1):
        start_mapping_idx = splits[i] + 2
        end_mapping_idx = splits[i+1]

        for row in data[start_mapping_idx:end_mapping_idx]:
            nums = row.split()
            source = int(nums[1])
            dest = int(nums[0])
            ran = int(nums[2])
            if source <= mapping <= source + ran:
                mapping = dest + mapping - source
                break

    return mapping
res = min([get_location(seed) for seed in seeds])
print(f"Solution to part 1: {res}")

#---------------------PART 2---------------------#

def range_overlab(r1, r2):
    if r1.start < r2.stop and r2.start <= r1.stop:
        return range(max(r1.start, r2.start), min(r1.stop, r2.stop))
    else:
        return range(r1.start, r1.start)

def part2():
    seeds_int = list(map(int, seeds))
    ranges = list(map(lambda i: range(seeds_int[i], seeds_int[i] + seeds_int[i+1]), range(0, len(seeds_int), 2)))
    conversions = []
    for i in range(len(splits)-1):
        lines = list(map(lambda row: row.split(), data[splits[i]+2:splits[i+1]]))
        lines = list(map(lambda i: tuple(map(int, i)), lines))
        conversions.append(lines)

    for conversion in conversions:
        converted = []
        unconverted = ranges

        for (dst, src, rng) in conversion:
            conversion_range = range(src, src + rng)
            offset = dst - src

            new_unconverted = []

            for unconv_range in unconverted:
                overlap = range_overlab(unconv_range, conversion_range)
                left = range(unconv_range.start, overlap.start)
                if left.stop > left.start:
                    new_unconverted.append(left)
                if overlap.stop > overlap.start:
                    converted.append(range(overlap.start + offset, overlap.stop + offset))

                right = range(overlap.stop, unconv_range.stop)
                if right.stop > right.start:
                    new_unconverted.append(right)

            unconverted = new_unconverted

        ranges = unconverted + converted

    return min(list(map(lambda rng: rng.start, ranges)))

res = part2()
print(f"Solution to part 2: {res}")
