from collections import*
class binarytree:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

root =binarytree(1)
root.left=binarytree(2)
root.left.left=binarytree(4)
root.left.right=binarytree(5)
root.right=binarytree(3)
root.right.left=binarytree(6)
root.right.left.left=binarytree(7)
root.right.left.right=binarytree(8)
root.right.left.right.left=binarytree(10)

def print_binary_tree(root):
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


print_binary_tree(root)
print_binary_tree(root.left)
print_binary_tree(root.left.left)
print_binary_tree(root.left.right)
print_binary_tree(root.right)
print_binary_tree(root.right.left)
print_binary_tree(root.right.left.left)
print_binary_tree(root.right.left.right)
print_binary_tree(root.right.left.right.left)
