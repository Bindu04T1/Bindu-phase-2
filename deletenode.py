def deleteTailNode(head):
    if head==None or head.next==None:
        return None
    
    previous=None
    currentNode=head
      
    while currentNode.next!=None:
        previous=currentNode
        currentNode=currentNode.next

    previous.next=None
    return head


