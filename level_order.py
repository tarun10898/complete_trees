from typing import Optional
from collections import deque

class Node:
    def __init__(self, value: int) -> None:
        self.value: int = value
        self.left: Optional[Node] = None
        self.right: Optional[Node] = None

class BinaryTree:
    def __init__(self) -> None:
        self.root: Optional[Node] = None

    def insert(self, value: int) -> None:
        self.root = self._insert_recursive(self.root, value)

    def _insert_recursive(self, node: Optional[Node], value: int) -> Node:
        if node is None:
            return Node(value)
        if value < node.value:
            node.left = self._insert_recursive(node.left, value)
        elif value > node.value:
            node.right = self._insert_recursive(node.right, value)
        return node

    def level_order(self) -> list[int]:
        result: list[int] = []
        if self.root is None:
            return result

        queue: deque[Node] = deque([self.root])
        while queue:
            current = queue.popleft()
            result.append(current.value)
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
        return result

if __name__ == "__main__":
    bt = BinaryTree()
    print("Enter values to insert into the BST (comma-separated):")
    user_input = input("Values: ")  # Example: 10,5,15,3,7,12,18

    try:
        values = [int(val.strip()) for val in user_input.split(",")]
        for val in values:
            bt.insert(val)
    except ValueError:
        print("Please enter only integers separated by commas.")

    print("Level Order Traversal:", bt.level_order())