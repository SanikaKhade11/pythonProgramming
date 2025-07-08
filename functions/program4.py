#First none repeating character
def first_non_repeating_character(s):
    pass
    char_count = {}
    for char in s:
        char_count[char] = char_count.get(char, 0) + 1
    for char in s:
        if char_count[char]==1:
            print("Non_repeating character : ")
            return char
    return None

s="swiss"
print(first_non_repeating_character(s))