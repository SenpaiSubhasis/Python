class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self,newNode):
        
        if self.head is None:
            self.head = newNode
        else:
            lastNode = self.head
            while True:
                if lastNode.next is None:
                    break
                lastNode = lastNode.next
            
            lastNode.next = newNode
    def printNode(self):
        currentNode = self.head
        while True:
            if currentNode is None:
                break
            print(currentNode.data)
            currentNode = currentNode.next

    def reverse(self):
        p1,p2 = None,self.head
        while p2 is not None:
            p3 = p2.next
            p2.next = p1
            p1=p2
            p2=p3
      
        while True:
            if p1 is None:
                break
            print(p1.data)
            p1 = p1.next

firstnode = Node("King")
secondnode = Node("Subhasis")
thirdnode = Node("Hello")
linkedlist = LinkedList()
linkedlist.insert(firstnode)
linkedlist.insert(secondnode)
linkedlist.insert(thirdnode)

linkedlist.reverse()
linkedlist.printNode()


