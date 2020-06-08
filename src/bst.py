class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BST:
    def __init__(self, root):
        self.root = root 

    def search(self, val):
        node = self.root
        while node:
            if node.val == val:
                return True 
            if node.val > val:
                node = node.left 
            else:
                node = node.right 
        return False

    def insert(self, val):
        node = self.root 
        parent = None
        while node:
            if node.val == val:
                return 
            parent = node 
            if node.val > val:
                node = node.left
            else: 
                node = node.right 
        
        if not parent:
            return
        
        if parent.val > val:
            parent.left = Node(val)
        else:
            parent.right = Node(val)

    def remove(self, val):
        node = self.root 
        parent = None

        found = False
        while node:
            if node.val == val:
                found = True 
                break
            parent = node
            if node.val > val:
                node = node.left 
            else:
                node = node.right
        
        if not found:
            return

        if not node.left or not node.right:
            only_child = node.left if node.left else node.right
            if not parent:
                self.root = node.right
            elif parent.val > val:
                parent.left = only_child
            else:
                parent.right = only_child

        else:
            replace_node = node.right
            p_replace_node = node
            while replace_node.left:
                p_replace_node = replace_node
                replace_node = replace.left

            p_replace_node.left = replace_node.right 
            node.val = replace_node.val
        
    def in_order(self):
        return self.__in_order(self.root)

    def __in_order(self, node):
        if not node:
            return []
        res = []
        res += self.__in_order(node.left)
        res.append(node.val)
        res += self.__in_order(node.right)
        return res 
