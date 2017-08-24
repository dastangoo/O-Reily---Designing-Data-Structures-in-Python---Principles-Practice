class BinaryNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    def add(self, value):
        if value <= self.value:
            self.left = self.addToSubTree(self.left, value)
        elif value > self.value:
            self.right = self.addToSubTree(self.right, value)
    def addToSubTree(self, parent, value):
        if parent is None:
            return BinaryNode(value)
        parent.add(val)
        return parent

class BinaryTree:
    def __init__(self):
        self.root = None
    def add(self, value):
        if self.root == None:
            self.root = BinaryNode(value)
        else:
            self.root.add(value)
    def remove(self, value):
        pass
    def __contains__(self, target):
        node = self.root
        while node is not None:
            if target < node.value:
                node = node.left
            elif target > node.value:
                node = node.right
            else:
                return True
        return False
