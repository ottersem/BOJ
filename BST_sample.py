class Node:
    def __init__(self, key):
        self.right = None
        self.left = None
        self.value = key

class BST:

    def __init__(self):
        self.root = None

    def insert(self, key):
        if not self.root:
            self.root = Node(key)

        else:
            curr = self.root
            while True:
                if key < curr.value:
                    if curr.left:
                        curr = curr.left
                    else:
                        curr.left = Node(key)
                        break
                else:
                    if curr.right:
                        curr = curr.right
                    else:
                        curr.right = Node(key)
                        break

    def search(self, key):
        curr = self.root

        while curr and curr.value != key:
            if key < curr.value:
                curr = curr.left
            else:
                curr = curr.right

        return curr
    
def solution(lst, search_lst):
    bst = BST()
    for element in lst:
        bst.insert(element)

    result = []

    for value in search_lst:
        if bst.search(value):
            result.append(True)
        else:
            result.append(False)

    return result

lst = [5,3,8,4,2,1,7,10]
search_lst = [1,2,5,6,12]

print(solution(lst=lst, search_lst=search_lst))