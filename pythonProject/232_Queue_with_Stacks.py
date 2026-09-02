# https://www.youtube.com/watch?v=eanwa3ht3YQ
class MyQueue:

    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, x: int) -> None:
        self.stack1.append(x)

    def pop(self) -> int:
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2.pop()

    def peek(self) -> int:
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2[-1]

    def empty(self) -> bool:
        return (len(self.stack1) + len(self.stack2) == 0)

# class MyQueue:

#     def __init__(self):
#         self.queue=[]

#     def push(self, x: int) -> None:
#         self.queue.append(x)

#     def pop(self) -> int:
#         data = self.queue[0]
#         del self.queue[0]
#         return data

#     def peek(self) -> int:
#         return self.queue[0]

#     def empty(self) -> bool:
#         return self.queue==[]


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()