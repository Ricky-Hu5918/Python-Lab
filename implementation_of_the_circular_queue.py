'''
leetcode number = 622. Design Circular Queue
Design your implementation of the circular queue. The circular queue is a linear data structure in which the operations are performed based on FIFO (First In First Out) principle and the last position is connected back to the first position to make a circle. It is also called "Ring Buffer".

One of the benefits of the circular queue is that we can make use of the spaces in front of the queue. In a normal queue, once the queue becomes full, we cannot insert the next element even if there is a space in front of the queue. But using the circular queue, we can use the space to store new values.

Your implementation should support following operations:

MyCircularQueue(k): Constructor, set the size of the queue to be k.
Front: Get the front item from the queue. If the queue is empty, return -1.
Rear: Get the last item from the queue. If the queue is empty, return -1.
enQueue(value): Insert an element into the circular queue. Return true if the operation is successful.
deQueue(): Delete an element from the circular queue. Return true if the operation is successful.
isEmpty(): Checks whether the circular queue is empty or not.
isFull(): Checks whether the circular queue is full or not.

Example:

MyCircularQueue circularQueue = new MyCircularQueue(3); // set the size to be 3
circularQueue.enQueue(1);  // return true
circularQueue.enQueue(2);  // return true
circularQueue.enQueue(3);  // return true
circularQueue.enQueue(4);  // return false, the queue is full
circularQueue.Rear();  // return 3
circularQueue.isFull();  // return true
circularQueue.deQueue();  // return true
circularQueue.enQueue(4);  // return true
circularQueue.Rear();  // return 4
 
Note:

All values will be in the range of [0, 1000].
The number of operations will be in the range of [1, 1000].
Please do not use the built-in Queue library.
'''
'''思路：用一个数组和两个指针，来实现循环列表'''
class MyCircularQueue:
    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the queue to be k.
        """
        self.circularQueue = [-1 for x in range(k+1)]
        self.head = -1
        self.tail = -1
        self.size = k

    def enQueue(self, value: int) -> bool:
        """
        Insert an element into the circular queue. Return true if the operation is successful.
        """
        if (self.isFull() == True):
            return False

        if (self.isEmpty() == True):
            self.head = 0

        self.tail = (self.tail + 1) % (self.size)
        self.circularQueue[self.tail] = value
        return True

    def deQueue(self) -> bool:
        """
        Delete an element from the circular queue. Return true if the operation is successful.
        """
        if (self.isEmpty() == True):
            return False

        if (self.head == self.tail):
            self.head, self.tail = -1, -1
            return True

        self.head = (self.head + 1) % (self.size)
        return True

    def Front(self) -> int:
        """
        Get the front item from the queue.
        """
        if (self.isEmpty() == True):
            return -1

        return self.circularQueue[self.head]

    def Rear(self) -> int:
        """
        Get the last item from the queue.
        """
        if (self.isEmpty() == True):
            return -1

        return self.circularQueue[self.tail]

    def isEmpty(self) -> bool:
        """
        Checks whether the circular queue is empty or not.
        """
        return self.head == -1

    def isFull(self) -> bool:
        """
        Checks whether the circular queue is full or not.
        """
        return (self.tail + 1) % (self.size) == self.head


MyCircularQueue = MyCircularQueue(3)  #set the size to be 3
print(MyCircularQueue.enQueue(1)) #return true
print(MyCircularQueue.enQueue(2)) #return true
print(MyCircularQueue.enQueue(3)) #return true
print(MyCircularQueue.enQueue(4)) #return false, the queue is full
print(MyCircularQueue.Rear()) #return 3
print(MyCircularQueue.Front()) #return 1
print(MyCircularQueue.isFull()) #return true
print(MyCircularQueue.deQueue()) #return true
print(MyCircularQueue.enQueue(4)) #return true
print(MyCircularQueue.Rear())  #return 4
print(MyCircularQueue.deQueue()) #return true
print(MyCircularQueue.deQueue()) #return true
print(MyCircularQueue.deQueue()) #return true
print(MyCircularQueue.deQueue()) #return -1