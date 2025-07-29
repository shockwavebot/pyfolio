

class TreeNode:
    def __init__(self, val):
        self.val: int = val
        self.left: TreeNode = None
        self.right: TreeNode = None

class BinaryTree:
    def __init__(self, root: TreeNode):
        self.root: TreeNode = root

    def add_right(self, at_val: int, value:int):
        stack = [self.root]
        found = False
        while stack:
            current = stack.pop()
            if current.val == at_val:
                if current.right is None:
                    current.right = TreeNode(value)
                    found = True
                    break
                else:
                    raise ValueError(f"Position occupied with {current.right}")
            stack.append(current.right)
            stack.append(current.left)
        if not found:
            raise ValueError(f"Value {value} not found in tree")

    def add_left(self, at_val: int, value:int):
        stack = [self.root]
        found = False 
        while stack:
            current = stack.pop()
            if current.val == at_val:
                if current.left is None:
                    current.left = TreeNode(value)
                    found = True
                    break
                else:
                    raise ValueError(f"Position occupied with {current.left}")
            stack.append(current.right)
            stack.append(current.left)
        if not found:
            raise ValueError(f"Value {value} not found in tree")

    def __repr__(self):
        from collections import deque
        from math import exp2
        return_str = ''
        q = deque([self.root])
        level = 0
        elems_at_level = []
        while q: 
            current = q.popleft()
            elems_at_level.append(current.val)
            if len(elems_at_level) == exp2(level):
                return_str += f"{elems_at_level}\n"
                elems_at_level = []
                level += 1
            if current.left:
                q.append(current.left)
            if current.right:
                q.append(current.right)
        if elems_at_level:
            current_count = len(elems_at_level)
            elems_at_level.extend([None]*(int(exp2(level))-current_count))
            return_str += f"{elems_at_level}\n"
        return return_str

if __name__ == '__main__':
    bt = BinaryTree(TreeNode(1))
    bt.add_left(1,2)
    bt.add_right(1,3)
    bt.add_left(2,4)
    bt.add_right(2,5)
    print(bt)