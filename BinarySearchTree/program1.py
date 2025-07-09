# 1. Node 2. edge 3. leaf  4.parent 5.child 6. root 7. Anceston 8. Predecessor 9. 10. level 11. path 

from  collections import*

class treenode:
    def __init__(self,data):
        self.data=data
        self.children=[]

root=treenode(1)
child1=treenode(2)
child2=treenode(3)
child3=treenode(4)

root.children.extend([child1,child2,child3])   #either used append or extend
print(root.children[0].data)

def print_tree(root):
    print(root.data)

    for eachchild in root.children:
        print_tree(eachchild)

print_tree(root)

def print_tree_imp(root):
    if root == None:
        return
    print(f"(root.data)" , end=',')
    
    for eachchild in root.children:
        print(eachchild.data, end=',')
    print()

    for eachchild in root.children:
        print_tree_imp(eachchild)

print_tree_imp(root)
