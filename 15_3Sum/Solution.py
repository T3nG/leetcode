from itertools import combinations


class Solution:
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
            target = [nums[comb_lst[i][0]], nums[comb_lst[i][1]], nums[comb_lst[i][2]]]
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
            target = [comb_nums[i][0], comb_nums[i][1], comb_nums[i][2]]
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
        triplets = []
        [triplets.append(list(i)) for i in rm_dup if sum(i) == 0]
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


class Solution7:
    @staticmethod
    def three_sum(nums):
        nums.sort()  # 由小到大排序
        triplets = []
        first = 0
        nums_len = len(nums)
        while first < nums_len - 2:
            if nums[first] != nums[first - 1] or first == 0:  # 解決 first重複, 及初始化
                # left, right 為指標
                target = 0 - nums[first]
                left = first + 1
                right = nums_len - 1
                while left < right:
                    if nums[left] + nums[right] > target:
                        right -= 1  # 正值過大, right往左移
                    elif nums[left] + nums[right] < target:
                        left += 1  # 負值過小, left往右移
                    else:
                        triplets.append([nums[first], nums[left], nums[right]])
                        while right > left:  # right往左移, 若所指數字相等, 則繼續左移
                            right -= 1
                            if nums[right] != nums[right + 1]:
                                break
                        while left < right:  # left往右移, 若所指數字相等, 則繼續右移
                            left += 1
                            if nums[left] != nums[left - 1]:
                                break
            first += 1
        return triplets
