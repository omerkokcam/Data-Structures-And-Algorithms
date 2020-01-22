"""
Binary Tree

Coded by Ömer Miraç Kökçam
omermirac.kokcam@gmail.com
"""

class Node:


    def __init__(self,key):
        #yapılandırıcı
        self.val = key
        self.right = None
        self.left = None



#kök oluşturalım

root = Node('A')
root.left = Node('B')
root.left.left = Node('D')
root.right = Node('C')

