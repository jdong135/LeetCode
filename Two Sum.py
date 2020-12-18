class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # dict: value: index
        nums_dict = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in nums_dict.keys():
                return [i, nums_dict[complement]]
            else:
                nums_dict[nums[i]] = i
