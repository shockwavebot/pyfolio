'''
Given the root of a binary tree, 
imagine yourself standing on the right side of it, 
return the values of the nodes you can see ordered from top to bottom.

Example 1:
Input: root = [1,2,3,null,5,null,4]
Output: [1,3,4]

Example 2:
Input: root = [1,2,3,4,null,null,null,5]
Output: [1,3,4,5]

Example 3:
Input: root = [1,null,3]
Output: [1,3]

Example 4:
Input: root = []
Output: []
'''
from typing import Optional, List
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def print_tree(root:TreeNode):
    queue = deque([root])
    while queue:
        level = []
        for _ in range(len(queue)):
            current = queue.popleft()
            level.append(current.val)
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
        print(level)

def print_tree_with_nones(root:TreeNode):
    queue = deque([root])
    while queue:
        level = []
        for _ in range(len(queue)):
            current = queue.popleft()
            if current:
                level.append(str(current.val))
                queue.append(current.left)
                queue.append(current.right)
            else:
                level.append("-")

        # Only print the level if it contains actual node values
        if any(current != "-" for current in level):
            print(" ".join(level))

def from_array(a: List[int]) -> Optional[TreeNode]:
    root = None
    if len(a) == 0:
        return root
    root = TreeNode(a[0])
    queue = deque([root])
    current = queue.popleft()
    for i in range(1, len(a)-1, 2):
        node = a[i]
        if node:
            current.left = TreeNode(node)
            queue.append(current.left)
        node = a[i+1]
        if node:
            current.right = TreeNode(a[i+1])
            queue.append(current.right)
        current = queue.popleft()
    return root


def right_side_view(root: Optional[TreeNode]) -> List[int]:
    if root is None:
        return []
    from collections import deque
    queue = deque([root])
    result = []
    while queue:
        level_size = len(queue)
        for i in range(level_size): # key part!!!
            current = queue.popleft() # O(1) FIFO BFS
            if i == level_size -1:
                result.append(current.val)
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
    return result

if __name__ == '__main__':
    a = [1,2,3,None,5,None,4]
    tree: TreeNode = from_array(a)
    print_tree(tree)
    print_tree_with_nones(tree)
    assert right_side_view(from_array(a)) == [1,3,4]
