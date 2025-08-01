'''
Given a binary tree, determine if it is height-balanced.

A height-balanced binary tree is a binary tree in which the depth of the two subtrees of every node never differs by more than one.

'''
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def is_balanced(root: Optional[TreeNode]) -> bool:
    def get_hight(root: TreeNode) -> int:
        if root is None:
            return 0
        left_hight = get_hight(root.left)
        rith_hight = get_hight(root.right)
        return 1 + max(left_hight, rith_hight)

    if root is None:
        return True
    
    from collections import deque

    queue = deque([root])
    while queue:
        left_hight = right_hight = 0
        current = queue.popleft()
        if current.left:
            left_hight = get_hight(current.left)
            queue.append(current.left)
        if current.right:
            right_hight = get_hight(current.right)
            queue.append(current.right)
        if abs(left_hight - right_hight) > 1:
            return False
    return True
