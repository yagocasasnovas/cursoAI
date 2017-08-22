import sys
import math
import timeit
import resource
import heapq

class PriorityQueue:
    def  __init__(self):

        self.heap = []
        self.count = 0

    def push(self, item, priority):
        entry = (priority, self.count, item)
        heapq.heappush(self.heap, entry)
        self.count = self.count + 1

    def pop(self):
        (_, _, item) = heapq.heappop(self.heap)
        """self.count = self.count - 1"""
        return item

    def isEmpty(self):
        return len(self.heap) == 0

    def update(self, item, priority):
        
        
        for index, (p, c, i) in enumerate(self.heap):
            if i == item:
                if p <= priority:
                    break
                del self.heap[index]
                self.heap.append((priority, c, item))
                heapq.heapify(self.heap)
                break
        else:
            self.push(item, priority)
            


class PriorityQueue1:



    def  __init__(self):
        self.heap = []
        self.count = 0

    def push(self, item, priority):
        entry = (priority, item)
        heapq.heappush(self.heap, entry)
        self.count = self.count + 1

    def pop(self):
        (_, item) = heapq.heappop(self.heap)
        self.count = self.count - 1
        return item

    def isEmpty(self):
        return len(self.heap) == 0

    def update(self, id, priority):
        
        
        for index, (p, i) in enumerate(self.heap):
            print 'id: ' + str(id) + ' index: ' + str(index) + ' p: ' + str(p) + ' i: ' + str(i)
            
            
            if i[1] == id:
                print 'h'
                if p <= priority:
                    break
                del self.heap[index]
                self.heap.append((priority, i))
                heapq.heapify(self.heap)
                break
         
            
            
            
a = PriorityQueue1()

a.push((1,1,'a'),4)
a.push((1,2,'c'),5)
a.push((2,1,'d'),6)

a.update(2,3)

print '1'
print a.pop()
print '2'
print a.pop()
print '3'
print a.pop()
