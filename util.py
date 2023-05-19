"""
This file contains implementations of different data structures.

"""

import heapq


class Stack:
    # Class for Stack which implement LIFO.
    def __init__(self):
        self.list = []
    
    def push(self, item):
        self.list.append(item)
    
    def pop(self):
        return self.list.pop()
    
    def isEmpty(self):
        return len(self.list)==0


class Queue:
    # Class for Queue which implement FIFO
    def __init__(self):
        self.list = []

    def push(self, item):
        self.list.append(item)
    
    def pop(self):
        return self.list.pop(0)

    def isEmpty(self):
        return len(self.list)==0


class PriorityQueue:
    # class for Queue which prioritize elements by its value
    def __init__(self):
        self.list = []

    def push(self, item):
        heapq.heappush(self.list, item)

    def pop(self):
        return(heapq.heappop(self.list)) 
