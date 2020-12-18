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

                
# If the list is already sorted, you can use the following appraoch with two pointers
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1
        while left < right:
            sum = numbers[left] + numbers[right]
            if sum == target:
                return [left+1,right+1]
            elif sum < target:
                left += 1
            else:
                right -= 1
