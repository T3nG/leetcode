from itertools import combinations


class Solution1:
    @staticmethod
    def three_sum(nums):
        nums_len = len(nums)
        triplets = []
        for i in range(nums_len):
            for j in range(nums_len):
                for k in range(nums_len):
                    if i != j and i != k and j != k:
                        target = [nums[i], nums[j], nums[k]]
                        if sum(target) == 0:
                            target_sorted = sorted(target)
                            if target_sorted not in triplets:
                                triplets.append(target_sorted)
        return triplets


class Solution2:
    @staticmethod
    def three_sum(nums):
        nums_len = len(nums)
        comb_lst = list(combinations(range(nums_len), 3))
        triplets = []
        for i in range(len(comb_lst)):
            target = [
                nums[comb_lst[i][0]],
                nums[comb_lst[i][1]],
                nums[comb_lst[i][2]]
            ]
            if sum(target) == 0:
                st = sorted(target)
                if st not in triplets:
                    triplets.append(st)
        return triplets


class Solution3:
    @staticmethod
    def three_sum(nums):
        comb_nums = list(combinations(nums, 3))
        triplets = []
        for i in range(len(comb_nums)):
            target = [
                comb_nums[i][0],
                comb_nums[i][1],
                comb_nums[i][2]
            ]
            if sum(target) == 0:
                st = sorted(target)
                if st not in triplets:
                    triplets.append(st)
        return triplets


class Solution4:
    @staticmethod
    def three_sum(nums):
        comb_nums = combinations(nums, 3)
        triplets = []
        for i in comb_nums:
            j = sorted(i)
            if sum(j) == 0:
                k = list(j)
                if k not in triplets:
                    triplets.append(k)
        return triplets


class Solution5:
    @staticmethod
    def three_sum(nums):
        comb_nums = combinations(nums, 3)
        temp = [tuple(sorted(sub)) for sub in comb_nums]
        rm_dup = set(temp)
        triplets = [list(i) for i in rm_dup if sum(i) == 0]
        return triplets


class Solution6:
    @staticmethod
    def three_sum(nums):
        comb_nums = combinations(nums, 3)
        triplets = []
        for i in comb_nums:
            if sum(i) == 0:
                j = sorted(i)
                if j not in triplets:
                    triplets.append(list(j))
        return triplets


# ref: https://medium.com/jacky-life/leetcode-3sum-bb1deec8ba31
class Solution7:
    @staticmethod
    def three_sum(nums):
        nums.sort()  # from small to great
        triplets = []
        first = 0
        nums_len = len(nums)
        while first < nums_len - 2:
            if nums[first] != nums[first - 1] or first == 0:  # startup
                # left, right as indices
                target = 0 - nums[first]
                left = first + 1
                right = nums_len - 1
                while left < right:
                    if nums[left] + nums[right] > target:
                        right -= 1  # move right index 'left'
                    elif nums[left] + nums[right] < target:
                        left += 1  # move left index 'right'
                    else:
                        triplets.append([nums[first], nums[left], nums[right]])
                        while right > left:  # move right index 'left' util point at different num
                            right -= 1
                            if nums[right] != nums[right + 1]:
                                break
                        while left < right:  # move left 'right' util point at different num
                            left += 1
                            if nums[left] != nums[left - 1]:
                                break
            first += 1
        return triplets


# ref: https://leetcode.com/problems/3sum/discuss/3109452/C%2B%2B-Easiest-Beginner-friendly-Sol-oror-Set-%2B-Two-Pointer-Approach-oror-O(n2)-time-and-O(n)-space

class Solution8:
    @staticmethod
    def three_sum(nums):
        solution_set = set()
        target_sum = 0
        count = len(nums)
        nums.sort()
        for i in range(count):
            j = i + 1
            k = count - 1
            while j < k:
                nums_sum = nums[i] + nums[j] + nums[k]
                if nums_sum == target_sum:
                    solution_set.add((nums[i], nums[j], nums[k]))
                    j += 1
                    k -= 1
                elif nums_sum < target_sum:
                    j += 1
                elif nums_sum > target_sum:
                    k -= 1
        output = list(map(list, solution_set))
        return output
'''
using nums.sort() to sort nums list, from left to right, small to big
suppose count = 10

i=0, nums_sum = nums[0]+nums[1]+nums[9]
nums_sum == target, next while => nums[0]+nums[2]+nums[8]
nums_sum < target,  next while => nums[0]+nums[2]+nums[9]
nums_sum > target,  next while => nums[0]+nums[1]+nums[8]
while loop break when j == k, meaning all possible combinations are checked at i=0

next for loop
i=1, nums_sum = nums[1]+nums[2]+nums[9]
...
i=7, nums_sum = nums[7]+nums[8]+nums[9]
...
i=8, j=9, k=9, for loop break
covert set to list using map, then output as list
'''


# ref: https://leetcode.com/problems/3sum/discuss/725950/Python-5-Easy-Steps-Beats-97.4-Annotated
class Solution9:
    @staticmethod
    def three_sum(nums):
        result = set()

        # 1. split positive, negative, and count zeros
        negatives, positives = [], []
        zero_count = 0
        for num in nums:
            if num > 0:
                positives.append(num)
            elif num < 0:
                negatives.append(num)
            else:
                zero_count += 1

        # 2. create a separate set for positive and negative
        ngsets = set(negatives), set(positives)

        # 3. if zero in nums, add cases where -num + num = 0, e.g [-1,0,1]
        if zero_count > 0:
            for num in ngsets[0]:
                if -num in ngsets[1]:
                    result.add((-num, 0, num))

        # 4. add case where at least 3 zeros in nums
        if zero_count >= 3:
            result.add((0, 0, 0))

        # 5. for all pairs of negatives, check if their complement exist in Pos, [-1,-2][3]
        #    for all pairs of positives, check if their complement exist in Neg, [1,2][-3]
        for i, s in enumerate([positives, negatives]):
            for n1, n2 in combinations(s, 2):
                complement = -(n1 + n2)
                if complement in ngsets[i]:
                    result.add(tuple(sorted([n1, n2, complement])))
        result = list(map(list, list(result)))
        return result
