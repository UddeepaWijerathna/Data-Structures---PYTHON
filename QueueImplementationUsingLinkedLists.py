#implementation of queue using linked lists

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None
        
class Queue:

    def __init__(self):
        self.length=0
        self.head=None
        self.tail=None

    def enqueue(self,item):
        newNode=Node(item)
        newNode.next=None
        self.length=self.length+1
        if self.head== None:
            self.head=newNode
            self.tail=newNode
        else:
            self.tail.next=newNode
            newNode.prev=self.tail
            self.tail=newNode

    def dequeue (self):
        val=self.head.data
        self.head=self.head.next
        self.length=self.length-1
        return val
        
        
q=Queue()
q.enqueue("2")
q.enqueue("5")
q.enqueue("7")
print q.dequeue()
