AVL trees are a natural evolution from basic binary search trees, especially for performance-critical systems. They maintain **balance** automatically, ensuring that operations like insert, delete, and search stay in **O(log n)** time.

---

## 🌳 What Is an AVL Tree?

An **AVL Tree** is a self-balancing Binary Search Tree where:
- The **height difference** (balance factor) between left and right subtrees of any node is at most **1**
- After every insertion or deletion, the tree may perform **rotations** to restore balance

---

## 🔁 Key Concepts to Master

| Concept             | Description |
|---------------------|-------------|
| **Balance Factor**  | `height(left) - height(right)` for each node |
| **Rotations**       | Used to rebalance the tree: Left, Right, Left-Right, Right-Left |
| **Height Tracking** | Each node stores its height to compute balance factor efficiently |
| **Insert/Delete**   | Same as BST, but followed by rebalancing if needed |

---

## 🧱 Suggested Learning Path

1. ✅ Start with a basic AVL `Node` class that tracks height
2. ✅ Implement `insert()` with rebalancing logic
3. 🔁 Add rotation methods: `rotate_left`, `rotate_right`, etc.
4. 🔍 Add `search()` (same as BST)
5. 🧹 Optionally add `delete()` with rebalancing
6. 📊 Add `inorder`, `preorder`, `level_order` traversal for validation

---
