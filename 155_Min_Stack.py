'''
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.
push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.

Example:
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin();   --> Returns -3.
minStack.pop();
minStack.top();      --> Returns 0.
minStack.getMin();   --> Returns -2.
'''
'''#1: normal way, using a list'''
class MinStack1:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.minstack = []
        self.stacklen = 0
        self.minelement = -1

    def push(self, x: int) -> None:
        self.minstack.append(x)
        self.stacklen += 1

    def pop(self) -> None:
        if (not self.isEmpty()):
            self.minstack.pop()
            self.stacklen -= 1

    def top(self) -> int:
        if (not self.isEmpty()):
            return self.minstack[self.stacklen - 1]
        else:
            return -1

    def getMin(self) -> int:
        if (self.isEmpty()):
            return -1

        self.minelement = self.minstack[0]
        for i in range(1, self.stacklen):
            if (self.minstack[i] < self.minelement):
                self.minelement = self.minstack[i]

        return self.minelement

    def isEmpty(self) -> bool:
        return (self.stacklen == 0)

'''#2: using two lists'''
class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.min_stack = []
        self.helper_stack = []

    def push(self, x: int) -> None:
        self.min_stack.append(x)
        self.helper_stack.append(x)

    def pop(self) -> None:
        if (self.min_stack):
            self.min_stack.pop()
            self.helper_stack.pop()

    def top(self) -> int:
        if (self.min_stack):
            return self.min_stack[-1]
        else:
            return -1

    def getMin(self) -> int: #don't use sort() method, because it will modify the orginal list
        return sorted(self.helper_stack)[0]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
m_stack = MinStack()
print(m_stack.push(2), m_stack.min_stack)
print(m_stack.push(0), m_stack.min_stack)
print(m_stack.push(-3), m_stack.min_stack)
print(m_stack.getMin(), m_stack.helper_stack)
print(m_stack.pop(), m_stack.min_stack)
print(m_stack.top())
print(m_stack.getMin(), m_stack.helper_stack)