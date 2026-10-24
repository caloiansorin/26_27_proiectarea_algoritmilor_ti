class Node:
    __slots__ = ("value", "left", "right")

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def insert(root, value):
    """Insert iteratively (avoids recursion limits on skewed trees)."""
    if root is None:
        return Node(value)
    cur = root
    while True:
        if value < cur.value:
            if cur.left is None:
                cur.left = Node(value)
                break
            cur = cur.left
        else:  # equal values go right, which keeps the sort stable
            if cur.right is None:
                cur.right = Node(value)
                break
            cur = cur.right
    return root


def inorder(root):
    """Iterative in-order traversal (yields values in sorted order)."""
    stack, cur = [], root
    while stack or cur:
        while cur:
            stack.append(cur)
            cur = cur.left
        cur = stack.pop()
        yield cur.value
        cur = cur.right


def tree_sort(items):
    root = None
    for x in items:
        root = insert(root, x)
    return list(inorder(root))


if __name__ == "__main__":
    print(tree_sort([5, 3, 8, 1, 4, 7, 9, 2, 6, 3]))
    # [1, 2, 3, 3, 4, 5, 6, 7, 8, 9]
