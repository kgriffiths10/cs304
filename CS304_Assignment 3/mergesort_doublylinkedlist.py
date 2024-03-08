import random
import time
import matplotlib.pyplot as plt

"""
Doubly Linked List Merge Sort Implementation
"""
class Node:
    def __init__(self, element):
        self.element = element
        self.next = None
        self.prev = None

class DoublyLinkedBase:
    # Empty Doubly Linked List
    def __init__(self):
        self.head = None
        self.size = 0

    def __len__(self):
        # Return the number of elements in the list.
        return self.size

    def is_empty(self):
        # Return true if list is empty.
        return self.size == 0

    # Seperate into two equal lists
    def seperate(self, tempHead):
        fast = slow = tempHead
        while (True):
            if fast.next is None:
                break
            if fast.next.next is None:
                break
            fast = fast.next.next
            slow = slow.next

        temp = slow.next
        slow.next = None
        return temp

    # Inserts new node at beginning of list
    def insert_node(self, new_element):
        # New data in allocated node
        new_node = Node(new_element)
        # Next becomes head
        new_node.next = self.head
        # Prev of head node becomes new_node
        if self.head is not None:
            self.head.prev = new_node
        # Head points to new_node
        self.head = new_node

    # Merge two linked list
    def merge(self, first_list, second_list):
        a = first_list
        b = second_list
        # Empty first list link
        if a is None:
            return b
        # Empty second list link
        if b is None:
            return a

        # Pick the smaller value
        if a.element < b.element:
            a.next = self.merge(a.next, b)
            a.next.prev = a
            a.prev = None
            return a
        else:
            b.next = self.merge(a, b.next)
            b.next.prev = b
            b.prev = None
            return b

    # Function to do merge sort
    def merge_sort(self, tempHead):
        if tempHead.next is None:
            return tempHead
        if tempHead is None:
            return tempHead

        b = self.seperate(tempHead)

        # Recursion (left and right halves)
        tempHead = self.merge_sort(tempHead)
        b = self.merge_sort(b)

        # Merge the two sorted halves
        return self.merge(tempHead, b)


"""
Array Merge Sort Implementation
"""
def merge2(A,p,q,r):  
    n1 = q - p + 1
    n2 = r - q
  
    L = []
    R = []
    for i in range(n1):
        L.append(A[p+i])
    for i in range(n2):
        R.append(A[q+i+1])
    L.append(99999)
    R.append(99999)  
    
    i=0
    j=0
    for k in range(p,r+1):
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1 
    
def mergesort(A,p,r):
    if p < r:
        q = (p + r) // 2
        mergesort(A,p,q)
        mergesort(A,q+1,r)
        merge2(A,p,q,r)
        
        
"""
Plotting
"""
import time
import numpy as np
times = []
times2 = []
doublelist = DoublyLinkedBase()

for i in range(10,150,10):      # 1000 was too large, therefore 150 was used
    start_t = time.time()
    mergesort(np.arange(0,i),0,i-1)
    times2.append(time.time() - start_t)
    for j in range (0,i):
        doublelist.insert_node(j)
    start_t = time.time()
    doublelist.head = doublelist.merge_sort(doublelist.head)
    times.append(time.time() - start_t)


import matplotlib.pyplot as plt

plt.plot(times, label = 'double list')
plt.plot(times2, label = 'array')
plt.legend()