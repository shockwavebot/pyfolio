"""
You are given the root of a binary search tree (BST) and an integer val.

Find the node in the BST that the node's value equals val and 
return the subtree rooted with that node. If such a node does not exist, return null.
"""
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def searchBST(root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        # LIFO = stack = DFS
        stack = [root]
        while stack:
            current = stack.pop()
            if val == current.val:
                return current
            elif val > current.val:
                if current.right:
                    stack.append(current.right)
            else:
                if current.left:
                    stack.append(current.left)
        return None

if __name__ == '__main__':
    expected_return = TreeNode(val=2, left=TreeNode(1), right=TreeNode(3))
    bst = TreeNode(val=4, left=expected_return, right=TreeNode(7))
    assert Solution.searchBST(bst, 2) == expected_return
