from typing import List
# https://www.youtube.com/watch?v=DfljaUwZsOk
from collections import deque


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq = deque()  # storing index (not values)
        l, r = 0, 0
        res = []
        while r < len(nums):
            # pop smaller values from queue
            while dq and nums[dq[-1]] < nums[r]:
                dq.pop()
            dq.append(r)
            # Edge case: remove left val from window
            # when window size increases
            if l > dq[0]:
                dq.popleft()
            # to append max output value in window
            if r + 1 >= k:  # r-l+1 is not correct
                res.append(nums[dq[0]])
                l = l + 1
            r = r + 1
        return res


s = Solution()
nums = [1,3,-1,-3,5,3,6,7]
reverse = s.maxSlidingWindow(nums,3)
print(reverse)