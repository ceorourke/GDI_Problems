class Node(object):
    """Node class used to create a binary tree"""

    def __init__(self, data, left=None, right=None):
        """Instantiate a node"""
        self.data = data
        self.left = left
        self.right = right

    def __repr__(self):
        """Override print with node data"""
        return "<Binary Node %s>" % self.data

def translate_morse_code(root, morse_code):
    """Translates morse code to English"""

    result = ""

    for item in morse_code:
        current = root
        for char in range(len(item)):
            if item[char] == ".":
                current = current.left
            else: 
                current = current.right
        result += current.data
    return result

root = Node("") # morse code tree
root.left = Node("e")
root.left.left = Node("i")
root.left.right = Node("a")
root.left.right.left = Node("r")
root.left.right.left.left = Node("l")
root.left.right.right = Node("w")
root.left.right.right.left = Node("p")
root.left.right.right.right = Node("j")
root.left.left.left = Node("s")
root.left.left.right = Node("u")
root.left.left.right.left = Node("f")
root.left.left.left.left = Node("h")
root.left.left.left.right = Node("v")
root.right = Node("t")
root.right.left = Node("n")
root.right.left.left = Node("d")
root.right.left.left.left = Node("b")
root.right.left.left.right = Node("x")
root.right.left.right = Node("k")
root.right.left.right.left = Node("c")
root.right.left.right.right = Node("y")
root.right.right = Node("m")
root.right.right.left = Node("g")
root.right.right.left.left = Node("z")
root.right.right.left.right = Node("q")
root.right.right.right = Node("o")

morse_code = ["....", ".."] #=> "hi"
print translate_morse_code(root, morse_code)
morse_code = ["--.","..", ".-.", ".-.."] #=> "girl"
print translate_morse_code(root, morse_code)
morse_code = ["--.", "-..", "..", "...", "..-."]
print translate_morse_code(root, morse_code) #=> "gdisf"


