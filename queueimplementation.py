# queue Implementation using lists

class Queue:
    def __init__(self):                      #items enter to a queue at back
        self.items= []                      # and leave at front

    def isEmpty(self):
        return self.items==[]

    def enqueue(self,item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

    def show(self):
        for i in self.items:
            print i
            
        

q=Queue()
q.enqueue("2")
q.enqueue("3")
q.enqueue("67")
q.show()
print (q.dequeue())


