# Task 1
class ArrayQueue:
    # Initialises queue as an array
    def __init__(self):
        self.queue = []
    # adds order to end of queue
    def addOrder(self, order):
        self.queue.append(order)
    # pops the element at the front of the queue
    def processOrder(self):
        if self.isEmpty():
            return None
        return self.queue.pop(0)
    # views the element at the front of the queue
    def viewNextOrder(self):
        return self.queue[0]
    # removes a specified order from the queue,
    # moves everything behind it forwards by 1 in the queue
    def cancelOrder(self, order):
        if order in self.queue:
            self.queue.remove(order)
            return True
        return False
    # checks if the queue is empty
    def isEmpty(self):
        return len(self.queue) == 0
    
"""
Task 2:
Discuss the limitations of using an array-based queue for this implementation.

An array based queue has some limitations:

To remove an order from the middle of the queue, it requires O(n) time complexity, as it has to loop through the array untill it finds the correct element. It then has to shift all elements after it.

When an order is dequeued from the front, all elements still need to be shifted forwards, requiring O(n) time complexity, instead of O(1).

As python arrays dynamically change size, sometimes when adding an element to the back of the queue, the current array size reaches capacity, so python creates a new array double the size and copies all elements across which requires O(n) time. Otherwise, adding an elemnt to the back of the queue should usually be O(1) time.
"""


"""
Task 3:
Given the identified limitations of an array-based queue, would a singly
linked list be a better alternative? Why or why not?

Dequing an element from the front can be done in O(1) time, rather then O(n)

Enqueueing an element to the back will always be in constant time (O(1)).

A linked list dynamically allocates memory unlike an array that needs to resize which prevents uneccassary memory usage.

However there are still some drawbacks.

Cancelling an order from the middle of the queue is still O(n) as we still need to search through the que to find the element

Each node in a linked list also requires memory for storage of a pointer to the next node, thus is less space efficient then an array.

Overall, a singly linked list is better then an array based queue if there are frequent enqueue and dequeue operations mainly due to not needing to shift all elements. However order cancellation time is still not improved and it also uses more memory due to the need to store pointers for each node.

"""

# Task 4:
class Node:
    # initailises a node with an order 
    # and an empty pointer to the next
    def __init__(self, order):
        self.order = order
        self.next = None

class SinglyLinkedListQueue:
    def __init__(self):
        self.front = None
        self.rear = None

    # adds an order to the back of the queue
    def addOrder(self, order):
        new_node = Node(order)
        if self.rear is None:
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node
    # returns order at front of queue and 
    # sets the front to the next node in queue
    def processOrder(self):
        if self.isEmpty():
            return None
        temp = self.front
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        return temp.order
    # returns the order at the front
    def viewNextOrder(self):
        if self.isEmpty():
            return None
        return self.front.order
    # linear search to find order, 
    # then removes it from queue,
    # and sets pointer of node infront to node 
    # behind the one that just got cancelled
    def cancelOrder(self, order):
        if self.isEmpty():
            return False
        temp = self.front
        prev = None
        while temp is not None:
            if temp.order == order:
                if prev is None:
                    self.front = temp.next
                else:
                    prev.next = temp.next
                if temp == self.rear:
                    self.rear = prev
                return True
            prev = temp
            temp = temp.next
        return False
    # Checks if queue is empty
    def isEmpty(self):
        return self.front is None
    
