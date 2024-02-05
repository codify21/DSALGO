class Solution:
    def longestValidParentheses(self, s: str) -> int:

        max_so_far = 0
        stack = [-1]

        for i, c in enumerate(s):
            if c == "(":
                stack.append(i)
            else:
                stack.pop()
                if not stack:
                    stack.append(i)
                else:
                    max_so_far = max(max_so_far, i - stack[-1])

        return max_so_far

s = Solution()
reverse = s.longestValidParentheses(")()())()()()(")
print(reverse)