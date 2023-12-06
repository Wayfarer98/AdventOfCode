from Helpers.DataHelper import DataHelper
import numpy as np

data = DataHelper(2023, 6).get_data()[:-1]
times = list(map(int, data[0].split(": ")[1].strip().split()))
distances = list(map(int, data[1].split(": ")[1].strip().split()))

# -------------------------Part 1-------------------------#

def find_intersect(records, total_time):
    d = total_time**2 - 4 * records
    intersections = [(-total_time + np.sqrt(d))/-2, (-total_time - np.sqrt(d))/-2]
    intersections = list(map(int, [np.ceil(intersections[0]), np.floor(intersections[1])]))
    return max(intersections) - min(intersections) + 1

results = [find_intersect(record, time) for record, time in zip(distances, times)]
print(f"Solution 1: {np.prod(results)}")

# -------------------------Part 2-------------------------#

time = "".join(list(map(str, times)))
distance = "".join(list(map(str, distances)))
print(f"Solution 2: {find_intersect(int(distance), int(time))}")