"""
Task 4:
Suppose that each order in the system has a direct reference, meaning we
can instantly locate any specific order without searching through the queue.
Would a doubly linked list improve upon a singly linked list in this case?
Why or why not?
##
Yes a doubly linked list would improve performance for order cancellation. 
This is because it changes this operation to constant time O(1), rather then O(n) like it is in an array or singly linked list.
The reason for this is that each order now has a direct reference and therefore we do not have to traverse the array to find it.
However, a doubly linked list will require more memoruy usage as each node stores an extra pointer to its previous element.
##
##
Analyze and compare all three implementations (array-based queue, singly
linked list, and doubly linked list) based on:
■ Time complexity for canceling an order.
■ Space complexity and memory usage.
■ Situations where each implementation is preferred
##
Time complexity:
Array: O(n) as it has to search for the element and then shift all elemnts after it.
Singly Linked List: O(n) as it requires traversal through the list.
Doubly Linked List: O(1) as there is a direct reference to the order so no traversal is required.

Space complexity:
Array: O(n), This is the most memory efficient as there are no extra pointers stored, the only drawback is the dynamically changing array sizes which can be sometimes over allocated.
Singly Linked List: O(n), This is the second most efficient as it requires storage of a pointer for each node, there is no over allocation however.
Doubly Linked List: O(n), This is the least memory efficiend as it requires storage of two pointers for each node, using the most memory per order, there is no over allocation however.

An array based queue implementation is best used in a situation where memory is very limited and order cancellations are rare.
A singly linked list is best used when orders are frequently being added and dequed.
A doubly linked list is best used when orders within the middle of the queue need to cancelled frequently and each order has a direct reference.
"""
        
class DllNode:
    """
    Node in a doubly linked list.
    Attributes:
        order: The value stored in this node.
        prev:  Reference to the previous node.
        next:  Reference to the next node.
    """
    def __init__(self, order):
        self.order = order
        self.prev = None
        self.next = None

class DoublyLinkedListQueue:
    """
    Queue implemented via a doubly linked list.
    Operations:
      - addOrder(order)       : O(1), returns a direct node reference
      - processOrder()        : O(1), removes and returns front order
      - viewNextOrder()       : O(1), peeks at the front order
      - cancelOrder(node)     : O(1), removes given node reference
      - isEmpty()             : O(1), checks empty
    """
    def __init__(self):
        self.front = None
        self.rear = None

    def addOrder(self, order):
        """Add `order` to the back of the queue; return node reference."""
        new_node = DllNode(order)
        if not self.front:            # empty queue
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            new_node.prev = self.rear
            self.rear = new_node
        return new_node

    def processOrder(self):
        """Remove and return the front order, or None if empty."""
        if self.isEmpty():
            return None
        node = self.front
        self.front = node.next
        if self.front:
            self.front.prev = None
        else:
            self.rear = None       # queue is now empty
        return node.order

    def viewNextOrder(self):
        """Return the front order without removing it, or None if empty."""
        return self.front.order if not self.isEmpty() else None

    def cancelOrder(self, node):
        """
        Remove the node referenced by `node` in O(1) time.
        Assumes `node` is currently in this queue.
        """
        # Re-link prev and next around node
        if node.prev:
            node.prev.next = node.next
        else:
            self.front = node.next

        if node.next:
            node.next.prev = node.prev
        else:
            self.rear = node.prev

        # Clear node's pointers (optional cleanup)
        node.prev = node.next = None
        return True

    def isEmpty(self):
        """Return True if queue is empty."""
        return self.front is None






import time
import random


