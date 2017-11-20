def is_palindrome(phrase):
    """Returns whether a phrase is a palindrome or not"""

    phrase = strip_punctuation(phrase)

    for i in range(len(phrase) / 2):
        if phrase[i] != phrase[-i - 1]:
            return False

    return True

def strip_punctuation(phrase):
    """Removes punctuation, white space, and lowers all letters from a phrase"""

    new_phrase = [letter.lower() for letter in phrase if letter.isalpha()]
    return ''.join(new_phrase)


phrase = "Madam I'm Adam"
print is_palindrome(phrase) #=> true

phrase = "Hi, I'm Amelia"
print is_palindrome(phrase) #=> false

################################################################################

def is_palindrome_recursive(phrase):
    """Recursively returns whether a phrase is a palindrome"""

    phrase = strip_punctuation(phrase)

    if (len(phrase)) < 2:
        return True

    return phrase[0] == phrase[-1] and \
        is_palindrome(phrase[1:len(phrase) - 1])


phrase = "Madam I'm Adam"
print is_palindrome_recursive(phrase) #=> true

phrase = "Hi, I'm Amelia"
print is_palindrome_recursive(phrase) #=> false