class Node():
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

node1 = Node(10)
node2 = Node(20)
node3 = Node(30)

head = node1
node1.next = node2
node2.next = node3



def search(head, target):
    current = head
    while(current):
        if current.data == target:
             return True
        current = current.next
    return False

def insert_beginning(head, value):
    new_node = Node(value)

    new_node.next = head
    head = new_node

def insert_end(head, value):
    new_node = Node(value)
    if not head:
        head = new_node
        return head

    current = head
    while(current.next != None):
        current = current.next

    current.next = new_node

    return head