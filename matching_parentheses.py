class Stack(object):
    """Stack implemented using a list."""

    def __init__(self):
        self._stack = []

    def push(self, item):
        """Add item to top"""

        self._stack.append(item)

    def pop(self):
        """Remove top item"""

        return self._stack.pop()

    def peek(self):
        """Look at the top item"""

        return self._stack[-1]

    def is_empty(self):
        """Is the stack empty?"""

        return not self._stack

def has_matching_parentheses(str):
    """Returns whether parentheses are balanced or not"""

    parens = Stack()
    left = {'(', '[', '{'}
    closed_matches = {')':'(', '}':'{',']':'['}

    for char in str:
        if char in left:
            parens.push(char)
        elif char in closed_matches:
            if parens.is_empty():
                return False
            # check if closed_matches[char] matches whatever's on top of the stack
            if parens.peek() == closed_matches[char]: # it's a match, pop it
                parens.pop()

    return parens.is_empty()

str = "{ different parens ]"
print has_matching_parentheses(str) #=> False

str = "]]] repeated close parens only"
print has_matching_parentheses(str) #=> False

str = "[({})]"
print has_matching_parentheses(str) #=> True

str = "((3+4)-(1+2))/(1+1)"
print has_matching_parentheses(str) #=> True

str = "(I(really)love al(g)orithms)"
print has_matching_parentheses(str) #=> True

str = ")hello("
print has_matching_parentheses(str) #=> False
