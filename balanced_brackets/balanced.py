import re

class WithStack:
    """
    Does balanced brackets using a Stack
    """
    def __init__(self):
        print('initialised')

    def is_balanced(self, incoming: str) -> bool:
        st = []
        for c in incoming:
            # push openers onto stack
            if c in '({[':
                st.append(c)

            # check for a matching closing bracket
            elif c in '}])':
                if not st or (c == ')' and st[-1] != '(') or (c == '}' and st[-1] != '{') or (c == ']' and st[-1] != '['):
                    print(False)
                    break
                st.pop() # pop our matched bracket off

        # if the stack is empty, we are balanced?
        return (True if not st else False)


class WithCounters:
    """
    Does not enforce order, so not an actual working solution
    """
    def __init__(self):
        print('initialised')

    def is_balanced(self, incoming: str) -> bool:
        countera = 0
        counterb = 0
        counterc = 0
        for ch in incoming:
            if(ch == '('):
                countera += 1
            elif(ch == ')'):
                countera -= 1
            elif(ch == '{'):
                counterb += 1
            elif(ch == '}'):
                counterb -= 1
            elif(ch == '['):
                counterc += 1
            elif(ch == ']'):
                counterc -= 1

        if(countera == 0 and counterb == 0 and counterc == 0):
            return True
        else:
            return False


class WithRegex:
    """
    unreadbility, ho!
    Also, I don't think this passes the mismatched order thing either
    """
    def __init__(self):
        pass

    def is_balanced(self, incoming:str) -> bool:
        # Remove pairs of '()' until no more are found
        while re.search(r'\(\)', incoming):
            s = re.sub(r'\(\)', '', incoming)

        # If the string is empty, the parentheses are balanced
        return (True if not incoming else False)
