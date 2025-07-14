from typing import List


class Solution:
    def two_num(self, nums: List[int], target: int) -> List[int]:
        print(f"The target is {target}")
        print(f"The nubbers array is:")
        dict_nums = dict(enumerate(nums))
        sum = 0

        for index_a, num_a in dict_nums.items():
            for index_b, num_b in dict_nums.items():
                if index_a == index_b:
                    continue
                sum = dict_nums[index_a] + dict_nums[index_b]
                if sum == target:
                    return [index_a, index_b]






