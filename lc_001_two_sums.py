from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Finds and returns the indices of two distinct elements in the list `nums`
        whose sum equals the given `target`.

        The function assumes that exactly one valid solution exists and that
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
