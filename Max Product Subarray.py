def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_prod = 1
        min_prod = 1
        result = nums[0]
        for num in nums:
            if num == 0:
                result = max(0, result)
                max_prod = 1
                min_prod = 1
            else:
                temp = max_prod
                max_prod = max(num, num * max_prod, num * min_prod)
                min_prod = min(num, num * min_prod, num * temp)
                result = max(max_prod, result)
        return result

# At all points in array, we keep track of max possible product and min possible product. That way, if we encounter a negative number, we may use the the min possible product to find the new max. When we encounter a 0, we want to reset min/max product to 1, so we don't just have 0s through the rest of the array. 
