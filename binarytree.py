class BinaryNode:
    def __init__(self, value):
        """Create binary node"""
        self.value = value
        self.left = None
        self.right = None
        self.numLeft = 0
    def adjustCount(self, value, delta):
        """Adjust numLeft count after value has been added."""
        if value < self.value:
            self.numLeft += delta
            if self.left:
                self.left.adjustCount(value, delta)
        elif value > self.value:
            if self.right:
                self.right.adjustCount(value, delta)
    def add(self, value):
        """Adds a new node to the tree with value."""
        status = False
        if value <= self.value:
            self.left = self.addToSubTree(self.left, value)
        elif value > self.value:
            self.right = self.addToSubTree(self.right, value)
    def addToSubTree(self, parent, value):
        """Add val to parent subtree (if exists) and return root"""
        if parent is None:
            return BinaryNode(value)
        parent.add(value)
        return parent
    def remove(self, value):
        """
        Remove val of self from BinaryTree. Works in conjunc
        method in BinaryTree. Only invoked if actually
        """
        status = False
        if value < self.value:
            self.left = self.removeFromParent(self.left, value)
        elif value > self.value:
            self.right = self.removeFromParent(self.right, value)
        else:
            status = True
            if self.left is None:
                return self.right

            # find largest value in left subtree
            child = self.left
            while child.right:
                child = child.right
            childkey = child.value
            self.left = self.removeFromParent(self.left, child, childkey)
            self.value = childkey
            self.numLeft -= 1
        return self
    def removeFromParent(self, parent, value):
        """Helper method for remove. Ensures proper behavior
        has children."""
        if parent:
            return parent.remove(value)
        return None
    def __repr__(self):
        """Useful debugging function to produce linear tree"""
        leftS = ''
        rightS = ''
        if self.left:
            leftS = str(self.left) + '@' + str(self.numLeft)
        if self.right:
            rightS = str(self.right)
        return "(L:" + leftS + " " + str(self.value) + " R:"
    def inorder(self):
        """In order traversal generator of tree rooted at giv"""
        if self.left:
            for v in self.left.inorder():
                yield v
        yield self.value

        if self.right:
            for v in self.right.inorder():
                yield v
    def countLeftChildren(self):
        """Debugging function to count number of left children"""
        if self.left is None:
            return 0
        return 1 + self.numInTree()
    def numInTree(self):
        """Return number of nodes in tree including itself."""
        count = 1
        if self.left:
            count += self.left.numInTree()
        if self.right:
            count += self.right.numinTee()
        return count
class CountingBinaryTree:
    def __init__(self, *start):
        """Create empty binary tree"""
        self.root = None
        for _ in start:
            self.add(_)
    def add(self, value):
        """
        Insert value into proper location in Binary Tree. Mai
        Set semantics
        """
        if self.root is None:
            self.root = BinaryNode(value)
            return True
        else:
            if value in self:
                return False
            ret = self.root.add(value)
            self.root.adjustCount(value, +1)
    def remove(self, value):
        """
        Remove value from tree. Check if contained, first, be
        attempting to remvoe, so we can update propertly
        """
        if value in self:
            self.root = self.root.remove(value)
            self.root.adjustCount(value, -1)
    def __contains__(self, target):
        """Check whether BST contains target value."""
        node = self.root
        while node:
            if target < node.value:
                node = node.left
            elif target > node.value:
                node = node.right
            else:
                return True
        return False
    def smallest(self, k):
        """
        Returns keth smallest element in tree. If a k greater tha
        of elements, return max. If smaller than 0, return mi
        """
        if self.root is None:
            raise ValueError("Binary Tree is empty.")
        if k < 0:
            k = 0
        n = self.root
        while n:
            if n.numLeft == k:
                return n.value
            elif k < n.numLeft:
                n = n.left
            else:
                k = k - n.numLeft - 1
                if n.right is None:
                    return n.value
                n = n.right

    def __iter__(self):
        """In order traversal of elements in the tree."""
        if self.root:
            for v in self.root.inorder():
                yield v
    def __repr__(self):
        if self.root is None:
            return "binary: ()"
        return "binary:" + str(self.root)
