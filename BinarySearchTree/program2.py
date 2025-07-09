##################program2####################

class BST():
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
        self.children=[]       

def print_BST(root):
    if root is None:
        return
    
    print(root.data, end=',')

    if(root.left is not None):
        print(f"L -> {root.left.data} ", end=',')
    else:
        print(f"L -> None" , end=',')

    if(root.right is not None):
        print(f"R -> {root.right.data} ", end=',')
    else:
        print(f"R -> None" , end=',')

    print()
    

def input_bst_manual():
    root1=BST(2)
    root1.left=BST(1)
    root1.right=BST(3)
    root2=BST(5)
    root2.left=BST(3)   
    root2.right=BST(7)
    root2.left.left=BST(2)
    root2.left.right=BST(4)
    root2.right.left=BST(6)
    root2.right.right=BST(8)

    root3=BST(10)
    root3.left=BST(8)   
    root3.right=BST(15)
    root3.right.left=BST(12)
    

    return root1, root2,root3
root1, root2,root3 = input_bst_manual()
print_BST(root1)
def sum_of_bst_nodes(root1):
    if root1 is None:
        return 0
    return root1.data + sum_of_bst_nodes(root1.left) + sum_of_bst_nodes(root1.right)

total=sum_of_bst_nodes(root1) 
print("sum of all nodes in BST Tree : ", total)
print("\nSecond BST")
print_BST(root2)
print_BST(root2.left)
print_BST(root2.right)
print("\nThird BST")
print_BST(root3)
print_BST(root3.left)
print_BST(root3.right)




################ Insert in BST###########

def insert_in_bst(root,value):
    if root is None:
        return BST(value)
    if value< root.data:
        root.left=insert_in_bst(root.left,value)
    else:
        root.right=insert_in_bst(root.right, value)
    return root

root1=insert_in_bst(root1, 4)
print("\nInsert 4 in root1 : " )
print_BST(root1)


##########Search in BST ############

def search_in_BST(root, value):
    if root is None:
        return False
    if root.data==value:
        return True
    elif value<root.data:
        return search_in_BST(root.left,value)
    else:
        return search_in_BST(root.right, value)
    
print("\nSearch 3 in root1 : ", search_in_BST(root1, 3))
print("\nSearch 9 in root2 : ", search_in_BST(root2, 9 ))


def delete_in_bst(root, value):
    if root is None:
        return None
    if value< root.data:
        root.left=delete_in_bst(root.left,value)
    elif value> root.data:
        root.right=delete_in_bst(root.right, value)
    else:
        if root.left is None:
            return root.right
        elif root.right is None:
            return root.left
        

#Program - WAP successor and predecessor in BST 
def find_successor(root , key):
    successor=None
    while root:
        if key < root.data:
            successor = root
            root = root.left
        elif key > root.data:
            root = root.right
        else:
            break
    return successor.data if successor else None
print("Successor is : ", find_successor(root2, 3))

def find_predecessor(root,key):
    predecessor=None
    while root:
        if key > root.data:
            predecessor=root
            root=root.right
        else:
            root=root.left
    return predecessor.data if predecessor else None
print("Predecessor is:", find_predecessor(root2, 5))
