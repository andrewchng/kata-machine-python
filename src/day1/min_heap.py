import math


class min_heap():
 
    def __init__(self, length = 0):
        self.length = length
        self.data = []

    def insert(self, value: int):
        self.data.append(value)
        self.heapify_up(self.length)
        #why account for length after heapify?
        self.length+=1

    def delete(self) -> int:
        if self.length == 0 :
            return -1
        deleted = self.data[0]
        if self.length == 1 : 
            self.length-=1
            self.data=[]
            return deleted
        
        #why can this work if i just swapping?
        # self.data[0], self.data[self.length-1] =  self.data[0], self.data[self.length-1]
        self.data[0] = self.data[self.length-1]
        self.length-=1
        self.heapify_down(0)
        return deleted

    def heapify_up(self, idx):
        if idx == 0 :
            return
        parentIdx = self.parent(idx) 
        if self.data[parentIdx] > self.data[idx]:
            self.data[parentIdx], self.data[idx] = self.data[idx], self.data[parentIdx]
            self.heapify_up(parentIdx)

    def heapify_down(self, idx):
        leftIdx = self.left_child(idx)
        rightIdx = self.right_child(idx)
        if idx >= self.length or leftIdx >= self.length:
            return
        leftV = self.data[leftIdx]
        rightV = self.data[rightIdx]
        currV = self.data[idx]
        if leftV < currV and leftV < rightV:
            self.data[leftIdx], self.data[idx] = self.data[idx], self.data[leftIdx]
            self.heapify_down(leftIdx)
        if rightV < currV and rightV < leftV:
            self.data[rightIdx], self.data[idx] = self.data[idx], self.data[rightIdx]
            self.heapify_down(rightIdx)
    
    def parent(self, idx: int):
        return math.floor((idx-1)/2)
    
    def left_child(self, idx:int):
        return 2*idx+1
    
    def right_child(self, idx:int):
        return 2*idx+2