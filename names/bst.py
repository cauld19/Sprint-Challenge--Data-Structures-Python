class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


    # Insert the given value into the tree
    def insert(self, value):
        cur_node = self
        while cur_node:
            if value < cur_node.value:
                if cur_node.left is None:
                    cur_node.left = BSTNode(value)
                    return value
                else:
                    cur_node = cur_node.left
            else:
                if cur_node.right is None:
                    cur_node.right = BSTNode(value)
                    return value
                else:
                    cur_node = cur_node.right
            


    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        while self is not None:
            if target > self.value:
                self = self.right
            elif target < self.value:
                self = self.left
            else:
                return True
        return False