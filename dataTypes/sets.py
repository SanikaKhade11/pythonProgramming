############sets##############
my_set={1,2,3,4,5,6, "hello", "world", 3.14, True, False, (3,5,6)}
print(my_set)
print(type(my_set))
print(len(my_set))
print(3 in my_set)

# set1={} ##this not a way to create set
# print(set1)
# print(type(set1))

# empty= set()   #to create empty set
# print(empty)
# print(type(empty))
# print(empty.add(1))  
# print(empty.add(2))
# print(empty.add(2))
# print(empty.add(("hi","how")))
# print(empty.add(("fine",(43,45))))
# print(empty.remove(1))
# print(empty.add(1))
# print(empty.discard(1))    #use this instead of remove  pop i snot work in set throw error when argument pass in it otherwise it pop randomaly  print(empty.pop())
# print(empty)

set1={1,2,2,2}
set2={1,2,3,4}
set1.union(set2)
print(set1.union(set2))
print(set1.intersection(set2))

# Program 4 - WAP list- History,Science, Java, Python,C , C++, jSS, .net, History,Science, Java,Java assume one class is required for 1 sub find how many class required for each subject
set_of_subject = {"History" , "Science" , "Java" , "Python" , "C" , "C++" , "jSS", ".net" , "History" , "Science" , "Java" , "Java"}
print(set_of_subject)
print(type(set_of_subject))
print("unique_subjects : " , set_of_subject )
print("Total classes required for each subject : ", len(set_of_subject))

# Program 6 - figure out a way to  store the value 9 and 9.0 in set  as a seperate value
a = set()
a.add(("int", 9))
a.add(("float", 9.0))
print(a)



