
# https://leetcode.com/problems/remove-duplicates-from-sorted-array/?page=1&search=parenthesis
from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 0 or len(nums) == 1:
            return len(nums)
        slow, fast = 0, 0

        while fast < len(nums):
            if nums[slow] != nums[fast]:
                slow = slow + 1
                nums[slow] = nums[fast]

            fast = fast + 1

        return slow + 1


nums = [0,0,1,1,1,2,2,3,3,4]

sol = Solution()
res = sol.removeDuplicates(nums)
print(nums[:res])



