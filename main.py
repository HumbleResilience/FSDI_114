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




string_a = 'car'
string_b = 'rac'
#check length of words
def is_anagram(string_a, string_b):
    if len(string_a) != len(string_b):
        print("not anagrams")
    
    
#convert to uppercase
string_a = string_a.upper()
string_b = string_b.upper()

char_list_a  = []
char_list_b = []

for char_a in string_a:
    char_list_a.append(char_a)

for char_b in string_b:
    char_list_b.append(char_b)

    if char_a == char_b:
        print("These words are anagrams.")

is_anagram('car', 'RAC')