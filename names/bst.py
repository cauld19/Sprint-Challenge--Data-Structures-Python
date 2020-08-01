class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


    # Insert the given value into the tree
    def insert(self, value):
        cur_node = self
        while cur_node:
            if cur_node.value == value:
                return None
            if value < cur_node.value:
                if cur_node.left is None:
                    cur_node.left = BSTNode(value)
                    return value
                elif cur_node.left.value == value:
                    return None
                else:
                    cur_node = cur_node.left
            else:
                if cur_node.right is None:
                    cur_node.right = BSTNode(value)
                    return value
                elif cur_node.right.value == value:
                    return None
                else:
                    cur_node = cur_node.right
            


    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        cur_node = self
        if self is None:
            return False
        elif cur_node.value is target:
            return True
        else:
            while cur_node:
                if target < cur_node.value:
                    if cur_node.left is None:
                        return False
                    elif target is not cur_node.left.value:
                        cur_node = cur_node.left
                    else:
                        return True
                else:
                    if cur_node.right is None:
                        return False
                    elif target is not cur_node.right.value:
                        cur_node = cur_node.right
                    else:
                        return True