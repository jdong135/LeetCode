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
            # if nums[i] is chosen in the max() function, that resets where the products are calculated from
            # anything before index i will not be included in the product calculation
            current_max = max(nums[i], nums[i] * current_min, nums[i] * current_max)
            current_min = min(nums[i], nums[i] * current_min, nums[i] * temp)
            final_max = max(current_max, final_max)
        return final_max

# Example run through
#               2 3 -2  4    -2
# current_max = 2 6 -2  4    96
# current_min = 2 3 -12 -48  -8
# final_max =   2 6 6   6    96

# current_min calculates the minimum possible product up to and including index i. So when i = 1, [2,3] has a minimum product of 3.
# current_max calculates the maximum possible product up to and including index i. So when i = 2, [2,3,-2] has a max product of -2
# because including 2 and 3 would make the product more negative.
