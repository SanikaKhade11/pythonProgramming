#####tuple#############
tuple=(1,2,3,4,5,1,6,1)
print(tuple)
print(tuple.index(3))
print(tuple.count(1))

#Program 1- WAP to count no. of students with "A" grade in tuple ('c', D, A, A, B D C  A A D)###
tuple= ('c', 'D', 'A', 'A', 'B', 'D' , 'C','A', 'A', 'D')
count_of_A = tuple.count('A')
print("Number of students with grade A : ", count_of_A)
