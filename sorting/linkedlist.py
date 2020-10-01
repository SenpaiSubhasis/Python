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
            lastNode = newNode

    def printf(self):
        currentNode = self.head
        while True:
            if currentNode is None:
                break
            print(currentNode.next)
            currentNode = currentNode.next

firstNode = Node("King")
secondNode = Node("Subhasis")

linked_list = LinkedList()
linked_list.insert(firstNode)
linked_list.insert(secondNode)

linked_list.printf()
