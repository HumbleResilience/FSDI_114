class Stack:
    def __init__(self):
        self.items = []
    
    def is_empty(self):
        return self.items == []
    
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        return self.items.pop()
    
    def peek(self):
        return self.items[len(self.items)-1]
    
    def size(self):
        return len(self.items)

def is_match(p1, p2):
    if p1 == "(" and p2 == ")":
        return True
    elif p1 == "{" and p2 == "}":
        return True
    elif p1 == "[" and p2 == "]":
        return True
    else: 
        return False



def balance_check(s):
    stack = Stack()
    is_balanced = True
    index = 0

    string_length = len(s)
    if string_length % 2 == 1:
        return False
    else: 
        while index < len(s) and is_balanced:
            my_string = s[index]
            if my_string in "([{":
                stack.push(my_string)
            else:
                if stack.is_empty():
                    is_balanced = False

                else: 
                    top = stack.pop()
                    if not is_match(top, my_string):
                        is_balanced = False
            index += 1

        if stack.is_empty() and is_balanced:
            return True
        else:
                return False

print(balance_check("(((((())))))"))




















#         #valid_matches = [("(",")")], ("[","]"), ("{","}")
#         for char in s:
#             if char in [("(" or "{" or "[")]:
#                 s.append(char) #adding to stack
#             else:
#                 if not s:
#                     return False
#                 current_char = s.pop()
#                 if current_char == "(":
#                     if char != ")":
#                         return False
#                     if current_char == "{":
#                         if char != "}":
#                             return False
#                     if current_char == "[":
#                         if char != "]":
#                             return False

#         if s:
#             return False
#         return 

# userinput=input("Enter string: ")

