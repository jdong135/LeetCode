def maxProduct(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return -1
        current_max = nums[0]
        current_min = nums[0]
        final_max = nums[0]
        for i in range(1, len(nums)):
            temp = current_max
            current_max = max(nums[i], nums[i] * current_min, nums[i] * current_max)
            current_min = min(nums[i], nums[i] * current_min, nums[i] * temp)
            final_max = max(current_max, final_max)
        return final_max
