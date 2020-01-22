"""
Binary Search Tree

Coded by Ömer Miraç Kökçam
omermirac.kokcam@gmail.com
"""


class Node:
    def __init__(self, val):
        #node yapılandırıcısı
        self.val = val
        self.left = None
        self.right = None



def insert(root,node):
    #agacin icine eleman ekleme
    if root is None:
        root = node
    else:
        if root.val < node.val:
            if root.right is None:
                root.right = node
            else:
                insert(root.right, node)
        else:
            if root.left is None:
                root.left = node
            else:
                insert(root.left, node)

r = Node(34)
insert(r, Node(54))
insert(r, Node(101))
insert(r, Node(48))
insert(r, Node(12))
insert(r, Node(9))
insert(r, Node(30))


def inorder(root):
    #kucukten buyuge dogru arama yapma
    if root is not None:
        inorder(root.left)
        print(root.val)
        inorder(root.right)
    else:
        return None

# inorder(r)
insert(r, Node(42))
inorder(r)
def reverse_inorder(root):
    #buyukten kucuge dogru sıralama yapma
    if root is not None:
        reverse_inorder(root.right)
        print(root.val)
        reverse_inorder(root.left)
    else:
        return None
reverse_inorder(r)


def search(root, key):
    #agac icinde arama yapma
    if root is None or root.val == key:
        return root.val

    if root.val < key:
        return search(root.right, key)
    else:
        return search(root.left, key)

print(search(r, 42))