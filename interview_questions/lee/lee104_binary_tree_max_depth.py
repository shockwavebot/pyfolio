from typing import Optional, List
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def root_from_array(btree = List[Optional[int]]) -> Optional[TreeNode]:
    """
    root = [3,9,20,None,None,15,7]

      3
     / \ 
    9   20
       / \ 
      15  7

    size = 2^3 - 1, dept = 3

    """
    if not btree or btree[0] is None:
        return None
    
    root = TreeNode(btree[0])
    queue = [root]
    i = 1
    
    while queue and i < len(btree):
        current = queue.pop(0)
        
        # Left child
        if i < len(btree) and btree[i] is not None:
            current.left = TreeNode(btree[i])
            queue.append(current.left)
        i += 1
        
        # Right child
        if i < len(btree) and btree[i] is not None:
            current.right = TreeNode(btree[i])
            queue.append(current.right)
        i += 1
    
    return root


# 🟡 Recursive DFS (Elegant and Simple)
def max_depth(root: Optional[TreeNode]) -> int:
    if not root:
        return 0
    return 1 + max(max_depth(root.left), max_depth(root.right))


# ✅ Iterative DFS (Using a Stack LIFO)
def max_depth_iterative(root: Optional[TreeNode]) -> int:
    """Iterative DFS approach using stack (LIFO)"""
    if not root:
        return 0
    
    stack = [(root, 1)]
    max_depth = 0

    while stack:
        node, depth = stack.pop()
        if node:
            max_depth = max(max_depth, depth)
            stack.append((node.left, depth + 1))
            stack.append((node.right, depth + 1))

    return max_depth


# 🟡 Iterative BFS (Using a Queue FIFO)
def max_depth_bfs(root: Optional[TreeNode]) -> int:
    """BFS approach using queue (FIFO)"""
    if not root:
        return 0
    
    queue = deque([(root, 1)])
    max_depth = 0

    while queue:
        node, depth = queue.popleft()  # FIFO - processes level by level
        if node:
            max_depth = max(max_depth, depth)
            if node.left:
                queue.append((node.left, depth + 1))
            if node.right:
                queue.append((node.right, depth + 1))

    return max_depth
