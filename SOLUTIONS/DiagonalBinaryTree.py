#!/usr/bin/python3

from collections import deque, defaultdict

class Node:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val

def diagonal_traversal(root, should_print=True):
    queue = deque()
    queue.append((root, 0))

    vals = defaultdict(list)
    while queue:
        node, left_count = queue.popleft()
        vals[left_count].append(node.val)

        if node.right is not None:
            queue.append((node.right, left_count))
        if node.left is not None:
            queue.append((node.left, left_count + 1))

    while should_print and vals:
        min_key = min(vals.keys())
        print(vals[min_key])
        del vals[min_key]

    return vals if not should_print else None

if __name__ == '__main__':
    tree = Node(8)
    tree.left = Node(3)

    branch = Node(6)
    branch.left = Node(4)
    branch.right = Node(7)

    right_branch = Node(10)
    right_branch.left = branch
    right_branch.right = Node(14)
    right_branch.right.left = Node(13)

    tree.left.left = Node(1)
    tree.right = right_branch

    diagonal_traversal(tree)

