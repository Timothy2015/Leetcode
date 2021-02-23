# https://leetcode-cn.com/problems/min-stack-lcci/

## 双栈模拟：
# * 主栈：stack
# * 辅栈：minStack
class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.minStack = [] # 保存“历史的（含重复的）”最小值

    def push(self, x: int) -> None:
        # 添加元素，需要更新min
        if not self.minStack:
            self.minStack.append(x)
        elif x <= self.minStack[-1]:
            self.minStack.append(x)
        """
        注意：重复的最小值也需要保存进来，因为删除的时候会毫不犹豫地删除
        ["MinStack","push","push","push","getMin","pop","getMin"]
        [[],[0],[1],[0],[],[],[]]
        """
        self.stack.append(x)

    def pop(self) -> None:
        # 栈不空，才出栈
        if self.stack:
            delete = self.stack.pop()
        # 删除元素，也需要更新min
        if delete == self.minStack[-1]:
            self.minStack.pop()

    def top(self) -> int:
        if len(self.minStack) > 0:
            return self.stack[-1]

    def getMin(self) -> int:
        # 最小栈不空，返回栈顶最小值
        if self.minStack:
            return self.minStack[-1]
        else:
            return None

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()


# 一个列表模仿栈，只有一个列表不行……
class MinStack:
    def __init__(self):
        """
        initialize your data structure here.
        """
        # minStack[0]保存最小值，初始栈长度为1
        self.minStack = [sys.maxsize]

    def push(self, x: int) -> None:
        # 添加元素，需要更新min
        if x < self.minStack[0]:
            self.minStack[0] = x
        self.minStack.append(x)

    def pop(self) -> None:
        # 栈不空，才出栈
        if len(self.minStack) > 1:
            delete = self.minStack.pop()
        # 删除元素，也需要更新min
        if delete == minStack[0]:
            """
            # 然后写不下去了……（发现需要两个栈）
            """

    def top(self) -> int:
        if len(self.minStack) > 1:
            return self.minStack[-1]

    def getMin(self) -> int:
        return self.minStack[0]
