class Node:
    def __init__(self, data):
        self.data = data 
        self.next = None 
 
def printLinkedList(head):
    currentNode = head 
    while currentNode != None:
        print(currentNode.data, end = " --> ")
        currentNode = currentNode.next
    print()
 
def insertAtTail(head, ele):
    temp = Node(ele)
    if head == None:
        return temp
 
    tail = head 
    while tail.next != None:
        tail = tail.next 
    tail.next = temp 
    return head
 
# Task - 1
def insertAtHead(head, ele):
    temp = Node(ele)
    temp.next = head 
    return temp
 
# Task - 2
def insertAtSpecificPosition(head, position, ele):
    if position == 0:
        return insertAtHead(head, ele)
 
    temp = Node(ele)
    index = 0 
    currentNode = head 
 
    while index != position - 1:
        currentNode = currentNode.next 
        index += 1 
 
    nextNode = currentNode.next 
    temp.next = nextNode 
    currentNode.next = temp 
    return head
 
 
 
 
nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
head = None 
for ele in nums:
    head = insertAtTail(head, ele)
print("Final linked list is:")
printLinkedList(head)
 
head =insertAtSpecificPosition(head, 3, 101)
printLinkedList(head)
 
# Object creation is happening      
# obj1 = Node(10)
# obj2 = Node(20)
# obj3 = Node(30)
# obj4 = Node(40)
# obj5 = Node(50) 
 
# Links establishing in below lines 
# obj1.next = obj2 
# obj2.next = obj3
# obj3.next = obj4 
# obj4.next = obj5 
 
# print linked list 
#10 --> 20 --> 30 --> 40 --> None


