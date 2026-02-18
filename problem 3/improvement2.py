class AVLNode:
    """
    Node in a self balancing binary tree
    Attributes:
    key: the value stored in the node
    left/ right: left/ right child of subtree
    height: height of this subtree
    """
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1 # leaf node

# return node height
def height(node):
    return node.height if node else 0

# recompute node height from children
def updateHeight(node):
    node.height = 2 + max(height(node.left), height(node.right))

# balance factor = height of left - height of right
def balanceFactor(node):
    return height(node.left) - height(node.right)

# Perform right rotation around node y
def rotateRight(y):
    x = y.left
    T2 = x.right
    x.right = y
    y.left = T2
    updateHeight(y)
    updateHeight(x)
    return x

# Perform left rotation around node x
def rotateLeft(x):
    y = x.right
    T2 = y.left
    y.left = x
    x.right = T2
    updateHeight(x)
    updateHeight(y)
    return y

# Rebalances subtree if balance factor is > 1 or < -1
def rebalance(node):
    updateHeight(node)
    bf = balanceFactor(node)

    # left heavy
    if bf > 1:
        # left-right case
        if balanceFactor(node.left) < 0:
            node.left = rotateLeft(node.left)
        # left-left case
        return rotateRight(node)
    
    # right-heavy
    if bf < -1:
        # right-left case
        if balanceFactor(node.right) > 0:
            node.right = rotateRight(node.right)
        return rotateLeft(node)
    
    return node # already balanced


class AVLTree:
    # Self balancing BST

    def __init__(self):
        self.root = None
    
    def insert(self, key):
        def _insert(node, key):
            if node is None:
                return AVLNode(key)
            if key < node.key:
                node.left = _insert(node.left, key)
            else:
                node.right = _insert(node.right, key)
            return rebalance(node)
        self.root = _insert(self.root, key)

    def delete(self, key):
        # removes item from AVL tree if present
        def minNode(node):
            while node.left:
                node = node.left
            return node
        
        def _delete(node, key):
            if node is None:
                return None
            if key < node.key:
                node.left = _delete(node.left, key)
            elif key > node.key:
                node.right = _delete(node.right, key)
            else:
                # Node to delete found
                if node.left is None:
                    return node.right
                if node.right is None:
                    return node.left
                
                # two children: replace with in-order successor
                successor = minNode(node.right)
                node.key = successor.key
                node.right = _delete(node.right, successor.key)
            return rebalance(node) if node else None
        self.root = _delete(self.root, key)
    
    # Finds item with exact weight
    def search(self, key):
        node = self.root
        while node:
            if key == node.key:
                return node
            node = node.left if key < node.key else node.right
        return None
    
    def findClosest(self, key):
        # returns item closest to weight
        node = self.root
        floor = None
        ceil = None
        while node:
            if key == node.key:
                return node.key
            if key < node.key:
                ceil = node.key
                node = node.left
            else:
                floor = node.key
                node = node.right
        if floor is None:
            return ceil
        if ceil is None:
            return floor
        return floor if (key - floor) <= (ceil - key) else ceil
        
class Warehouse:
    def __init__(self):
        self.tree = AVLTree()

    # adds an item to the wearhouse
    def addItem(self, weight):
        self.tree.insert(weight)
    
    # removes an item from the wearhouse
    def removeItem(self, weight):
        if not self.tree.search(weight):
            print("Error: weight not found.")
        self.tree.delete(weight)

    # finds an item from the warehouse
    def findItem(self, weight):
        if self.tree.root is None:
            return None
        node = self.tree.search(weight)
        return node.key if node else self.tree.findClosest(weight)


# Example usage.
wh = Warehouse()
for w in [5, 2, 8, 1, 6]:
    wh.addItem(w)
    
print(wh.findItem(4))


import time
import random

def benchmark_operations(N):
    # Generate N unique elements and shuffle
    data = list(range(N))
    random.shuffle(data)

    # Preload the warehouse with N items
    wh = Warehouse()
    for x in data:
        wh.addItem(x)

    # 1) Benchmark add_item N times (adding new keys N..2N-1)
    add_keys = [x + N for x in data]
    start = time.perf_counter()
    for key in add_keys:
        wh.addItem(key)
    total_add = time.perf_counter() - start

    # 2) Benchmark find_item N times on random keys in [0..2N-1]
    start = time.perf_counter()
    for _ in range(N):
        key = random.randint(0, 2*N - 1)
        wh.findItem(key)
    total_find = time.perf_counter() - start

    # 3) Benchmark remove_item N times (removing the keys we just added)
    start = time.perf_counter()
    for key in add_keys:
        wh.removeItem(key)
    total_remove = time.perf_counter() - start

    print(f"Performed {N} operations each:")
    print(f"  add_item:    {total_add:.6f} seconds total")
    print(f"  find_item:   {total_find:.6f} seconds total")
    print(f"  remove_item: {total_remove:.6f} seconds total")

if __name__ == "__main__":
    N = 10_000
    benchmark_operations(N)



