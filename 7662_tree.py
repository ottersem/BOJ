import sys
input = sys.stdin.readline

class Node:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None
        self.count = 1

class Tree:
    def __init__(self):
        self.root = None
        self.size = 0

    def i(self, data):
        new_node = Node(data)
        if self.root is None:
            self.root = new_node
            self.size += 1
            return

        current = self.root
        while True:
            if data < current.data:
                if current.left is None:
                    current.left = new_node
                    self.size += 1
                    return
                current = current.left
            elif data > current.data:
                if current.right is None:
                    current.right = new_node
                    self.size += 1
                    return
                current = current.right
            else: 
                current.count += 1
                self.size += 1
                return


    def find_max(self):
        if self.root is None:
            return None
        
        crt = self.root
        
        while crt.right is not None:
            crt = crt.right

        return crt
    
    def find_min(self):
        if self.root is None:
            return None
        
        crt = self.root

        while crt.left is not None:
            crt = crt.left

        return crt
        
    def d(self, v):
        if self.size == 0:
            return

        is_max = (v == 1)
        
        parent = None
        current = self.root
        
        while (is_max and current.right is not None) or \
              (not is_max and current.left is not None):
            parent = current
            current = current.right if is_max else current.left

        if current.count > 1:
            current.count -= 1
            self.size -= 1
            return
            
        self.size -= 1
        
        if current.left is not None:
            child = current.left
        else:
            child = current.right 
            
        if parent is None:
            self.root = child
        elif is_max:
            parent.right = child
        else:
            parent.left = child

        
for _ in range(int(input())):
    BST = Tree()
    N = int(input())
    for _ in range(N):
        line = input().split()
        ops = line[0]

        if ops == 'I':
            num = int(line[1])
            BST.i(num)
        elif ops == 'D':
            num = int(line[1])
            BST.d(num)
    if BST.size == 0:
        print("EMPTY")
    else:
        print(BST.find_max().data, BST.find_min().data)


