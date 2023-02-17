import random
from Solution import *
from big_nums import bnums

# case1
# nums = [0, 0, 0]

# case2
# nums = [-1,0,1,2,-1,-4]

# case3
# nums = [0, 1, 1]

# case4
# nums = bnums

# case5
count = 3000  # 3 <= count <= 3000
num_range_max = int(1e05)
num_range_min = int(-1e05)
nums = [random.randint(num_range_min, num_range_max) for i in range(count)]

triplets = Solution9.three_sum(nums)
print(triplets)