def benchmark_queues(N):
    data = list(range(N))
    random.shuffle(data)

    # Process Order benchmark
    arrq = ArrayQueue()
    for x in data:
        arrq.addOrder(x)
    start = time.perf_counter()
    for _ in range(N):
        arrq.processOrder()
    time_arr_process = time.perf_counter() - start

    llq = SinglyLinkedListQueue()
    for x in data:
        llq.addOrder(x)
    start = time.perf_counter()
    for _ in range(N):
        llq.processOrder()
    time_ll_process = time.perf_counter() - start

    dllq = DoublyLinkedListQueue()
    for x in data:
        dllq.addOrder(x)
    start = time.perf_counter()
    for _ in range(N):
        dllq.processOrder()
    time_dll_process = time.perf_counter() - start

    # View Next Order benchmark
    arrq = ArrayQueue()
    for x in data:
        arrq.addOrder(x)
    start = time.perf_counter()
    for _ in range(N):
        arrq.viewNextOrder()
    time_arr_view = time.perf_counter() - start

    llq = SinglyLinkedListQueue()
    for x in data:
        llq.addOrder(x)
    start = time.perf_counter()
    for _ in range(N):
        llq.viewNextOrder()
    time_ll_view = time.perf_counter() - start

    dllq = DoublyLinkedListQueue()
    for x in data:
        dllq.addOrder(x)
    start = time.perf_counter()
    for _ in range(N):
        dllq.viewNextOrder()
    time_dll_view = time.perf_counter() - start

    # Cancel Order benchmark
    arrq = ArrayQueue()
    for x in data:
        arrq.addOrder(x)
    start = time.perf_counter()
    for x in data:
        arrq.cancelOrder(x)
    time_arr_cancel = time.perf_counter() - start

    llq = SinglyLinkedListQueue()
    for x in data:
        llq.addOrder(x)
    start = time.perf_counter()
    for x in data:
        llq.cancelOrder(x)
    time_ll_cancel = time.perf_counter() - start

    dllq = DoublyLinkedListQueue()
    nodes = [dllq.addOrder(x) for x in data]
    start = time.perf_counter()
    for node in nodes:
        dllq.cancelOrder(node)
    time_dll_cancel = time.perf_counter() - start

    # isEmpty benchmark
    arrq = ArrayQueue()
    for x in data:
        arrq.addOrder(x)
    start = time.perf_counter()
    for _ in range(N):
        arrq.isEmpty()
    time_arr_empty = time.perf_counter() - start

    llq = SinglyLinkedListQueue()
    for x in data:
        llq.addOrder(x)
    start = time.perf_counter()
    for _ in range(N):
        llq.isEmpty()
    time_ll_empty = time.perf_counter() - start

    dllq = DoublyLinkedListQueue()
    for x in data:
        dllq.addOrder(x)
    start = time.perf_counter()
    for _ in range(N):
        dllq.isEmpty()
    time_dll_empty = time.perf_counter() - start

    # Print results
    print(f"{'Operation':<20}{'Array':>12}{'SinglyLL':>12}{'DoublyLL':>12}")
    print("-" * 56)
    print(f"{'processOrder':<20}{time_arr_process:12.8f}{time_ll_process:12.8f}{time_dll_process:12.8f}")
    print(f"{'viewNextOrder':<20}{time_arr_view:12.8f}{time_ll_view:12.8f}{time_dll_view:12.8f}")
    print(f"{'cancelOrder':<20}{time_arr_cancel:12.8f}{time_ll_cancel:12.8f}{time_dll_cancel:12.8f}")
    print(f"{'isEmpty':<20}{time_arr_empty:12.8f}{time_ll_empty:12.8f}{time_dll_empty:12.8f}")

if __name__ == "__main__":
    benchmark_queues(10000)

import sys
import random

def mem_array_queue(N):
    q = ArrayQueue()
    for i in range(N):
        q.addOrder(i)
    return sys.getsizeof(q.queue)

def mem_singly_llq(N):
    q = SinglyLinkedListQueue()
    for i in range(N):
        q.addOrder(i)
    total = 0
    node = q.front
    while node:
        total += sys.getsizeof(node)         # the Node object
        total += sys.getsizeof(node.__dict__) # its attribute dict
        node = node.next
    return total

def mem_doubly_llq(N):
    q = DoublyLinkedListQueue()
    for i in range(N):
        q.addOrder(i)
    total = 0
    node = q.front
    while node:
        total += sys.getsizeof(node)
        total += sys.getsizeof(node.__dict__)
        node = node.next
    return total

if __name__ == "__main__":
    N = 10_000
    print(f"ArrayQueue container size:        {mem_array_queue(N):>8d} bytes")
    print(f"SinglyLinkedListQueue total node:  {mem_singly_llq(N):>8d} bytes")
    print(f"DoublyLinkedListQueue total node:  {mem_doubly_llq(N):>8d} bytes")
