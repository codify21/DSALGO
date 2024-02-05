class Solution:
    def evalRPN(self, tokens):
        integers = [str(i) for i in range(-201,201)]
        i = 0
        while i < len(tokens):
            if tokens[i] not in integers:
                result = int(eval(tokens[i - 2] + tokens[i] + tokens[i - 1]))
                tokens[i - 2:i + 1] = [str(result)]
                i = i - 2
            i += 1
        return tokens[0]
    #Solution 2
    def evalRPN(self, tokens):
        stack = []
        for num in tokens:
            if num == '+':
                stack.append(stack.pop() + stack.pop())
            elif num == '-':
                a, b = stack.pop(), stack.pop()
                stack.append(b - a)
            elif num == '*':
                stack.append(stack.pop() * stack.pop())
            elif num == '/':
                a, b = stack.pop(), stack.pop()
                # if using b//a, once the num is neg, it would minus 1 more than int(b/a)
                # int取整
                stack.append(int(b / a))

            # Put result into stack
            else:
                stack.append(int(num))
        return stack[0]


s = Solution()
reverse = s.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"])
print(reverse)