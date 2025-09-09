from collections import deque

# ============================
# Classe Node
# ============================
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# ============================
# Classe BinaryTree
# ============================
class BinaryTree:
    def __init__(self):
        self.root = None

    # ----------------------------
    # Inserção automática por nível
    # ----------------------------
    def insert_level_order(self, data):
        new_node = Node(data)
        if not self.root:
            self.root = new_node
            return

        q = deque([self.root])
        while q:
            node = q.popleft()
            if not node.left:
                node.left = new_node
                return
            else:
                q.append(node.left)

            if not node.right:
                node.right = new_node
                return
            else:
                q.append(node.right)

    # ----------------------------
    # Travessias
    # ----------------------------
    def inorder(self, node, result):
        if node:
            self.inorder(node.left, result)
            result.append(node.data)
            self.inorder(node.right, result)

    def preorder(self, node, result):
        if node:
            result.append(node.data)
            self.preorder(node.left, result)
            self.preorder(node.right, result)

    def postorder(self, node, result):
        if node:
            self.postorder(node.left, result)
            self.postorder(node.right, result)
            result.append(node.data)

    def level_order(self):
        result = []
        if not self.root:
            return result
        q = deque([self.root])
        while q:
            node = q.popleft()
            result.append(node.data)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        return result

    # ----------------------------
    # Verificações estruturais
    # ----------------------------
    def height(self, node):
        if not node:
            return 0
        return 1 + max(self.height(node.left), self.height(node.right))

    def count_nodes(self, node):
        if not node:
            return 0
        return 1 + self.count_nodes(node.left) + self.count_nodes(node.right)

    def is_perfect(self):
        def check(node, depth, level=0):
            if not node:
                return True
            if not node.left and not node.right:
                return depth == level + 1
            if not node.left or not node.right:
                return False
            return check(node.left, depth, level+1) and check(node.right, depth, level+1)

        depth = self.height(self.root)
        return check(self.root, depth)

    def is_complete(self):
        if not self.root:
            return True
        q = deque([self.root])
        end = False
        while q:
            node = q.popleft()
            if not node:
                end = True
            else:
                if end:
                    return False
                q.append(node.left)
                q.append(node.right)
        return True

    def is_regular(self):
        def check(node):
            if not node:
                return True
            if (node.left and not node.right) or (not node.left and node.right):
                return False
            return check(node.left) and check(node.right)
        return check(self.root)

    def is_balanced(self):
        def check(node):
            if not node:
                return 0, True
            lh, lb = check(node.left)
            rh, rb = check(node.right)
            return 1 + max(lh, rh), lb and rb and abs(lh - rh) <= 1
        return check(self.root)[1]

    def is_unbalanced(self):
        return not self.is_balanced()


# ============================
# Exemplo de uso
# ============================
if __name__ == "__main__":

    print("\nÁrvore 1")
    tree1 = BinaryTree()
    valores = [1, 2, 3, 4, 5, 6]
    for v in valores:
        tree1.insert_level_order(v)

    in_ord = []
    tree1.inorder(tree1.root, in_ord)
    pre_ord = []
    tree1.preorder(tree1.root, pre_ord)
    post_ord = []
    tree1.postorder(tree1.root, post_ord)
    level_ord = tree1.level_order()

    print("In-Order:", in_ord)
    print("Pré-Order:", pre_ord)
    print("Pós-Order:", post_ord)
    print("Level-Order:", level_ord)

    print("\nClassificação da árvore:")
    if tree1.is_perfect(): print("Perfeita")
    if tree1.is_complete(): print("Completa")
    if tree1.is_regular(): print("Regular")
    if tree1.is_balanced(): print("Balanceada")
    if tree1.is_unbalanced(): print("Desbalanceada")

    print("\nÁrvore 2")
    tree2 = BinaryTree()
    valores = [6, 5, 4, 3, 2, 1, 0]
    for v in valores:
        tree2.insert_level_order(v)

    in_ord = []
    tree2.inorder(tree2.root, in_ord)
    pre_ord = []
    tree2.preorder(tree2.root, pre_ord)
    post_ord = []
    tree2.postorder(tree2.root, post_ord)
    level_ord = tree2.level_order()

    print("In-Order:", in_ord)
    print("Pré-Order:", pre_ord)
    print("Pós-Order:", post_ord)
    print("Level-Order:", level_ord)

    print("\nClassificação da árvore:")
    if tree2.is_perfect(): print("Perfeita")
    if tree2.is_complete(): print("Completa")
    if tree2.is_regular(): print("Regular")
    if tree2.is_balanced(): print("Balanceada")
    if tree2.is_unbalanced(): print("Desbalanceada")
