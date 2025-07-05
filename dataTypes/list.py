######List###########
myList=['1', '4' ,'3']
print(len(myList))
print(myList)
print(myList[0:1])
print(myList[2:])
print(myList[:-2])
print(type(myList))
myList.append(2)
print(myList)
myList.pop(2)  #indexing used for popping
print(myList)

#Program 1 - WAP to ask user enter the names of their three favourite movies and show them list ####
movies=[]
for i in range(3):
    movie = str(input(f"Enter the name of favourite movies {i+1} : "))
    movies.append(movie)
print("Favourite mmovies : " , movies)


#Program 3 - WAP to count no. of students with "A" grade in list and sort them
list= ['c', 'D', 'A', 'A', 'B', 'D' , 'C','A', 'A', 'D']
count_of_A = list.count('A')
sort_list= sorted(list, key=str.upper, reverse=True)   #desc
sort_list= sorted(list)
print("Sorted List : ", sort_list)
print("Number of students with grade A : ", count_of_A)

