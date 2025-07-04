####dict#####
info={
    "key": "main",
    "name": "p",
    "learn" : "code",
    "age" :20,
    "is_student": True,
    "marks":92.4,
    "hobbies":["reading", "coding", "gaming"],
    "subject":["Maths","Science","history"]
}
print(type(info))
print(len(info))
print(info["name"])
print(info["hobbies"][1])
print(info["subject"][2])
print(info["marks"]*2)
print(info["key"].replace("main","main.py"))
print(info["learn"].upper())
print(info["key"].capitalize())
print(info["subject"][0].lower())
print(info["is_student"] and info["age"]>15)
print(info["age"]%3)
print(info.keys())
print(info.values())
print(info.items())
print(info.pop("age", "Age not found"))
print(info.popitem()) #remove and return the last inserted key-value pair
# print(info["place"])
print(info.clear())
print(info)
print(info.copy())
print(info.setdefault("new_key", "default_value"))
print(info.update({"extra_key": "extra_value"}))
print(info.get("key"))
print(info)
print(info.copy())

###Program 5 -make dict a- apple to z key- a value - apple
cap_alphabet_dict= {"A":"Apple", "B": "Ball", "C": "Cat" , "D": "Dog" , "E": "Elephant" , "F": "Frog" , "G": "Girl" , "H": "Horse" , "I": "Ice-cream", "J": "Joker", "K": "King", "L": "Lion", "M": "Monkey", "N": "Nose", "O": "Orange", "P": "Parrot", "Q": "Queen", "R": "Rose", "S": "Sun", "T": "Toy", "U": "Umbrella", "V": "Van", "W": "Wolf", "X": "X-Ray", "Y": "Yarn", "Z": "Zebra"}
print(cap_alphabet_dict)
print(cap_alphabet_dict.keys())
print(cap_alphabet_dict.values())
print(cap_alphabet_dict.items())
lower_alphabet={key.lower():value.lower() for key, value in cap_alphabet_dict.items()}
print("\nSmall alphabet a to z : ", lower_alphabet)
print(len(cap_alphabet_dict))

