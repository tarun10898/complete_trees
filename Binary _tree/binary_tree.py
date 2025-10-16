from typing import Optional


class Node:
    def __init__(self,value:int) -> None:
        self.value:int = value
        self.left:Optional[Node] = None
        self.right:Optional[Node] = None

class BinaryTree:
    def __init__(self) -> None:
        self.root:Optional[Node] = None
    
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

    def search(self, value: int) -> bool:
        return self._search_recursive(self.root, value)

    def _search_recursive(self, node: Optional[Node], value: int) -> bool:
        if node is None:
            return False
        if value == node.value:
            return True
        elif value < node.value:
            return self._search_recursive(node.left, value)
        else:
            return self._search_recursive(node.right, value)

    def inorder(self) -> list[int]:
        result: list[int] = []
        self._inorder_recursive(self.root, result)
        return result

    def _inorder_recursive(self, node: Optional[Node], result: list[int]) -> None:
        if node:
            self._inorder_recursive(node.left, result)
            result.append(node.value)
            self._inorder_recursive(node.right, result)

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

    print("Inorder Traversal:", bt.inorder())