#implementation of a singly linkedlist using Node class

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        

class LinkedList:
    def __init__(self):
        self.head=None

    def add_node (self,data):   #adding a node to the front of a linkedlist
        newNode=Node(data)
        newNode.next=None
        if self.head==None:
            self.head=newNode
        else:
            newNode.next=self.head
            self.head=newNode

    def search_node(self,data):
        curNode=self.head
        found=False
        while curNode !=None and not found:
            if curNode.data==data:
                found=True

            else:
                curNode=curNode.next
        return found

    def delete_node (self,data):
        temp=self.head
        curNode=temp.next
        found=False
        if temp.data==data:
            temp.next=None
            self.head=curNode
            temp=self.head
            current=temp.next
            
            
        else:
            while curNode != None and not found:
                if curNode.data==data:
                    found=True
                    temp.next=curNode.next
                else:
                    curNode=curNode.next

    def traverse (self):
        curNode=self.head
        while curNode != None:
            print (curNode.data)
            curNode=curNode.next


l=LinkedList()
l.add_node("4")
l.add_node("6")
l.add_node("8")
l.add_node("9")

print(l.search_node("7"))
print(l.search_node("8"))

l.delete_node("9")

l.traverse()








        
