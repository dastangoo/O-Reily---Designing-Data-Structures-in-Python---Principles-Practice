"""
    AVL Implementaiton of Binary Tree.
"""
class BinaryNode:
    def __init__(self, value = None):
        """Create binary node."""
        self.value = value
        self.left = None
        self.right = None
        self.height = 0
    def computeHeight(self):
        """Compute height of node in BST."""
        height = -1
        if (self.left):
            height = max(height, self.left.height)
        if (self.right):
            height = max(height, self.right.height)

        self.height = height + 1
    def heightDiffrence(self):
        """Compute height difference of node's children in BST"""
        leftTarget = 0
        rightTarget = 0
        if (self.left):
            leftTarget = 1 + self.left.height
        if (self.right):
            rightTarget = 1 +  self.right.height

        return leftTarget - rightTarget
    def rotateRight(self):
        """Perform right rotation around given node."""
        newRoot = self.left
        grandson = newRoot.right
        self.left = grandson
        newRoot.right = self

        self.computeHeight()
        return newRoot

    def rotateLeft(self):
        """Perform left rotation around given node."""
        newRoot = self.right
        grandson = newRoot.left
        self.right = grandson
        newRoot.left = self

        self.computeHeight()
        return newRoot


    def rotateLeftRight(self):
        """Perform left, then right rotation around given node"""
        child = self.left
        newRoot = child.right
        grand1 = newRoot.left
        grand2 = newRoot.right
        child.right = grand1
        self.left = grand2

        newRoot.left = child
        newRoot.right = self

        child.computeHeight()
        self.computeHeight()
        return newRoot

    def rotateRightLeft(self):
        """Perform right, then left rotation around given node"""
        child = self.right
        newRoot = child.left
        grand1 = newRoot.left
        grand2 = newRoot.right
        child.left =  grand2
        self.right = grand1

        newRoot.left = self
        newRoot.right = child

        child.computeHeight()
        self.computeHeight()
        return newRoot

    def add(self, val):
        """Adds a new node to the tree with value and Rebalancing"""
        newRoot = self

        if val <= self.value:
            self.left = self.addToSubTree(self.left, val)
            if self.heightDiffrence() == 2:
                if val <= self.value:
                    newRoot = self.rotateRight()
                else:
                    newRoot = self.rotateLeftRight()
            else:
                self.right = self.addToSubTree(self.right, val)
                if self.heightDiffrence() == -2:
                    if val > self.right.value:
                        newRoot = self.rotateLeft()
                    else:
                        newRoot = self.rotateRightLeft()
        newRoot.computeHeight()
        return newRoot
    def addToSubTree(self, parent, val):
        """Add val to parent subtree (if exists) and return node"""
        if parent is None:
            return BinaryNode(val)

        parent = parent.add(val)
        return parent

    def removeFromParent(self, parent, val):
        """Helper method for remove. Ensure proper behavior
        bas children."""
        if parent:
            return parent.remove(val)
        return None

    def remove(self, val):
        """
        Remvoe val of self from BinaryTree. Works in conjunction
        method in BinaryTree
        """
        newRoot = self
        if self.value == val:
            if self.left is None:
                return self.right

            child = self.left
            while child.right:
                child = child.right

            childkey = child.value
            self.left = self.removeFromParent(self.left, childkey)
            self.value = childkey

            if self.heightDiffrence() == -2:
                if self.right.heightDiffrence() <= 0:
                    newRoot = self.rotateleft()
                else:
                    newRoot = self.rotateRightLeft()
        elif self.value > val:
            self.left = self.removeFromParent(self.left, val)
            if self.heightDiffrence() == -2:
                if self.right.heightDiffrence() <= 0:
                    newRoot = self.rotateLeft()
                else:
                    newRoot = self.rotateRightLeft()
        else:
            self.right = self.removeFromParent(self.right, val)
            if self.heightDiffrence() == 2:
                if self.left.heightDiffrence() >= 0:
                    newRoot = self.rotateRight()
                else:
                    newRoot = self.rotateLeftRight()
        newRoot.computeHeight()
        return newRoot
    def __repr__(self):
        """Useful debugging function to produce linear tree representation"""
        
