def maxProduct(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return -1
        current_max = nums[0]
        current_min = nums[0]
        final_max = nums[0]
        for i in range(1, len(nums)):
            # Need temp because current_max might change
            temp = current_max
            # nums[i] is what makes sure you have continguous sub-array
            # if nums[i] is chose in the max() or min() function, that resets where the products are calculated from
            # anything before index i will not be included in the product calculation
            current_max = max(nums[i], nums[i] * current_min, nums[i] * current_max)
            current_min = min(nums[i], nums[i] * current_min, nums[i] * temp)
            final_max = max(current_max, final_max)
        return final_max

# Example run through
#               2 3 -2  4
# current_max = 2 6 -2  4
# current_min = 2 3 -12 -48
# final_max =   2 6 6   6
