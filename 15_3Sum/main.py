import random
from Solution import Solution7
from big_nums import bnums

# case1
# nums = [0, 0, 0]

# case2
# nums = [-1,0,1,2,-1,-4]

# case3
nums = bnums

# case4
# nums = []
# [nums.append(random.randint(int(-1e05), int(1e05))) for i in range(3000)]

triplets = Solution7.three_sum(nums)
print(triplets)
