# https://www.youtube.com/watch?v=HLZLwjzIVGo
# breaking the no. 12 to 4 + dp[8] -- giving 3 output
class Solution:
    def numSquares(self, n: int) -> int:
        dp = [n] * (n + 1)
        dp[0] = 0

        for target in range(1, n + 1):
            for s in range(1, target + 1):
                square = s * s
                if target - square < 0:
                    break
                dp[target] = min(dp[target], 1 + dp[target - square])

        return dp[n]


s = Solution()
nums = [1,3,-1,-3,5,3,6,7]
squares = s.numSquares(12)
print(squares)