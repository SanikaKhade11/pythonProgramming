from BT import*
##################take input level wise##############
def take_input_level_wise():
    data=int(input("Enter the data for the root : "))
    if (data==-1):
        return None
    
    root =binarytree(data)
    queue=deque([root])

    while len(queue) !=0:
        current_node=queue.popleft()
        left_child_data=int(input(f"Enter the left child for {current_node.data}"))
        if(left_child_data != -1):
            left_node = binarytree(left_child_data)
            current_node.left=left_node
            queue.append([left_node])

        right_child_data=int(input(f"Enter the right child for {current_node.data}"))   
        if(right_child_data != -1):
            right_node = binarytree(right_child_data)
            current_node.right=right_node
            queue.append([right_node])

    return root
root=take_input_level_wise()
print_binary_tree(root)