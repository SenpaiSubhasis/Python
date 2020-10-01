class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def insert_head(self,newnode):
        temporary = self.head
        self.head = newnode
        self.head.next = temporary
        del temporary


    def insert(self,newnode):
        if self.head is None:
            self.head = newnode
        else:
            lastnode = self.head
            while True:
                if lastnode.next is None:
                    break
                lastnode = lastnode.next
            lastnode.next = newnode
    def print(self):
        currentNode = self.head
        while True:
            if currentNode is None:
                break
            print(currentNode.data)
            currentNode = currentNode.next

firstnode = Node("King")
secondnode = Node("Subhasis")
thirdnode = Node("Hello")
linkedlist = LinkedList()
linkedlist.insert(firstnode)
linkedlist.insert(secondnode)
linkedlist.insert_head(thirdnode)
linkedlist.print()
