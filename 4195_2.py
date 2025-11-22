import sys
input = sys.stdin.readline

def find(i, parent):
    if parent[i] == i:
        return i
    parent[i] = find(parent[i], parent)
    return parent [i]

def union(a,b,parent,size):
    root_a = find(a,parent)
    root_b = find(b,parent)

    if root_a != root_b:
        if size[root_a] < size[root_b]:
            root_a, root_b = root_b, root_a
        
        parent[root_b] = root_a

        size[root_a] += size[root_b]
        return size[root_a]
    else:
        return size[root_a]
    
def get_id_and_init(name, name2id, parent, size):
    if name not in name2id:
        new = len(name2id)
        name2id[name] = new

        parent.append(new)
        size[new] = 1

        return new
    else:
        return name2id[name]
    
def answer(t):
    name2id = dict()
    parent = []
    size = {}
    
    for _ in range(t):
        a,b = map(str, input().split())

        id_a = get_id_and_init(a, name2id, parent, size)
        id_b = get_id_and_init(b, name2id, parent, size)

        print(union(id_a, id_b, parent, size))

for _ in range(int(input())):
    answer(int(input()))