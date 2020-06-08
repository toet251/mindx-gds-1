
class LinkedListNode:
    def __init__(self, val, next):
        self.val = val
        self.next = next 
    
def ex2(root, k):
    count_node = 0
    node = root
    while node:
        count_node += 1
        node = node.next 

    k = k % count_node
    if k == 0:
        return root

    i = 0
    node = root
    new_root = None; new_last_node = None; last_node = None
    
    while node:
        i += 1
        if i == count_node - k:
            new_last_node = node
            new_root = new_last_node.next
        if i == count_node:
            last_node = node
        node = node.next

    last_node.next = root 
    new_last_node.next = None

    return new_root 

