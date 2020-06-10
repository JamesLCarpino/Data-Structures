"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""


class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # check if there is no root
        # 1 check if there is no root
        # if there isn't create the node and park it there
        # we can check this if self is none to see if there is no root
        if self is None:
            self = BSTnode(value)

        # 2 otherwise, there is a root
        else:
            # compare the value to the roots value to determine which direction to go
            if value < self.value:
                # how do we go left?
                # we need to check if there is another node on the left side
                if self.left:
                    # then self.left is a node
                    self.left.insert(value)
                else:
                    # if no self let we can park value here
                    self.left = BSTNode(value)
                # self.left = BSTNode(value)
            # if the value < root's value
            # go left

            else:
                # else the value >= roots value
                # go right
                # how do we go right?
                if self.right:
                    # then self.right is a node
                    self.right.insert(value)
                else:
                    # if no self right we can park value here
                    self.right = BSTNode(value)
                # self.right = BSTNode(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # if the tree contains the target value it is True

        if self.value == target:
            return True
        if target < self.value:
            if not self.left:
                return False
            else:
                return self.left.contains(target)
        else:
            if not self.right:
                return False
            else:
                return self.right.contains(target)
        # else the tree doesn't contain the target value there for False

    # Return the maximum value found in the tree
    def get_max(self):
        # go to the right
        # if nothing right to the value than the root must be largest value
        if not self.right:
            return self.value
        else:
            # return a recursive call
            # if using recursion to find an answer then always return a recursive call so that you can return backinto the next level until you hit basecase
            return self.right.get_max()

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        fn(self.value)

        if self.left:
            self.left.for_each(fn)
        if self.right:
            self.right.for_each(fn)

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        pass

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
