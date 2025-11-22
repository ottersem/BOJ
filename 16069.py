import sys
input = sys.stdin.readline

def get_id(name, name2id, parent, size):
    if name not in name2id:
        new = len(name2id)-1
        name2id[name] = new

        parent.append(new)
        size[new] += 1
        return new # name2id, parent 삽입 성공시 True
    else:
        return name2id[name]
    
def find(i, parent):
    if parent[i] == i:
        return i
    parent[i] = find(parent[i], parent)
    return parent[i]

def union(a,b,parent,size):
    root_a = find(a,parent)
    root_b = find(b,parent)

    if root_a == root_b:
        return size[root_a]
    else:
        if size[root_a] < size[root_b]:
            root_a, root_b = root_b, root_a

        parent[root_b] = root_a

        size[root_a] += size[root_b]
        return size[root_a]
    

def answer(i):
    name2id = {'ChongChong':0}
    parent = [0]
    size = {}

    for _ in range(i):
        a, b = map(str,input().split())

        a_id = get_id(a, name2id, parent, size)
        b_id = get_id(b, name2id, parent, size)

        union(a_id, b_id, parent, size)

    print(parent)


answer(int(input()))
