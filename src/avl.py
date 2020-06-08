class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left 
        self.right = right


class AVL:
    def __init__(self, root=None):
        self.root = root 

    def search(self, val):
        # Return bool if val is in AVL tree
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
        # Insert val into AVL tree

        # Iterate to get the place for new value
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
        
        # If root is None => parent is None, let new node be root
        if not parent:
            self.root = Node(val)
            return
        
        # Insert new value to the found place
        if parent.val > val:
            parent.left = Node(val)
        else:
            parent.right = Node(val)

        # Rebalance tree
        self.__rebalance(None, self.root)

    def remove(self, val):
        # Remove value from AVL tree
        node = self.root 
        parent = None

        found = False # to check if the value is in AVL
        # Find the node contains the value to remove
        while node:
            if node.val == val:
                found = True 
                break
            parent = node
            if node.val > val:
                node = node.left 
            else:
                node = node.right
        
        # If the value is not in AVL, nothing to do
        if not found:
            return

        # If the node has no child or 1 child, just remove the node by reassigning the child for the parent of the removed node
        if not node.left or not node.right:
            only_child = node.left if node.left else node.right
            if not parent:
                self.root = node.right
            elif parent.val > val:
                parent.left = only_child
            else:
                parent.right = only_child

        # Else: Find the min node of right-child, take the value to removed val, and remove the min node
        else:
            # Find the min node of right-child
            replace_node = node.right
            p_replace_node = node
            while replace_node.left:
                p_replace_node = replace_node
                replace_node = replace.left

            # Remove the min node, assign min value to removed value
            p_replace_node.left = replace_node.right
            node.val = replace_node.val

        self.__rebalance(None, self.root)

    def __height(self, node):
        if not node: 
            return 0
        return max(self.__height(node.left) + 1, self.__height(node.right) + 1)

    def __bf(self, node):
        if not node:
            return 0
        return self.__height(node.right) - self.__height(node.left)

    def __rebalance(self, parent, node):
        if not node:
            return 

        if self.__bf(node) < -1:
            if self.__bf(node.left) > 0:
                self.__rotate_left(node, node.left)
            self.__rotate_right(parent, node)
        
        elif self.__bf(node) > 1:
            if self.__bf(node.right) < 0:
                self.__rotate_right(node, node.right)
            self.__rotate_left(parent, node)

        self.__rebalance(node, node.left)
        self.__rebalance(node, node.right)

    def __rotate_right(self, parent, node):
        replace_node = node.left 
        node.left = replace_node.right 
        replace_node.right = node
        
        if not parent:
            self.root = replace_node
        elif parent.val > node.val:
            parent.left = replace_node
        else:
            parent.right = replace_node

    def __rotate_left(self, parent, node):
        replace_node = node.right 
        node.right = replace_node.left 
        replace_node.left = node

        if not parent:
            self.root = replace_node
        elif parent.val > node.val:
            parent.left = replace_node
        else:
            parent.right = replace_node

    def display(self):
        q = []
        q.append(self.root)
        res = []

        while q:
            node = q.pop(0)
            if node:
                res.append(node.val)
            else:
                res.append(None)

            if node:
                q.append(node.left)
                q.append(node.right)
    
        print(res)
