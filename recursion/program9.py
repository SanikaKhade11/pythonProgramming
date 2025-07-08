####Program - tower of hanoi
def tower_of_hanoi(n , source, destination, auxillary):
    if n==1:
        print(f"Move disk 1 from {source} to {destination} ")
        return
    tower_of_hanoi(n-1, source, auxillary, destination)
    print(f"Move disk {n} from {source} to {destination} ")

    tower_of_hanoi(n-1, auxillary,destination,source)

num_of_disk=int(input("Enter the number of disks : "))

print(f"Solving tower of hanoi with {num_of_disk} disks : ")
tower_of_hanoi(num_of_disk,'A','C','B')

