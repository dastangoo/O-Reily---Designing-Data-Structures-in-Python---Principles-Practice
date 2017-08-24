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
        parent.add(value)
        return parent
    def remove(self, value):
        if value < self.value:
            self.left = self.removeFromParent(self.left, value)
        elif value > self.value:
            self.right = self.removeFromParent(self.right, value)
        else:
            if self.left is None:
                return self.right
            # find largest value in left subtree

            child = self.left
            while child.right:
                child = child.right
            childkey = child.value
            self.left = self.removeFromParent(self.left, child, childkey)

            self.value = childkey
        return self
    def removeFromParent(self, parent, value):
        if parent:
            return parent.remove(value)
        return None

class BinaryTree:
    def __init__(self):
        self.root = None
    def getMin(self):
        if self.root is None:
            raise ValueError("Binary Tree is empty")
        n = self.root
        while n.left:
            n = n.left
        return n.value
    def getMax(self):
        if self.root is None:
            raise ValueError("Binary Tree is empty")
        n = self.root
        while n.right:
            n = n.right
        return n.value
    def add(self, value):
        if self.root == None:
            self.root = BinaryNode(value)
        else:
            self.root.add(value)
    def remove(self, value):
        if self.root is not None:
            self.root = self.root.remove(value)
    def closest(self, target):
        if self.root is None:
            return None
        node = self.root
        best = node
        distance = abs(self.root.value - target)
        while node:
            if abs(node.value - target) < distance:
                best = node
                distance = abs(node.value - target)
            if target < node.value:
                node = node.left
            elif target > node.value:
                node = node.right
            else:
                return target
        return best.value

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
