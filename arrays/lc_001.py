# Two Sums Problem


from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Finds and returns the indices of two distinct elements in the list `nums`
        whose sum equals the given `target`.

        The fu nction assumes that exactly one valid solution exists and that
        the same element cannot be used more than once.

        Args:
            nums (List[int]): A list of integers.
            target (int): The target sum.

        Returns:
            List[int]: A list containing the indices of the two elements
            that add up to the target.
        """
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
                
# Optimized version using dictionary


# This is the optimized version of the two sum problem
# It uses a hash map or lets say dictionary
# First we find the compliment (meaning target - nums [i])
# After that we add key value pair to the dictionary
# They we are adding them is by storing the numbers in nums as the key of the pairs and the index value as value in the dict
# so we have something like this at the end {2: 0, 7: 1, 11: 2, 19: 3}
# now when we have that specific element in our dictionary we go into the if statement
# and return the current index number of nums list and the value(index) of the dictionary 
# where the specific number matched with the key 


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        
        for i,num in enumerate(nums):
            compliment=target-num
            if compliment in seen:
                return[i,seen[compliment]]
            
            seen[num]=i
            
            

nums=[2,7,11,19,15]
target=22
sol = Solution()
result = sol.twoSum(nums, target)
print(result)