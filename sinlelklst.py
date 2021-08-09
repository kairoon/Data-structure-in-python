class Node(object):
    def __init__(self,data):
        self.data=data
        self.nextNode=None
class LinkedList(object):
    def __init__(self):
        self.head=None
        self.size=0
    def insertStart(self,data):
        self.size=self.size+1
        newNode=Node(data)
        if not self.head:
            self.head=newNode
        else:
            newNode.nextNode=self.head
            self.head=newNode
    def insertEnd(self,data):
        self.size=self.size+1
        newNode=Node(data)
        actualNode=self.head
        while actualNode.nextNode is not None:
            actualNode=actualNode.nextNode
        actualNode.nextNode=newNode
    def remove(self,data):
        if self.head is None:
            return
        self.size=self.size-1
        currentNode=self.head
        previousNode=None
        while currentNode.data!=data:
            previousNode=currentNode
            currentNode=currentNode.nextNode
        if previousNode is None:
            self.head=currentNode.nextNode
        else:
            previousNode.nextNode=currentNode.nextNode
    def traverselst(self):
        actualNode=self.head
        while actualNode is not None:
            print('%d'%actualNode.data)
            actualNode=actualNode.nextNode
    def size1(self):
        return self.size
    def size2(self):
        actualNode=self.head
        size=0
        while actualNode is not None:
            size+=1
            actualNode=actualNode.nextNode
        return size
linkedlist=LinkedList()
linkedlist.insertStart(20)
linkedlist.insertStart(30)
linkedlist.insertStart(40)
linkedlist.insertStart(50)
linkedlist.insertStart(60)
linkedlist.traverselst()
print('*******************')
linkedlist.insertEnd(70)
linkedlist.traverselst()
linkedlist.remove(30)
print('@@@@@@@@@@@@@@@@@@@')
linkedlist.traverselst()




