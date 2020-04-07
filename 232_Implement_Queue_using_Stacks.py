'''
Implement the following operations of a queue using stacks.

push(x) -- Push element x to the back of queue.
pop() -- Removes the element from in front of queue.
peek() -- Get the front element.
empty() -- Return whether the queue is empty.

Example:
MyQueue queue = new MyQueue();
queue.push(1);
queue.push(2);
queue.peek();  // returns 1
queue.pop();   // returns 1
queue.empty(); // returns false

Notes:
You must use only standard operations of a stack -- which means only push to top, peek/pop from top, size, and is empty operations are valid.
Depending on your language, stack may not be supported natively. You may simulate a stack by using a list or deque (double-ended queue), as long as you use only standard operations of a stack.
You may assume that all operations are valid (for example, no pop or peek operations will be called on an empty queue).
'''

class MyQueue1:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack = []
        self.size = 0


    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.size += 1
        return self.stack.append(x)

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        if (not self.empty()):
            self.size -= 1
            return self.stack.pop(0)
        else:
            return -1

    def peek(self) -> int:
        """
        Get the front element.
        """
        if (not self.empty()):
            return self.stack[0]
        else:
            return -1

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return (self.size == 0)


mydeque = MyQueue1()
print(mydeque.push(1))
print(mydeque.push(2))
print(mydeque.peek())
print(mydeque.pop())
print(mydeque.empty())