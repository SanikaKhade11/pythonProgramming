from BT import*
###take input from user
def take_input():
    data=int(input("Enter the data for the node : "))

    if (data== -1):
        return None
    
    node=binarytree(data)

    print(f"enter the left child of {data}")
    node.left=take_input()

    print(f"Enter the right child of {data}")
    node.right=take_input()

    return node

root = take_input()

print_binary_tree(root)
