from typing import List


# https://www.youtube.com/watch?v=LeRU6irRoW0
class Solution:
        def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
                # soution 1 :  DP
                # time complexity - O(N^2)
                # Sapce Complexity - O(N^2)
                nums.sort()
                res = []
                dp = [[n] for n in nums]
                for i in reversed(range(len(nums))):
                        for j in range(i + 1, len(nums)):
                                if nums[j] % nums[i] == 0:
                                        tmp = [nums[i]] + dp[j]
                                        if len(dp[i]) < len(tmp):
                                                dp[i] = tmp

                        res = dp[i] if len(dp[i]) > len(res) else res

                return res

                # solution 1: Recursion +Caching
                # time complexity - O(N^2)
                # Sapce Complexity - O(N)

                nums.sort()
                cache = {}

                def dfs(i):
                        if i == len(nums):
                                return []
                        if i in cache: return cache[i]

                        res = [nums[i]]
                        for j in range(i + 1, len(nums)):
                                if nums[j] % nums[i] == 0:
                                        tmp = [nums[i]] + dfs(j)  # O32(1,2,4,8,16....2^32)
                                        if len(tmp) > len(res):
                                                res = tmp
                        cache[i] = res
                        return res

                res = []
                for i in range(len(nums)):
                        tmp = dfs(i)
                        if len(tmp) > len(res):
                                res = tmp
                return res


s = Solution()
nums = [1,2,5,15,45]
squares = s.largestDivisibleSubset(nums)
print(squares)