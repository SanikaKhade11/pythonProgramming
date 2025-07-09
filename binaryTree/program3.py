

from BT import*
def height(root):
    if(root is None):

        return 0
    
    left_height=height(root.left)
    right_height=height(root.right)

    heightoftree=1+max(left_height,right_height)

    return heightoftree
print("height of tree : ", height(root))

def diameter_of_tree(root):
    if (root is None):
        return 0

    left_height=height(root.left)
    right_height=height(root.right)

    left_diameter=diameter_of_tree(root.left)
    right_diameter=diameter_of_tree(root.right)

    ans=max(left_diameter,right_diameter, left_height,right_height)

    return ans

print("Diameter of tree : ", diameter_of_tree(root))

def count_nodes(root):
    if (root==None):
        return 0
    
    else:
        return 1 + count_nodes(root.left) + count_nodes(root.right)
    
print("Count of the nodes : ", count_nodes(root))

