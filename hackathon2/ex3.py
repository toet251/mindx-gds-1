class Node:
    def __init__(self, val, next):
        self.val = val
        self.next = next

def ex3(head):
    node = head 
    
    count = 0
    pre = None; pre_pre = None 
    head_even = None

    while node:
        count += 1
        if count == 2:
            head_even = node
        elif count > 2:
            pre_pre.next = node
        pre_pre = pre 
        pre = node 
        node = node.next 

    if count % 2:    
        pre_pre.next = None 
        pre.next = head_even 
    else:
        pre_pre.next = head_even
        pre.next = None

    return head

