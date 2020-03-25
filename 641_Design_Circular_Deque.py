'''
Design your implementation of the circular double-ended queue (deque).
Your implementation should support following operations:

MyCircularDeque(k): Constructor, set the size of the deque to be k.
insertFront(): Adds an item at the front of Deque. Return true if the operation is successful.
insertLast(): Adds an item at the rear of Deque. Return true if the operation is successful.
deleteFront(): Deletes an item from the front of Deque. Return true if the operation is successful.
deleteLast(): Deletes an item from the rear of Deque. Return true if the operation is successful.
getFront(): Gets the front item from the Deque. If the deque is empty, return -1.
getRear(): Gets the last item from Deque. If the deque is empty, return -1.
isEmpty(): Checks whether Deque is empty or not. 
isFull(): Checks whether Deque is full or not.

Example:
MyCircularDeque circularDeque = new MycircularDeque(3); // set the size to be 3
circularDeque.insertLast(1);			// return true
circularDeque.insertLast(2);			// return true
circularDeque.insertFront(3);			// return true
circularDeque.insertFront(4);			// return false, the queue is full
circularDeque.getRear();  			// return 2
circularDeque.isFull();				// return true
circularDeque.deleteLast();			// return true
circularDeque.insertFront(4);			// return true
circularDeque.getFront();			// return 4

Note:
All values will be in the range of [0, 1000].
The number of operations will be in the range of [1, 1000].
Please do not use the built-in Deque library.
'''
'''#1: 还是使用一个数组和两个指针实现循环双端队列，跟循环队列类似（leetcode num = 622）'''
class MyCircularDeque:

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the deque to be k.
        """
        self.circularDeque = [-1 for x in range(k)]
        self.head = -1
        self.tail = -1
        self.size = k

    def insertFront(self, value: int) -> bool:
        """
        Adds an item at the front of Deque. Return true if the operation is successful.
        """
        if (self.isFull() == True):
            return False

        if (self.isEmpty() == True):
            self.tail = 0
            self.head = 0
        else:
            self.head = (self.head - 1) % (self.size)

        self.circularDeque[self.head] = value
        return True

    def insertLast(self, value: int) -> bool:
        """
        Adds an item at the rear of Deque. Return true if the operation is successful.
        """
        if (self.isFull() == True):
            return False

        if (self.isEmpty() == True):
            self.head = 0

        self.tail = (self.tail + 1) % (self.size)
        self.circularDeque[self.tail] = value
        return True

    def deleteFront(self) -> bool:
        """
        Deletes an item from the front of Deque. Return true if the operation is successful.
        """
        if (self.isEmpty() == True):
            return False

        if (self.head == self.tail):
            self.head, self.tail = -1, -1
            return True

        self.head = (self.head + 1) % (self.size)
        print('deleteFront', self.head, self.tail)
        return True

    def deleteLast(self) -> bool:
        """
        Deletes an item from the rear of Deque. Return true if the operation is successful.
        """
        if (self.isEmpty() == True):
            return False

        if (self.head == self.tail):
            self.head, self.tail = -1, -1
            return True

        self.tail = (self.tail - 1) % (self.size)
        print('deleteLast', self.head, self.tail)
        return True

    def getFront(self) -> int:
        """
        Get the front item from the deque.
        """
        if (self.isEmpty() == True):
            return -1

        return self.circularDeque[self.head]

    def getRear(self) -> int:
        """
        Get the last item from the deque.
        """
        if (self.isEmpty() == True):
            return -1

        return self.circularDeque[self.tail]

    def isEmpty(self) -> bool:
        """
        Checks whether the circular deque is empty or not.
        """
        return (self.head == -1)

    def isFull(self) -> bool:
        """
        Checks whether the circular deque is full or not.
        """
        # print('isFull.tail', self.tail, self.head)
        return ((self.tail + 1) % (self.size)) == self.head

# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()

dq = MyCircularDeque(3)
print(dq.insertFront(1), dq.circularDeque)
print(dq.insertFront(2), dq.circularDeque)
print(dq.insertFront(3), dq.circularDeque)
print(dq.insertFront(4), dq.circularDeque)
print(dq.getFront())
print(dq.getRear())
print(dq.deleteFront(), dq.circularDeque)
print(dq.deleteLast(), dq.circularDeque)
print(dq.getFront())
print(dq.getRear())
print(dq.insertFront(4), dq.circularDeque)
