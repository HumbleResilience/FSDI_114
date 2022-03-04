# define function "is_anagram" <- parameters: string_a, string_b
#if length of string_a != length of string_b; then
#    return False
#
#string_a = uppercase(string_a)
#string_b = uppercase(string_b)
#char_list_a = list()
#char_list_b = list()
#loop through every character in string_a and store value temporarily in "char_a":
#      char_list.append(char_a) append char_a to char_list
#loop through every character in string_b and store value temporarily in "char_b":
#       append char_b to char_list_b


NO_OF_CHARS = 256

#user input
string_a = input("Enter string_a: ")
string_b = input("Enter string_b: ")
#check length of words
def is_anagram(string_a, string_b):

    #count arrays initialized to 0
    count1 = [0] * NO_OF_CHARS
    count2 = [0] * NO_OF_CHARS
    

    #for each char in input strings, increment count
    for char_a in string_a:
        count1[ord(char_a)] += 1
    
    for char_b in string_b:
        count2[ord(char_b)] +=1

    #checking length of words  
    if len(string_a) != len(string_b):
        return 0

    #compare the arrays
    for char in range(NO_OF_CHARS):
        if count1[char] != count2[char]:
            return 0

    return 1
    
if is_anagram(string_a, string_b):
    print("These are anagrams")

else:
    print("These are not anagrams")
        